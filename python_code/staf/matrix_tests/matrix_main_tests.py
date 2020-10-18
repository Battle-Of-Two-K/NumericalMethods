import pytest
import random
from random import *

from python_code.main import *


def test_square_matrix_creation():
    m = Matrix(1)
    assert m.is_square
    assert m.matrix == [[0]]
    m = Matrix(2)
    assert m.is_square
    assert m.matrix == [[0, 0], [0, 0]]
    m = Matrix(3)
    assert m.is_square
    assert m.matrix == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_matrix_creation():
    cols = randint(2, 10)
    rows = randint(2, 10)
    m = Matrix(rows, cols)
    assert m.rows == rows
    assert m.columns == cols


def test_matrix_adaptation():
    rows = randint(2, 10)
    cols = randint(2, 10)
    test_list = [[randint(-10, 10) for _ in range(cols)] for __ in range(rows)]
    m = Matrix(test_list.copy())
    assert m.rows == rows
    assert m.columns == cols
    assert m.matrix == test_list


def test_ones_mode():
    m = Matrix(3)
    m.fill_diagonal_ones()
    assert det(m) == 1


def test_sequence_mode():
    m = Matrix(3)
    m.fill_sequence()
    assert det(m) == 0
    m = Matrix(2)
    m.fill_sequence()
    assert det(m) == -2


def test_dominant_mode():
    m = Matrix(3)
    m.fill_dominant(-10., 10)
    assert m.is_dominant
    m = Matrix(5)
    m.fill_dominant()
    assert m.is_dominant


def test_triple_diagonal():
    m = Matrix(10)
    m.fill_triple_diagonal()
    assert m.is_triple_diagonal


def test_minor():
    m = Matrix(3)
    m.fill_sequence()
    assert m.minor(1, 1).matrix == [[1, 3], [7, 9]]
    assert m.minor(0, 0).matrix == [[5, 6], [8, 9]]
    assert m.minor(2, 2).matrix == [[1, 2], [4, 5]]


def test_mul():
    m1 = Matrix([[0, 4, 7], [-3, 8, 1], [3, 8, -4]])
    m2 = Matrix([[-8, 4, -10], [10, 3, 2], [9, 10, 5]])
    assert (m1 * m2).matrix == [[103, 82, 43], [113, 22, 51], [20, -4, -34]]
    assert (m2 * m1).matrix == [[-42, -80, -12], [-3, 80, 65], [-15, 156, 53]]


def test_reverse_matrix():
    """Этот тест проверяет и транспонирование, и алгебраические дополнения разом"""
    m = Matrix(3)
    m.fill_random()
    assert round(det(m ** (-1) * m)) == 1


def test_reverse_matrix2():
    m = Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(det(m ** (-1) * m)) == 1


def test_pop_row():
    size = randint(2, 10)
    m = Matrix(size)
    what_pop = randint(0, size - 1)
    line = m.matrix[what_pop]
    assert m.pop_row(what_pop) == line


def test_pop_column():
    m = Matrix(4)
    m.fill_sequence()
    assert m.pop_column(0) == [1, 5, 9, 13]


def test_transpon():
    m = Matrix(5)
    m.fill_random()
    assert m.matrix == m.T.T.matrix


def test_is_triple_diagonal():
    m = Matrix(10)
    m.fill_triple_diagonal()
    assert m.is_triple_diagonal


def test_col_insertion():
    m = Matrix([[1, 3], [4, 6]])
    col_to_insert = [2, 5]
    correct_result = [[1, 2, 3], [4, 5, 6]]
    m.insert_column(1, col_to_insert)
    assert correct_result == m.matrix


def test_row_insertion():
    m = Matrix([[1, 2], [5, 6]])
    row_to_insert = [3, 4]
    correct_result = [[1, 2], [3, 4], [5, 6]]
    m.insert_row(1, row_to_insert)
    assert correct_result == m.matrix


def test_vector_norm_1():
    m = Matrix([[1, 2, -3]])
    assert 3 == m.vector_norma_1


