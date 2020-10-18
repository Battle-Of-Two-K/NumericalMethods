import pytest
import random
from random import *

from python_code.main import *


def test_square_matrix_creation():
    m = Матрица(1)
    assert m.квадратная_ли
    assert m.матрица == [[0]]
    m = Матрица(2)
    assert m.квадратная_ли
    assert m.матрица == [[0, 0], [0, 0]]
    m = Матрица(3)
    assert m.квадратная_ли
    assert m.матрица == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_matrix_creation():
    cols = randint(2, 10)
    rows = randint(2, 10)
    m = Матрица(rows, cols)
    assert m.количество_строк == rows
    assert m.количество_столбцов == cols


def test_matrix_adaptation():
    rows = randint(2, 10)
    cols = randint(2, 10)
    test_list = [[randint(-10, 10) for _ in range(cols)] for __ in range(rows)]
    m = Матрица(test_list.copy())
    assert m.количество_строк == rows
    assert m.количество_столбцов == cols
    assert m.матрица == test_list


def test_ones_mode():
    m = Матрица(3)
    m.заполнить_до_единичной()
    assert определитель(m) == 1


def test_sequence_mode():
    m = Матрица(3)
    m.заполнить_последовательностью()
    assert определитель(m) == 0
    m = Матрица(2)
    m.заполнить_последовательностью()
    assert определитель(m) == -2


def test_dominant_mode():
    m = Матрица(3)
    m.заполнить_до_доминантной(-10., 10)
    assert m.преобладающая_ли_диагональ
    m = Матрица(5)
    m.заполнить_до_доминантной()
    assert m.преобладающая_ли_диагональ


def test_triple_diagonal():
    m = Матрица(10)
    m.заполнить_до_трехдиагональной()
    assert m.трехдиагональная_ли


def test_minor():
    m = Матрица(3)
    m.заполнить_последовательностью()
    assert m.удалить_строку_столбец(1, 1).матрица == [[1, 3], [7, 9]]
    assert m.удалить_строку_столбец(0, 0).матрица == [[5, 6], [8, 9]]
    assert m.удалить_строку_столбец(2, 2).матрица == [[1, 2], [4, 5]]


def test_mul():
    m1 = Матрица([[0, 4, 7], [-3, 8, 1], [3, 8, -4]])
    m2 = Матрица([[-8, 4, -10], [10, 3, 2], [9, 10, 5]])
    assert (m1 * m2).матрица == [[103, 82, 43], [113, 22, 51], [20, -4, -34]]
    assert (m2 * m1).матрица == [[-42, -80, -12], [-3, 80, 65], [-15, 156, 53]]


def test_reverse_matrix():
    """Этот тест проверяет и транспонирование, и алгебраические дополнения разом"""
    m = Матрица(3)
    m.заполнить_случайными()
    assert round(определитель((~m) * m)) == 1


