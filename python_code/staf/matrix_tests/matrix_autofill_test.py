import pytest
import python_code.main as main


def test_ones_mode():
    m = main.Matrix(3)
    m.autofill('diagonal_ones')
    assert main.det(m) == 1


def test_sequence_mode():
    m = main.Matrix(3)
    m.autofill('sequence')
    assert main.det(m) == 0
    m = main.Matrix(2)
    m.autofill('sequence')
    assert main.det(m) == -2


def test_dominant_mode():
    m = main.Matrix(3)
    m.autofill('dominant', options=(-10., 10))
    assert m.is_dominant
    m = main.Matrix(5)
    m.autofill('dominant')
    assert m.is_dominant


def test_triple_diagonal():
    m = main.Matrix(10)
    m.autofill('triple_diagonal')
    assert m.is_triple_diagonal