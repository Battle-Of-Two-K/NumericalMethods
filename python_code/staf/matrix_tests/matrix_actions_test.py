import pytest
import python_code.main as main
import random


def test_minor():
    m = main.Matrix(3)
    m.autofill('sequence')
    assert m.minor(1, 1).matrix == [[1, 3], [7, 9]]
    assert m.minor(0, 0).matrix == [[5, 6], [8, 9]]
    assert m.minor(2, 2).matrix == [[1, 2], [4, 5]]


def test_mul():
    m1 = main.Matrix([[0, 4, 7], [-3, 8, 1], [3, 8, -4]])
    m2 = main.Matrix([[-8, 4, -10], [10, 3, 2], [9, 10, 5]])
    assert (m1 * m2).matrix == [[103, 82, 43], [113, 22, 51], [20, -4, -34]]
    assert (m2 * m1).matrix == [[-42, -80, -12], [-3, 80, 65], [-15, 156, 53]]


def test_reverse_matrix():
    """Этот тест проверяет и транспонирование, и алгебраические дополнения разом"""
    m = main.Matrix(3)
    m.autofill()
    assert round(main.det((~m) * m)) == 1


def test_reverse_matrix2():
    m = main.Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(main.det((~m) * m)) == 1


def test_pop_row():
    size = random.randint(2, 10)
    m = main.Matrix(size)
    what_pop = random.randint(0, size - 1)
    line = m.matrix[what_pop]
    assert m.pop_row(what_pop) == line


def test_pop_column():
    m = main.Matrix(4)
    m.autofill('sequence')
    assert m.pop_column(0) == [1, 5, 9, 13]


def test_transpon():
    m = main.Matrix(5)
    m.autofill()
    assert m.matrix == m.T.T.matrix


def test_is_triple_diagonal():
    m = main.Matrix(10)
    m.autofill('triple_diagonal')
    assert m.is_triple_diagonal


def test_col_insertion():
    m = main.Matrix([[1, 3], [4, 6]])
    col_to_insert = [2, 5]
    correct_result = [[1, 2, 3], [4, 5, 6]]
    m.insert_column(1, col_to_insert)
    assert correct_result == m.matrix


def test_row_insertion():
    m = main.Matrix([[1, 2], [5, 6]])
    row_to_insert = [3, 4]
    correct_result = [[1, 2], [3, 4], [5, 6]]
    m.insert_row(1, row_to_insert)
    assert correct_result == m.matrix


def test_vector_norm_1():
    m = main.Matrix([[1, 2, -3]])
    assert 3 == m.vector_norma_1


def test_vector_norm_2():
    m = main.Matrix([[1, 2, -3]])
    assert 6 == m.vector_norma_2


def test_vector_norm_3():
    m = main.Matrix([[1, 2, -3]])
    assert 14 ** .5 == m.vector_norma_3


def test_matrix_norm_3():
    m = main.Matrix([[1, -3, 5], [-7, 4, -4], [3, -6, 1]])
    assert 162 ** .5 == m.norma_3

