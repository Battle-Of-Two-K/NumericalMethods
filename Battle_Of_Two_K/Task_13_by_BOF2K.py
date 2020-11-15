from python_code.main import *
from sympy.abc import x

try:
    # Ввод исходных данных:
    print("\n                             ___Тема: решение краевой задачи для ОДУ___")
    print("                             _________Метод конечных разностей_________\n")
    print("-" * 100)
    print("*Примечание: дан отрезок [a, b], дано уравнение вида K(x)*y'' +L(x)*y' + M(x)*y = F(x), а также даны")
    print("краевые (граничные) условия 3-го рода на границах отрезка: R*y'(a) + S*y(a) = T и V*y'(b) + W*y(b) = Z")
    print("                          небольшая подсказка: R и V во всех вариантах равны 0")
    print("-" * 100)
    print("* - умножение")
    print("** - возведение в степень")
    print("6.5 - число с плавающей точкой (да, ставить нужно именно ТОЧКУ, а не запятую)")
    print("-" * 100)
    print("Введите свои данные (если не понятно, что вводить, но смотрите примечание выше или же читайте методичку):\n")
    a = input("a = ")
    b = input("b = ")
    h = input("h = ")
    K = input("K(x) = ")
    L = input("L(x) = ")
    M = input("M(x) = ")
    F = input("F(x) = ")
    R = input("R = ")
    S = input("S = ")
    T = input("T = ")
    V = input("V = ")
    W = input("W = ")
    Z = input("Z = ")

    # Вариант из методички
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
    # Z = 2 * 10 * 0.5

    # -------------------------------------------
    # Предупреждение!!! Ниже программный код!!!
    # -------------------------------------------

    y_a = T / S
    y_b = Z / W

    # Первая итерация
    b_1 = -R / h + S
    c_1 = R / h
    d_1 = T

    # Последняя итерация
    a_n = V / h
    b_n = -V / h + W
    d_n = -Z


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
        while output <= b:
            list_x.append(output)
            output += h
        return list_x


    def all_a():
        """
        Returns:
            list: возвращет список всех значений a_i
        """
        list_a = []
        for step in all_x():
            new_a = K.evalf(subs={x: step}) / (h ** 2) - L.evalf(subs={x: step}) / (2 * h)
            list_a.append(new_a)
        list_a.pop(0)
        n = len(list_a) - 1
        list_a.pop(n)
        list_a.insert(n, a_n)
        return list_a


    def all_b():
        """
        Returns:
            list: возвращает спсиок всех значений b_i
        """
        list_b = []
        for step in all_x():
            new_a = -2 * K.evalf(subs={x: step}) / (h ** 2) + parse_expr(str(M))
            list_b.append(new_a)
        list_b.pop(0)
        list_b.insert(0, b_1)
        n = len(list_b) - 1
        list_b.pop(n)
        list_b.insert(n, b_n)
        return list_b


    def all_c():
        """
        Returns:
            list: возвращет список всех значений с_i
        """
        list_c = []
        for step in all_x():
            new_a = K.evalf(subs={x: step}) / (h ** 2) + L.evalf(subs={x: step}) / (2 * h)
            list_c.append(new_a)
        list_c.pop(0)
        list_c.insert(0, c_1)
        n = len(list_c) - 1
        list_c.pop(n)
        return list_c


    def all_d():
        """
        Returns:
            list: возвращет список всех значений d_i
                  (он же столбец свободных членов)
        """
        list_d = []
        for step in all_x():
            new_a = F.evalf(subs={x: step})
            list_d.append(new_a)
        return list_d


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
                out_matrix[row_no][col_no] = list_up[col_no - 1]
            if row_no == col_no:
                out_matrix[row_no][col_no] = list_middle[row_no]
            if row_no - 1 == col_no:
                out_matrix[row_no][col_no] = list_down[row_no - 1]

        return out_matrix


    def progonka():
        matrix = fill_triple_from_lists(
            all_c(),
            all_b(),
            all_a(),
        )

        matrix.console_display()

        free_column = all_d()
        decision = iterations.triple_diagonal(matrix, free_column, level_of_detail=2)
        decision = iterations.triple_diagonal(matrix, free_column, level_of_detail=3)

        solution = None
        for step in decision:
            solution = step.get("Решение")
            print(step)


    progonka()

except Exception as error:
    print(error)
input('\nНажмите "Enter" чтобы выйти...')
