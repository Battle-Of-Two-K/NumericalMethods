def gauss_method(matrix, free_column, print_middle_values=False):
    """Решает матрицу методом Гаусса"""
    matrix = matrix.copy()
    # Добавляем столбец свободных членов
    matrix.append_column(free_column)
    # Преобразуем матрицу в треугольную с нулями под главной диагональю и единицами в главной диагонали
    matrix = matrix.triangulate_to_ones()
    if print_middle_values:
        print('\nРасширенная матрица, приведенная к треугольному виду')
        matrix.console_display()
    # Удаляем столбец свободных членов - он и будет решением (в процессе триангуляции он тоже менялся)
    return matrix.pop_column(matrix.columns - 1)
