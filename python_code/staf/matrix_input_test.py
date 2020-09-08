import pytest
import python_code.main as main
from random import randint


def test_square_matrix_creation():
    m = main.Matrix(1)
    assert m.is_square
    assert m.matrix == [[0]]
    m = main.Matrix(2)
    assert m.is_square
    assert m.matrix == [[0, 0], [0, 0]]
    m = main.Matrix(3)
    assert m.is_square
    assert m.matrix == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_matrix_creation():
    cols = randint(2, 10)
    rows = randint(2, 10)
    m = main.Matrix(rows, cols)
    assert m.rows == rows
    assert m.columns == cols


def test_matrix_adaptation():
    rows = randint(2, 10)
    cols = randint(2, 10)
    test_list = [[randint(-10, 10) for _ in range(cols)] for __ in range(rows)]
    m = main.Matrix(test_list.copy())
    assert m.rows == rows
    assert m.columns == cols
    assert m.matrix == test_list
