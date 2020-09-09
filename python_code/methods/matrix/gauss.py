def gauss_method(matrix, free_column):
    """Решает матрицу методом Гаусса"""
    matrix = matrix.copy()
    # Добавляем столбец свободных членов
    matrix.append_column(free_column)
    # Преобразуем матрицу в треугольную с нулями под главной диагональю и единицами в главной диагонали
    matrix = matrix.triangulate_to_ones()
    # Удаляем столбец свободных членов - он и будет решением (в процессе триангуляции он тоже менялся)
    return matrix.pop_column(matrix.columns - 1)
