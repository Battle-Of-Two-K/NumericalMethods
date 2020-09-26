from python_code.staf.sympy_init import *


def iterations(function, section, g_function=None, accuracy_order=8, iterations=None, level_of_details=3):

    def stop_iteration():
        if iteration_counter > (100 if iterations is None else iterations * 10):
            raise IndexError(f"\nОбнаружено нарушение работы функции. Работа аварийно остановлена. Сводка:\n"
                             f"abs(f(x)): {abs(function(x_value))} < {10 ** (-accuracy_order)} "
                             f"-> {abs(function(x_value)) < 10 ** (-accuracy_order)}\n"
                             f"abs(old_x - x): {abs(old_x_value - x_value)} < {10 ** (-accuracy_order)} -> "
                             f"{abs(function(x_value)) < 10 ** (-accuracy_order)}\n"
                             f"i: {iteration_counter} >= {iterations} -> {iteration_counter >= iterations}\n"
                             f"Для нормальной остановки требуется, чтобы все значения были True")
        return all([
            True if accuracy_order is None else abs(function(x_value)) < 10 ** (-accuracy_order),
            True if accuracy_order is None else abs(old_x_value - x_value) < 10 ** (-accuracy_order),
            True if iterations is None else iteration_counter >= iterations,
        ])

    left_edge = min(section)
    right_edge = max(section)
    function = simplify(parse_expr(function))
    if g_function is None:
        solving = map(simplify, solve(function.subs(x ** 3, y ** 3), y))
        try:
            g_function = solve(function.subs(x**3, y**3), y)[0]
            min_len = len(str(g_function))
            for new_g_function in solving:
                if len(str(new_g_function)) < min_len and 'I' not in str(new_g_function):
                    min_len = len(str(new_g_function))
                    g_function = new_g_function
        except IndexError:
            raise IndexError("Вероятно, не был найден способ преобразования функции к виду x = g(x)")
    else:
        g_function = simplify(parse_expr(g_function))
    g_function_d = simplify(diff(g_function))
    if level_of_details < 3:
        yield {
            'Этап': 'Получены значения',
            'Отрезок': (left_edge, right_edge),
            'Введенная функция': function,
            'Красиво введенная функция': pretty(function, use_unicode=False),
            'g(x)': g_function,
            'Красиво g(x)': pretty(g_function, use_unicode=False),
            "g'(x)": g_function_d,
            "Красиво g'(x)": pretty(g_function_d, use_unicode=False)
        }
    function = lambdify(x, function)
    g_function = lambdify(x, g_function)
    g_function_d = lambdify(x, g_function_d)
    iteration_counter = 1
    if abs(g_function_d(right_edge)) < 1:
        x_value = right_edge
    else:
        x_value = left_edge
    if level_of_details < 3:
        yield {
            'Номер итерации': iteration_counter,
            'x': x_value,
            'f(x)': function(x_value),
            'g(x)': g_function(x_value),
            "g'(x)": g_function_d(x_value)
        }
    while True:
        old_x_value = x_value
        x_value = g_function(x_value)
        if stop_iteration():
            if level_of_details < 3:
                yield {'Решение': x_value, }
            else:
                yield {}
            break
        iteration_counter += 1
        if level_of_details < 3:
            yield {
                'Номер итерации': iteration_counter,
                'x': x_value,
                'f(x)': function(x_value),
                'g(x)': g_function(x_value),
                "g'(x)": g_function_d(x_value)
            }