def test_reverse_matrix2():
    m = Матрица([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(определитель((~m) * m)) == 1


def test_pop_row():
    size = randint(2, 10)
    m = Матрица(size)
    what_pop = randint(0, size - 1)
    line = m.матрица[what_pop]
    assert m.удалить_строку(what_pop) == line


def test_pop_column():
    m = Матрица(4)
    m.заполнить_последовательностью()
    assert m.удалить_столбец(0) == [1, 5, 9, 13]


def test_transpon():
    m = Матрица(5)
    m.заполнить_случайными()
    assert m.матрица == m.транспонированная.транспонированная.матрица


def test_is_triple_diagonal():
    m = Матрица(10)
    m.заполнить_до_трехдиагональной()
    assert m.трехдиагональная_ли


def test_col_insertion():
    m = Матрица([[1, 3], [4, 6]])
    col_to_insert = [2, 5]
    correct_result = [[1, 2, 3], [4, 5, 6]]
    m.вставить_столбец(1, col_to_insert)
    assert correct_result == m.матрица


def test_row_insertion():
    m = Матрица([[1, 2], [5, 6]])
    row_to_insert = [3, 4]
    correct_result = [[1, 2], [3, 4], [5, 6]]
    m.вставить_строку(1, row_to_insert)
    assert correct_result == m.матрица


def test_vector_norm_1():
    m = Матрица([[1, 2, -3]])
    assert 3 == m.векторная_норма_1


def test_vector_norm_2():
    m = Матрица([[1, 2, -3]])
    assert 6 == m.векторная_норма_2


def test_vector_norm_3():
    m = Матрица([[1, 2, -3]])
    assert 14 ** .5 == m.векторная_норма_3


def test_matrix_norm_3():
    m = Матрица([[1, -3, 5], [-7, 4, -4], [3, -6, 1]])
    assert 162 ** .5 == m.матричная_норма_3


# ============================ Метод миноров ============================


def test_ones_minor_method():
    m = Матрица(3)
    m.заполнить_до_единичной()
    assert determinant.minor_method(m) == 1


def test_sequence_minor_method():
    m = Матрица(3)
    m.заполнить_последовательностью()
    assert determinant.minor_method(m) == 0


def test_four_minor_method():
    m = Матрица([[5, -3, 1, 0], [1, 4, 5, 0], [0, 0, 4, 10], [-5, 3, 5, -5]])
    assert determinant.minor_method(m) == -1840


def test_reverse_matrix_minor_method():
    m = Матрица([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(determinant.minor_method((~m) * m)) == 1


def test_reverse_matrix_minor_method2():
    m = Матрица(3)
    m.заполнить_случайными()
    assert round(determinant.minor_method((~m) * m)) == 1


# ============================ Метод быстрых миноров ============================


def test_ones_fast_minor_method():
    m = Матрица(3)
    m.заполнить_до_единичной()
    assert determinant.fast_minor_method(m) == 1


def test_sequence_fast_minor_method():
    m = Матрица(3)
    m.заполнить_последовательностью()
    assert determinant.fast_minor_method(m) == 0


def test_four_fast_minor_method():
    m = Матрица([[5, -3, 1, 0], [1, 4, 5, 0], [0, 0, 4, 10], [-5, 3, 5, -5]])
    assert round(determinant.fast_minor_method(m)) == -1840


def test_reverse_matrix_fast_minor_method():
    m = Матрица([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(determinant.fast_minor_method((~m) * m)) == 1


def test_reverse_matrix_fast_minor_method2():
    m = Матрица(3)
    m.заполнить_случайными()
    assert round(determinant.fast_minor_method((~m) * m)) == 1


# ============================ Метод диагоналей ============================


def test_ones_fast_diagonal_method():
    m = Матрица(3)
    m.заполнить_до_единичной()
    assert determinant.diagonal_method(m) == 1


def test_sequence_diagonal_method():
    m = Матрица(3)
    m.заполнить_последовательностью()
    assert determinant.diagonal_method(m) == 0


def test_reverse_matrix_diagonal_method():
    m = Матрица([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(determinant.diagonal_method((~m) * m)) == 1


def test_reverse_matrix_diagonal_method2():
    m = Матрица(3)
    m.заполнить_случайными()
    assert round(determinant.diagonal_method((~m) * m)) == 1


# ============================ Общие тесты ============================


def test_ones_union():
    m = Матрица(3)
    m.заполнить_до_единичной()
    assert determinant.diagonal_method(m) == determinant.minor_method(m) == \
           determinant.fast_minor_method(m)


def test_sequence_union():
    m = Матрица(3)
    m.заполнить_последовательностью()
    assert determinant.diagonal_method(m) == determinant.minor_method(m) == \
           determinant.fast_minor_method(m)


def test_four_union():
    m = Матрица([[5, -3, 1, 0], [1, 4, 5, 0], [0, 0, 4, 10], [-5, 3, 5, -5]])
    assert determinant.minor_method(m) == round(determinant.fast_minor_method(m))


def test_reverse_union():
    m = Матрица([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    m = (~m) * m
    assert determinant.diagonal_method(m) == determinant.minor_method(m) == \
           determinant.fast_minor_method(m)


def test_reverse_union_2():
    m = Матрица(3)
    m.заполнить_случайными()
    assert determinant.diagonal_method(m) == determinant.minor_method(m) == \
           round(determinant.fast_minor_method(m))


def test_five_union():
    m = Матрица(5)
    m.заполнить_случайными()
    assert determinant.minor_method(m) == round(determinant.fast_minor_method(m))
