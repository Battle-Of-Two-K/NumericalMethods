import matplotlib.pyplot as plt
from python_code.main import *
from sympy.abc import x


try:
    # Ввод исходных данных:
    print('\n' + "___Тема: решение краевой задачи для ОДУ___".center(100))
    print("_________Метод конечных разностей_________".center(100) + '\n')
    print("-" * 100)
    print("*Примечание: дан отрезок [a, b], дано уравнение вида K(x)*y'' +L(x)*y' + M(x)*y = F(x), а также даны")
    print("краевые (граничные) условия 3-го рода на границах отрезка: R*y'(a) + S*y(a) = T и V*y'(b) + W*y(b) = Z")
    print("-" * 100)
    print()

    # Вариант из методички (работает, можно проверить)
    # a = 1
    # b = 10
    # h = 9 / 4
    # K = 2 * x ** 2
    # L = x
    # M = 1
    # F = 2 * x ** .5
    # R = 0
    # S = 1
    # T = 2
    # V = 0
    # W = 1
    # Z = 2 * 10 ** 0.5

    # Вариант из методички №2 (работает, можно проверить)
    # a = 0
    # b = 4
    # h = 1
    # K = 2
    # L = 2
    # M = -4
    # F = 1 - 2 * x
    # R = 0
    # S = 1
    # T = 1
    # V = 2
    # W = 4
    # Z = 9

    # Мой вариант (вариант 7):
    # a = -3
    # b = -2
    # h = 0.2
    # K = 2
    # L = -1
    # M = 4
    # F = -(x ** 2) - 3 * x + 5
    # R = 0
    # S = -4
    # T = 1
    # V = 0
    # W = -4
    # Z = 5

    # Мой вариант (вариант 7) Дз:
    a = -3
    b = -2
    h = 0.2
    K = 1
    L = -1
    M = 2
    F = -3 * x ** 2 + 3 * x - 4
    R = -2
    S = -7
    T = 6
    V = 2
    W = 6
    Z = -2

    # -----------------------
    # Ниже программный код!!!
    # -----------------------

    y_a = T / S
    y_b = Z / W

    # Первая итерация
    b_1 = -R / h + S
    c_1 = R / h
    d_1 = T

    # Последняя итерация
    a_n = V / h
    b_n = -V / h - W
    d_n = -Z

    def rounded_list(values: list, quantity: int = 9):
        """
        Округление элементов списка.

        Args:
            values (list): список значений
            quantity (int): точность округления
        Returns:
            list: список с округлёнными элементами

        """
        return [round(value, quantity) for value in values]

    def number_of_segments():
        """
        Returns:
            int: возвращает количество отрезков одинаковой длины
        """
        return int((b - a) / h)

    def all_x():
        """
        Returns:
            list: возвращает список всех значений x от a до b
        """
        output = a
        list_x = []
        for step in range(1, number_of_segments() + 2):
            list_x.append(output)
            output += h
        return rounded_list(list_x)

    def all_a():
        """
        Returns:
            list: возвращет список всех значений a_i
        """
        list_a = []
        for step in all_x():
            new_a = parse_expr(str(K)).evalf(subs={x: step}) / (h ** 2) -\
                    parse_expr(str(L)).evalf(subs={x: step}) / (2 * h)
            list_a.append(new_a)
        list_a.pop(0)
        n = len(list_a) - 1
        list_a.pop(n)
        list_a.insert(n, a_n)
        return rounded_list(list_a)

    def all_b():
        """
        Returns:
            list: возвращает спсиок всех значений b_i
        """
        list_b = []
        for step in all_x():
            new_a = -2 * parse_expr(str(K)).evalf(subs={x: step}) /\
                    (h ** 2) + parse_expr(str(M)).evalf(subs={x: step})
            list_b.append(new_a)
        list_b.pop(0)
        list_b.insert(0, b_1)
        n = len(list_b) - 1
        list_b.pop(n)
        list_b.insert(n, b_n)
        return rounded_list(list_b)

    def all_c():
        """
        Returns:
            list: возвращет список всех значений с_i
        """
        list_c = []
        for step in all_x():
            new_a = parse_expr(str(K)).evalf(subs={x: step}) / (h ** 2) +\
                    parse_expr(str(L)).evalf(subs={x: step}) / (2 * h)
            list_c.append(new_a)
        list_c.pop(0)
        list_c.insert(0, c_1)
        list_c.pop()
        return rounded_list(list_c)

    def all_d():
        """
        Returns:
            list: возвращет список всех значений d_i
                  (он же столбец свободных членов)
        """
        list_d = []
        for step in all_x():
            new_a = parse_expr(str(F)).evalf(subs={x: step})
            list_d.append(new_a)
        list_d.pop()
        list_d.insert(len(list_d), d_n)
        list_d.pop(0)
        list_d.insert(0, d_1)
        return rounded_list(list_d)

    def fill_triple_from_lists(list_up: list, list_middle: list, list_down: list) -> Matrix:
        """
        Заполняет трехдиагональную матрицу, используя 3 списка

        Args:
            list_up (list): список над главной диагональю
            list_middle (list): список главной диагонали
            list_down (list): список под главной диагональю

        Returns:
            Matrix: заполненная трехдиагональная матрица
        """
        out_matrix = Matrix(len(list_middle))

        for row_no, col_no in out_matrix:
            if row_no == col_no - 1:
                out_matrix[row_no][col_no] = list_up[row_no]
            if row_no == col_no:
                out_matrix[row_no][col_no] = list_middle[row_no]
            if row_no - 1 == col_no:
                out_matrix[row_no][col_no] = list_down[col_no]

        return out_matrix

    def main():
        matrix = fill_triple_from_lists(
            all_c(),
            all_b(),
            all_a(),
        )

        print(f'Столбец свободных членов {all_d()}')
        print(matrix.map(float).to_pretty_string())

        free_column = all_d()
        decision = iterations.triple_diagonal(matrix, free_column, level_of_detail=2)
        solution = None
        for step in decision:
            solution = step.get("Решение")
            print(f'y: {step}')
        print(f'x: {all_x()}')

        # \\\\\\\\\\\\\\\\\\\\\\\
        # Красивый вывод графика
        # \\\\\\\\\\\\\\\\\\\\\\\

        figure, axes = plt.subplots()
        Y = solution
        X = all_x()
        axes.grid()
        axes.scatter(X, Y, color='red')
        axes.set_title('Метод конечных разностей')
        plt.show()

    main()

except Exception as error:
    print(error)
input('\nНажмите "Enter" чтобы выйти...')
