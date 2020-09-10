import pytest
import python_code.main as main


def test_gauss_metod_1():
    """Тест из методички"""
    m = main.Matrix([[2, 5, 1], [-1, 2, -2], [6, 2, 1]])
    free = [1, 2, 3]
    assert main.gauss.gauss_method(m, free) == [0.6315789473684212, 0.17543859649122806, -1.1403508771929827]


def test_gauss_metod_2():
    matrix = main.Matrix([
                          [3, -1, -7, -8],
                          [3, -10, 2, 3],
                          [11, 7, 11, -3],
                          [-7, -8, 10, 3]
                         ])
    free_column = [-30, 56, -54, 142]
    assert list(map(lambda x: round(x, 8), main.gauss.gauss_method(matrix, free_column))) == [-6, -7, 5, -2]
