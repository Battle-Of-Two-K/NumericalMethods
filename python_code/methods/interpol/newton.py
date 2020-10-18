from python_code.staf.sympy_init import *


def newton_pol(x_list_of_values, y_list_of_values):
    if len(x_list_of_values) != len(y_list_of_values):
        raise IndexError("Количество занчений X не совпадает с количеством значений Y")
    if len(x_list_of_values) < 2:
        raise IndexError("Недостаточно точек для применения метода")

    def shuffle_list(target_list) -> list:
        out = []
        for element_no in reversed(range(len(target_list) // 2)):
            out.append(target_list[element_no - 1])
            out.append(target_list[element_no + 1])
        return out

    function_value = [y_list_of_values]
    x_list = x_list_of_values.копия()
    for col_no in range(1, len(x_list_of_values)):
        new_col = []
        for row_no in range(len(function_value[col_no - 1]) - 1):
            if col_no % 2 != 0 or row_no % 2 == 0:
                x_n_1 = x_list[row_no * col_no + 1]
                x_n_0 = x_list[row_no * col_no]
            else:
                x_n_1 = x_list[row_no * col_no]
                x_n_0 = x_list[row_no * col_no + 1]
            new_col.append((function_value[col_no - 1][row_no + 1] - function_value[col_no - 1][row_no]) /
                           (x_n_1 - x_n_0))
        function_value.append(new_col)
        x_list = shuffle_list(x_list)
    polynomial = 0
    for row_no in range(len(function_value)):
        line = 1
        for x_no in range(row_no):
            line *= x - x_list_of_values[x_no]
        polynomial += function_value[row_no][0] * line
    return {
        'Полный многочлен': polynomial,
        'Упрощенный многочлен': simplify(polynomial),
        'Функция python': lambdify(x, simplify(polynomial))
    }
