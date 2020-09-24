from python_code.staf.sympy_init import *


def hords(function, section, accuracy_order=None, iterations=None, level_of_details=3):
    def draw_secant():
        return (left_edge * function(right_edge) - right_edge * function(left_edge)) / \
               (function(right_edge) - function(left_edge))

    def stop_iteration():
        accur = False
        iter_ = False
        if accuracy_order:
            accur = abs(suppression - old_c) < 10 ** (-accuracy_order) and \
                    function(suppression) < 10 ** (-accuracy_order)
        if iterations:
            iter_ = iterations < iteration_counter
        return accur or iter_

    if accuracy_order is None and iterations is None:
        accuracy_order = 8

    left_edge = min(section)
    right_edge = max(section)
    function = parse_expr(function)
    answer = {}
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
    suppression = None
    f_a = function(left_edge)
    f_c = None
    f_b = function(right_edge)
    iteration_counter = 1
    old_c = 1
    while True:
        if level_of_details < 3:
            answer.update({
                'Номер итерации': iteration_counter,
                'a': left_edge,
                'c': suppression,
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
        suppression = draw_secant()
        f_c = function(suppression)
        if level_of_details < 3:
            answer.update({
                'Номер итерации': iteration_counter,
                'a': None,
                'c': suppression,
                'b': None,
                'f(a)': None,
                'f(c)': f_c,
                'f(b)': None
            })
            yield answer
            answer.pop('Номер итерации', None)
            answer.pop('a', None)
            answer.pop('c', None)
            answer.pop('b', None)
            answer.pop('f(a)', None)
            answer.pop('f(c)', None)
            answer.pop('f(b)', None)
        if stop_iteration():
            if level_of_details < 4:
                answer.update({'Решение': suppression})
            if level_of_details < 3:
                answer.update({'f(c)': f_c})
            yield answer
            break
        old_c = suppression
        if function(left_edge) * function(suppression) > 0:
            left_edge = suppression
            suppression = None
        else:
            right_edge = suppression
            suppression = None
        f_a = function(left_edge)
        f_c = None
        f_b = function(right_edge)
        iteration_counter += 1
