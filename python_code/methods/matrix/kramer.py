def kramer_method(matrix, free_column: list, level_of_detail: int = 3):
    """
    Решает СЛАУ методом Крамера

    Args:
        matrix (Matrix): матрица, относительно которой требуется решение
        free_column (list): столбец свободных членов
        level_of_detail (int): (int): уровень детализации (меньше число - больше деталей)

    Yields:
        dict: данные о текущем шаге решения

    Raises:
        ArithmeticError: если определитель матрицы равен нулю

    """
    def определитель(mat):
        return matrix.determinant.auto_det(mat)

    def calc_col_det(mat, free, col_no_):
        mat = mat.копия()
        mat.удалить_столбец(col_no_)
        mat.вставить_столбец(col_no_, free)
        det_ = определитель(mat)
        if level_of_detail < 3:
            answer.update({"Матрица с замененным столбцом": mat, "Определитель": det_})
        return det_

    answer = {}
    matrix = matrix.копия()
    main_det = определитель(matrix)
    if level_of_detail < 3:
        answer.update({'Этап': 'Получены данные', 'Матрица': matrix, 'Общий определитель': main_det})
        yield answer
        answer.pop('Общий определитель', None)
        answer.pop('Этап', None)
        answer.pop('Матрица', None)
    if main_det == 0:
        raise ArithmeticError("Метод крамера не работает с матрицами, определитель которых равен нулю")

    solution = []
    for col_no in range(matrix.количество_столбцов):
        if level_of_detail < 3:
            answer.update({"Номер столбца замены": col_no})
        solution.append(calc_col_det(matrix, free_column, col_no) / main_det)
        if level_of_detail < 2:
            answer.update({"Решение": f'X{col_no + 1} = определитель(matrix_{col_no}) / определитель(матрица) = '
                                      f'{answer["Определитель"]} / {main_det} = {answer["Определитель"] / main_det}'})
        if level_of_detail < 3:
            yield answer
    answer.pop("Номер столбца замены", None)
    answer.pop("Матрица с замененным столбцом", None)
    answer.pop("Определитель", None)
    answer.pop("Решение", None)
    if level_of_detail < 4:
        answer.update({"Решение": solution})
    yield answer
