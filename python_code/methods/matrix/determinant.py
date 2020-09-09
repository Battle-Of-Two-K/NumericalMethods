def minor_method(matrix):
    """Нахождение определителя по методу миноров (с рекурсией)"""
    if not matrix.is_square:
        raise ArithmeticError("Определитель возможно найти только у квадратной матрицы")
    matrix = matrix.copy()
    # Точки остановки (в них работает диагональный метод)
    if matrix.rows <= 3:
        return diagonal_method(matrix)
    # Иначе - рекурсия
    else:
        # Но сначала, небольшой бонус от simens_green - ищем строку с наибольшим количеством нулей
        max_zeros_row_no = matrix.search_for_max_num_count(0)
        if matrix[max_zeros_row_no].count(0) == matrix.columns:
            return 0
        det_value = 0
        for _ in range(matrix.columns):
            # Если значение в ячейке = 0, то пропускаем шаг (избежали потенциальную кучу дополнительных определителей)
            if matrix[max_zeros_row_no][_] != 0:
                # Иначе вычисляем через миноры и рекурсию
                if bool((max_zeros_row_no + _ + 1) % 2):
                    det_value += matrix[max_zeros_row_no][_] * minor_method(matrix.minor(max_zeros_row_no, _))
                else:
                    det_value -= matrix[max_zeros_row_no][_] * minor_method(matrix.minor(max_zeros_row_no, _))
        return det_value


def fast_minor_method(matrix):
    """Тот же метод миноров, но с предварительной триангуляцией (сокращение до 50% работы метода миноров)
    (метод Гаусса) ТОЧНОСТЬ НИЖЕ, ЧЕМ У МЕТОДА МИНОРОВ"""
    # TODO: метод через миноры и триангуляцию
    matrix = matrix.triangulate()
    return minor_method(matrix)


def diagonal_method(matrix):
    """Метод, использующий правило диагоналей, не использует рекурсию"""
    if not matrix.is_square:
        raise ArithmeticError("Определитель возможно найти только у квадратной матрицы")
    matrix = matrix.copy()
    if matrix.rows == 1:
        return matrix[0][0]
    elif matrix.rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    elif matrix.rows == 3:
        return matrix[0][0] * matrix[1][1] * matrix[2][2] + \
               matrix[1][0] * matrix[2][1] * matrix[0][2] + \
               matrix[0][1] * matrix[1][2] * matrix[2][0] - \
               matrix[2][0] * matrix[1][1] * matrix[0][2] - \
               matrix[0][1] * matrix[1][0] * matrix[2][2] - \
               matrix[2][1] * matrix[1][2] * matrix[0][0]
    else:
        raise ArithmeticError("Этот метод не рассчитанна такое")


def auto_det(matrix):
    """Автоматический выбор лучшего алгоритма"""
    if not matrix.is_square:
        raise ArithmeticError("Определитель возможно найти только у квадратной матрицы")
    if matrix.rows > 9:
        return fast_minor_method(matrix)
    else:
        return minor_method(matrix)