def test_vector_norm_2():
    m = Matrix([[1, 2, -3]])
    assert 6 == m.vector_norma_2


def test_vector_norm_3():
    m = Matrix([[1, 2, -3]])
    assert 14 ** .5 == m.vector_norma_3


def test_matrix_norm_3():
    m = Matrix([[1, -3, 5], [-7, 4, -4], [3, -6, 1]])
    assert 162 ** .5 == m.norma_3


# ============================ Метод миноров ============================


def test_ones_minor_method():
    m = Matrix(3)
    m.fill_diagonal_ones()
    assert determinant.minor_method(m) == 1


def test_sequence_minor_method():
    m = Matrix(3)
    m.fill_sequence()
    assert determinant.minor_method(m) == 0


def test_four_minor_method():
    m = Matrix([[5, -3, 1, 0], [1, 4, 5, 0], [0, 0, 4, 10], [-5, 3, 5, -5]])
    assert determinant.minor_method(m) == -1840


def test_reverse_matrix_minor_method():
    m = Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(determinant.minor_method(m ** (-1) * m)) == 1


def test_reverse_matrix_minor_method2():
    m = Matrix(3)
    m.fill_random()
    assert round(determinant.minor_method(m ** (-1) * m)) == 1


# ============================ Метод быстрых миноров ============================


def test_ones_fast_minor_method():
    m = Matrix(3)
    m.fill_diagonal_ones()
    assert determinant.fast_minor_method(m) == 1


def test_sequence_fast_minor_method():
    m = Matrix(3)
    m.fill_sequence()
    assert determinant.fast_minor_method(m) == 0


def test_four_fast_minor_method():
    m = Matrix([[5, -3, 1, 0], [1, 4, 5, 0], [0, 0, 4, 10], [-5, 3, 5, -5]])
    assert round(determinant.fast_minor_method(m)) == -1840


def test_reverse_matrix_fast_minor_method():
    m = Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(determinant.fast_minor_method(m ** (-1) * m)) == 1


def test_reverse_matrix_fast_minor_method2():
    m = Matrix(3)
    m.fill_random()
    assert round(determinant.fast_minor_method(m ** (-1) * m)) == 1


# ============================ Метод диагоналей ============================


def test_ones_fast_diagonal_method():
    m = Matrix(3)
    m.fill_diagonal_ones()
    assert determinant.diagonal_method(m) == 1


def test_sequence_diagonal_method():
    m = Matrix(3)
    m.fill_sequence()
    assert determinant.diagonal_method(m) == 0


def test_reverse_matrix_diagonal_method():
    m = Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(determinant.diagonal_method(m ** (-1) * m)) == 1


def test_reverse_matrix_diagonal_method2():
    m = Matrix(3)
    m.fill_random()
    assert round(determinant.diagonal_method(m ** (-1) * m)) == 1


# ============================ Общие тесты ============================


def test_ones_union():
    m = Matrix(3)
    m.fill_diagonal_ones()
    assert determinant.diagonal_method(m) == determinant.minor_method(m) == \
           determinant.fast_minor_method(m)


def test_sequence_union():
    m = Matrix(3)
    m.fill_sequence()
    assert determinant.diagonal_method(m) == determinant.minor_method(m) == \
           determinant.fast_minor_method(m)


def test_four_union():
    m = Matrix([[5, -3, 1, 0], [1, 4, 5, 0], [0, 0, 4, 10], [-5, 3, 5, -5]])
    assert determinant.minor_method(m) == round(determinant.fast_minor_method(m))


def test_reverse_union():
    m = Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    m = m ** (-1) * m
    assert determinant.diagonal_method(m) == determinant.minor_method(m) == \
           determinant.fast_minor_method(m)


def test_reverse_union_2():
    m = Matrix(3)
    m.fill_random()
    assert determinant.diagonal_method(m) == determinant.minor_method(m) == \
           round(determinant.fast_minor_method(m))


def test_five_union():
    m = Matrix(5)
    m.fill_random()
    assert determinant.minor_method(m) == round(determinant.fast_minor_method(m))
