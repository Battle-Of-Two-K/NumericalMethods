def gauss_method(matrix, free_column, print_middle_values=False):
    """Решает матрицу методом Гаусса"""
    matrix = matrix.copy()
    # Добавляем столбец свободных членов
    matrix.append_column(free_column)
    # Преобразуем матрицу в треугольную с нулями под главной диагональю и единицами в главной диагонали
    matrix = matrix.triangulate_to_ones()
    if print_middle_values:
        print('\nЗакончился первый проход')
        matrix.console_display()
    solution = [0 for _ in range(matrix.rows)]
    free_column = matrix.pop_column(matrix.columns - 1)
    for row_no in reversed(range(matrix.rows)):
        for col_no in range(matrix.rows):
            free_column[row_no] -= solution[col_no] * matrix.matrix[row_no][col_no]
        solution[row_no] = free_column[row_no]
    return solution
