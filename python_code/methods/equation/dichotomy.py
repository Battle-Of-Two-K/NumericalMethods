from math import log10, ceil

from python_code.staf.sympy_init import *


def dichotomy(function, section, accuracy_order=None, iterations=None, level_of_details=3):
    def find_center():
        return (right_edge + left_edge) / 2

    def get_section_len():
        return right_edge - left_edge

    def accuracy():
        return ceil(log10(get_section_len() / 2))

    def get_root():
        if accuracy() < 0:
            str_root = str(find_center())
            return float(str_root[:str_root.index('.') + abs(accuracy())])
        else:
            return None

    if accuracy_order is None and iterations is None:
        accuracy_order = 8

    answer = {}
    left_edge = min(section)
    right_edge = max(section)
    function = parse_expr(function)
    if level_of_details < 3:
        answer.update({
            'Этап': 'Получены значения',
            'Отрезок': (left_edge, right_edge),
            'Введенная функция': function,
            'Красиво введенная функция': pretty(function, use_unicode=False),
        })
        yield answer
        answer.pop('Этап', None)
        answer.pop('Отрезок', None)
        answer.pop('Введенная функция', None)
        answer.pop('Красиво введенная функция', None)
    function = lambdify(x, function)
    center = find_center()
    iteration_counter = 1
    while True:
        f_a = function(left_edge)
        f_c = function(center)
        f_b = function(right_edge)
        if level_of_details < 3:
            answer.update({
                'Номер итерации': iteration_counter,
                'a': left_edge,
                'c': center,
                'b': right_edge,
                'f(a)': f_a,
                'f(c)': f_c,
                'f(b)': f_b
            })
            yield answer
            answer.pop('Номер итерации', None)
            answer.pop('a', None)
            answer.pop('c', None)
            answer.pop('b', None)
            answer.pop('f(a)', None)
            answer.pop('f(c)', None)
            answer.pop('f(b)', None)
        if accuracy_order and abs(accuracy()) > accuracy_order or iterations and iterations < iteration_counter:
            if level_of_details < 4:
                answer.update({'Решение': get_root()})
            if level_of_details < 3:
                answer.update({
                    'Последний отрезок': (left_edge, right_edge),
                    'Длина последнего отрезка': get_section_len(),
                    'Середина последнего отрезка': find_center()
                })
            yield answer
            break
        if f_a * f_c < 0:
            right_edge = center
        else:
            left_edge = center
        center = find_center()
        iteration_counter += 1
