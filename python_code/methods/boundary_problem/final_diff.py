import re

from examples.triplediagonal import fill_triple_from_lists
from python_code.methods.matrix.iterations import triple_diagonal
from python_code.staf.sympy_init import *


def final_difference_method(equation: str, boundaries_in: dict, boundary_x: tuple,
                            num_of_sections: int = 4, section_step: float = None,
                            level_of_detail: int = 3):
    """
    Решение краевой задачи для ОДУ методом конечных разностей

    Args:
        equation (str): уравнение
        boundaries_in (dict): краевые условия
        boundary_x (tuple): краевые иксы (2 значения)
        num_of_sections (int): количество отрезков
        section_step (float): шаг (имеет приоритет над num_of_sections)
        level_of_detail (int): уровень детализации

    Yields:
        dict: значения шага решения

    """

    def get_boundaries(expression):
        klm_re = "(?:(?P<K>.*y'{2})|(?P<L>.*y'{1})|(?P<M>.*y))"
        group_names = list('KLM')

        out = dict()
        left, right = expression.split('=')
        re.findall(klm_re, left)
        print()
        for match in re.finditer(klm_re, left):
            for name in group_names:
                if match.group(name):
                    out.update({name: parse_expr(match.group(name).replace("'", '')).subs({y: 1})})
        out.update({'F': parse_expr(right)})
        out.update({
            'W': boundary_x[0],
            'Z': out['F'].evalf(subs={x: boundary_x[1]})
        })

        return out

    def get_a_x(x_value):
        return boundaries['K'].evalf(subs={x: x_value}) / section_x_len ** 2 - \
               boundaries['L'].evalf(subs={x: x_value}) / (2 * section_x_len)

    def get_b_x(x_value):
        return -2 * boundaries['K'].evalf(subs={x: x_value}) / (section_x_len ** 2) + \
               boundaries['M'].evalf(subs={x: x_value})

    def get_c_x(x_value):
        return boundaries['K'].evalf(subs={x: x_value}) / section_x_len ** 2 + \
               boundaries['L'].evalf(subs={x: x_value}) / (2 * section_x_len)

    def get_d_x(x_value):
        return boundaries['F'].evalf(subs={x: x_value})
    if section_step is not None:
        section_x_len = section_step
    else:
        section_x_len = (boundary_x[1] - boundary_x[0]) / num_of_sections  # h
    boundaries = get_boundaries(equation)
    boundaries.update({key: parse_expr(str(boundaries_in[key])) for key in boundaries_in})

    if level_of_detail < 3:
        yield {
            'Выражение': equation,
            'h': section_x_len,
            **boundaries
        }

    points_x = [boundary_x[0] + section * section_x_len for section in range(num_of_sections + 1)]

    diagonal_a = [get_a_x(value) for value in points_x]
    diagonal_b = [get_b_x(value) for value in points_x]
    diagonal_c = [get_c_x(value) for value in points_x]
    free_col_d = [get_d_x(value) for value in points_x]

    diagonal_a.pop(0)
    diagonal_b[0] = -boundaries['R'] / section_x_len + boundaries['S']
    diagonal_c[0] = boundaries['R'] / section_x_len
    free_col_d[0] = boundaries['T']
    free_col_d[-1] = -boundaries['Z']
    diagonal_a[-1] = boundaries['V'] / section_x_len
    diagonal_b[-1] = -boundaries['V'] / section_x_len - boundaries['W']
    diagonal_c.pop(-1)

    free_col_d = list(map(float, free_col_d))

    if level_of_detail < 3:
        yield {
            'Список значений c': diagonal_c,
            'Список значений b': diagonal_b,
            'Список значений a': diagonal_a,
            'Список значений d': free_col_d,
        }

    matrix = fill_triple_from_lists(diagonal_c,
                                    diagonal_b,
                                    diagonal_a).map(lambda val: val if isinstance(val, int) else float(val))

    if level_of_detail < 3:
        drop_matrix = matrix.copy()
        drop_matrix.append_column(free_col_d)
        yield {
            'Матрица': drop_matrix
        }

    decision = triple_diagonal(matrix, free_col_d, level_of_detail=level_of_detail)
    solution = None
    for step in decision:
        if level_of_detail < 3 and not 'Решение' in step:
            yield step
        solution = step.get('Решение')
    solution = list(map(float, solution))
    if level_of_detail < 4:
        yield {
            'Решение': {
                'X': points_x,
                'Y': solution
            }
        }
