import pytest
import python_code.main as main


# ============================ Метод миноров ============================


def test_ones_minor_method():
    m = main.Matrix(3)
    m.autofill('diagonal_ones')
    assert main.determinant.minor_method(m) == 1


def test_sequence_minor_method():
    m = main.Matrix(3)
    m.autofill('sequence')
    assert main.determinant.minor_method(m) == 0


def test_four_minor_method():
    m = main.Matrix([[5, -3, 1, 0], [1, 4, 5, 0], [0, 0, 4, 10], [-5, 3, 5, -5]])
    assert main.determinant.minor_method(m) == -1840


def test_reverse_matrix_minor_method():
    m = main.Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(main.determinant.minor_method((~m) * m)) == 1


def test_reverse_matrix_minor_method2():
    m = main.Matrix(3)
    m.autofill()
    assert round(main.determinant.minor_method((~m) * m)) == 1


# ============================ Метод быстрых миноров ============================


def test_ones_fast_minor_method():
    m = main.Matrix(3)
    m.autofill('diagonal_ones')
    assert main.determinant.fast_minor_method(m) == 1


def test_sequence_fast_minor_method():
    m = main.Matrix(3)
    m.autofill('sequence')
    assert main.determinant.fast_minor_method(m) == 0


def test_four_fast_minor_method():
    m = main.Matrix([[5, -3, 1, 0], [1, 4, 5, 0], [0, 0, 4, 10], [-5, 3, 5, -5]])
    assert round(main.determinant.fast_minor_method(m)) == -1840


def test_reverse_matrix_fast_minor_method():
    m = main.Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(main.determinant.fast_minor_method((~m) * m)) == 1


def test_reverse_matrix_fast_minor_method2():
    m = main.Matrix(3)
    m.autofill()
    assert round(main.determinant.fast_minor_method((~m) * m)) == 1


# ============================ Метод диагоналей ============================


def test_ones_fast_diagonal_method():
    m = main.Matrix(3)
    m.autofill('diagonal_ones')
    assert main.determinant.diagonal_method(m) == 1


def test_sequence_diagonal_method():
    m = main.Matrix(3)
    m.autofill('sequence')
    assert main.determinant.diagonal_method(m) == 0


def test_reverse_matrix_diagonal_method():
    m = main.Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(main.determinant.diagonal_method((~m) * m)) == 1


def test_reverse_matrix_diagonal_method2():
    m = main.Matrix(3)
    m.autofill()
    assert round(main.determinant.diagonal_method((~m) * m)) == 1


# ============================ Общие тесты ============================


def test_ones_union():
    m = main.Matrix(3)
    m.autofill('diagonal_ones')
    assert main.determinant.diagonal_method(m) == main.determinant.minor_method(m) == \
           main.determinant.fast_minor_method(m)


def test_sequence_union():
    m = main.Matrix(3)
    m.autofill('sequence')
    assert main.determinant.diagonal_method(m) == main.determinant.minor_method(m) == \
           main.determinant.fast_minor_method(m)


def test_four_union():
    m = main.Matrix([[5, -3, 1, 0], [1, 4, 5, 0], [0, 0, 4, 10], [-5, 3, 5, -5]])
    assert main.determinant.minor_method(m) == round(main.determinant.fast_minor_method(m))


def test_reverse_union():
    m = main.Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    m = (~m) * m
    assert main.determinant.diagonal_method(m) == main.determinant.minor_method(m) == \
           main.determinant.fast_minor_method(m)


def test_reverse_union_2():
    m = main.Matrix(3)
    m.autofill()
    assert main.determinant.diagonal_method(m) == main.determinant.minor_method(m) == \
           round(main.determinant.fast_minor_method(m))


def test_five_union():
    m = main.Matrix(5)
    m.autofill()
    assert main.determinant.minor_method(m) == round(main.determinant.fast_minor_method(m))
