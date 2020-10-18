from math import atan, cos, sin, pi


def method_rot_yakobi(matrix,
                      iterations: int = 8,
                      level_of_detail: int = 3):
    """
    Нахождение собственных чисел и векторов методом вращения Якоби

    Args:
        matrix (Matrix): матрица у которой необходимо найти собственные числа и векторы
        iterations (int): количество итераций, которое необходимо совершить
        level_of_detail (int): уровень детализации (меньше число - больше деталей)

    Yields:
        dict: данные о текущем шаге решения

    """
    def find_max_abs_elem_above_diagonal():
        """Находит координаты элемента с наибольшим максимальным абсолютным значением выше главной диагонали"""
        max_elem_row = 0
        max_elem_col = 1
        max_elem = abs(matrix[max_elem_row][max_elem_col])
        for row_no, col_no in matrix:
            if row_no < col_no:
                if abs(matrix[row_no][col_no]) > max_elem:
                    max_elem = abs(matrix[row_no][col_no])
                    max_elem_row = row_no
                    max_elem_col = col_no
        return max_elem_row, max_elem_col

    def calc_phi(cords_):
        """Рассчитывает угол поворота фи"""
        row_no_, col_no_ = cords_
        try:
            return atan(2 * matrix[row_no_][col_no_] / (matrix[row_no_][row_no_] - matrix[col_no_][col_no_])) / 2
        except ZeroDivisionError:
            return pi / 4 if matrix[row_no_][col_no_] > 0 else -pi / 4

    def build_rot_matrix(phi_, cords_):
        """Создает матрицу поворота"""
        row_no_, col_no_ = cords_
        h_matrix = matrix.обернуть(*matrix.размер)
        h_matrix.заполнить_до_единичной()
        h_matrix[row_no_][row_no_] = cos(phi_)
        h_matrix[row_no_][col_no_] = -sin(phi_)
        h_matrix[col_no_][row_no_] = sin(phi_)
        h_matrix[col_no_][col_no_] = cos(phi_)
        return h_matrix

    def extract_diagonal():
        """Получает значения из главной диагонали"""
        diagonal = []
        for row_no_, col_no_ in matrix:
            if row_no_ == col_no_:
                diagonal.append(matrix[row_no_][col_no_])
        return diagonal

    def get_own_vectors():
        def row_div(row: list, n):
            return [element / n for element in row]

        # Перемножение матриц вращения
        own_vectors_matrix = matrix.обернуть(*matrix.размер)
        own_vectors_matrix.заполнить_до_единичной()
        for mat in rotation_matrix_list:
            own_vectors_matrix *= mat

        # Нормировка столбцов итоговой матрицы
        own_vectors_matrix = own_vectors_matrix.транспонированная
        for row_no in range(own_vectors_matrix.количество_строк):
            own_vectors_matrix.матрица[row_no] = row_div(own_vectors_matrix[row_no],
                                                         matrix.обернуть([own_vectors_matrix[row_no]]).векторная_норма_1)
        own_vectors_matrix = own_vectors_matrix.транспонированная

        # Вырезание столбцов из матрицы
        own_vectors_list = []
        for col_no in range(own_vectors_matrix.количество_столбцов):
            own_vectors_list.append(own_vectors_matrix.удалить_столбец(0))
        return own_vectors_list

    answer = {}
    matrix = matrix.копия()
    if matrix.количество_строк < 2 or matrix.количество_столбцов < 2:
        return {'Решение': {'Собственные числа': matrix[0][0], 'Собственные векторы': [[1]]}}
    if not matrix.симметричная_ли:
        raise ArithmeticError("Метод вращения Якоби применим только для симметричных матриц")
    rotation_matrix_list = []
    for iteration_counter in range(iterations):
        cords_of_max_abs_elem_above_diagonal = find_max_abs_elem_above_diagonal()
        phi = calc_phi(cords_of_max_abs_elem_above_diagonal)
        rotation_matrix = build_rot_matrix(phi, cords_of_max_abs_elem_above_diagonal)
        # Ошибка в методичке? написано произведение матриц вращения,
        # но правильно произведение транспонированных матриц вращения
        rotation_matrix_list.append(rotation_matrix)
        matrix_for_out = rotation_matrix.транспонированная * matrix
        matrix = (rotation_matrix.транспонированная * matrix * rotation_matrix)
        if level_of_detail < 3:
            answer.update({
                'Номер итерации': iteration_counter,
                'Угол поворота фи': phi,
                'Матрица поворота H': rotation_matrix,
                'Транспонированная матрица поворота': rotation_matrix.транспонированная,
                'Матрица A после поворота': matrix,
                'Матрица произведение (H.транспонированная * A)': matrix_for_out
            })
            yield answer
    answer.pop('Номер итерации', None)
    answer.pop('Матрица поворота H', None)
    answer.pop('Транспонированная матрица поворота', None)
    answer.pop('Матрица A после поворота', None)
    if level_of_detail < 4:
        answer.update({'Решение': {'Собственные числа': extract_diagonal(), 'Собственные векторы': get_own_vectors()}})
    yield answer
