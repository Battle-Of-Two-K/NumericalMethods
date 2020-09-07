def minor_method(matrix):
    """Нахождение определителя по методу миноров (с рекурсией)"""
    assert matrix.is_square, "Определитель возможно найти только у квадратной матрицы"
    # Точки остановки (матрица 1х1 или 2х2)
    if matrix.rows == 1:
        return matrix[0][0]
    elif matrix.rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
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
                if bool((_ + 1) % 2):
                    det_value += matrix[max_zeros_row_no][_] * minor_method(matrix.minor(max_zeros_row_no, _))
                else:
                    det_value -= matrix[max_zeros_row_no][_] * minor_method(matrix.minor(max_zeros_row_no, _))
        return det_value


def fast_minor_method():
    """Тот же метод миноров, но с предварительной триангуляцией (сокращение до 50% работы метода миноров)"""
    # TODO: метод через миноры и триангуляцию
    pass


def diagonal_method():
    """Метод, использующий правило диагоналей, не использует рекурсию"""
    # TODO: Метод диагоналей
    pass
