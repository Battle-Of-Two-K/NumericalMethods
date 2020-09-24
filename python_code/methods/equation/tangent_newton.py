from python_code.staf.sympy_init import *


def tangent_newton(function, section, accuracy_order=None, iterations=None, level_of_details=3):
    def draw_tangent():
        return value - function(value) / function_d(value)

    def stop_iterations():
        return iteration_counter > iterations

    left_edge = min(section)
    right_edge = max(section)
    function = parse_expr(function)
    function = simplify(function)
    function_d = diff(function)
    function_dd = diff(function_d)
    answer = {}
    if level_of_details < 3:
        answer.update({
            'Этап': 'Получены значения',
            'Отрезок': (left_edge, right_edge),
            'Введенная функция': function,
            'Красиво введенная функция': pretty(function, use_unicode=False),
            'Ее производная': function_d,
            'Красиво ее производная': pretty(function_d, use_unicode=False),
            'Ее вторая производная': function_dd,
            'Красиво ее вторая производная': pretty(function_dd, use_unicode=False)
        })
        yield answer
        answer.pop('Этап', None)
        answer.pop('Отрезок', None)
        answer.pop('Введенная функция', None)
        answer.pop('Красиво введенная функция', None)
        answer.pop('Ее производная', None)
        answer.pop('Красиво ее производная', None)
        answer.pop('Ее вторая производная', None)
        answer.pop('Красиво ее вторая производная', None)
    function = lambdify(x, function)
    function_d = lambdify(x, function_d)
    function_dd = lambdify(x, function_dd)
    if function(right_edge) * function_dd(right_edge) > 0:
        value = right_edge
    else:
        value = left_edge
    iteration_counter = 1
    while True:
        if level_of_details < 3:
            answer.update({
                'Номер итерации': iteration_counter,
                'a_n-1': value,
                'f(a_n-1)': function(value),
                'f\'(a_n-1)': function_d(value),
                "f''(a_n-1)": function_dd(value)
            })
            value = draw_tangent()
            answer.update({'a_n': value})
            yield answer
            answer.pop('Номер итерации', None)
            answer.pop('a_n-1', None)
            answer.pop('f(a_n-1)', None)
            answer.pop('f\'(a_n-1)', None)
            answer.pop("f''(a_n-1)", None)
            answer.pop('a_n', None)
        if stop_iterations():
            if level_of_details < 4:
                answer.update({'Решение': value})
            yield answer
            break
        iteration_counter += 1
