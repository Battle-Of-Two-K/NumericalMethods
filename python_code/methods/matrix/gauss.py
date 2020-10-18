def gauss_method(matrix, free_column: list, level_of_details: int = 3):
    """
    Решает СЛАУ методом Гаусса

    Args:
        matrix (Matrix): матрица, относительно которой требуется решение
        free_column (list): столбец свободных членов
        level_of_details (int): уровень детализации (меньше число - больше деталей)

    Yields:
        dict: данные о текущем шаге решения

    """
    matrix = matrix.копия()
    # Добавляем столбец свободных членов
    matrix.добавить_столбец(free_column)
    # Преобразуем матрицу в треугольную с нулями под главной диагональю и единицами в главной диагонали
    matrix = matrix.триангулировать_до_единиц_в_диагонали()
    if level_of_details < 3:
        yield {
            'Этап': 'Закончился первый проход',
            'Матрица': matrix
        }
    solution = [0 for _ in range(matrix.количество_строк)]
    free_column = matrix.удалить_столбец(matrix.количество_столбцов - 1)
    for row_no in reversed(range(matrix.количество_строк)):
        for col_no in range(matrix.количество_строк):
            free_column[row_no] -= solution[col_no] * matrix.матрица[row_no][col_no]
        solution[row_no] = free_column[row_no]
    if level_of_details < 4:
        yield {
            'Решение': solution
        }
