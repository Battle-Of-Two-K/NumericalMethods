import pytest
import python_code.main as main


def test_gauss_metoda():
    """Тест из методички"""
    m = main.Matrix([[2, 5, 1], [-1, 2, -2], [6, 2, 1]])
    free = [1, 2, 3]
    assert main.solve_gauss(m, free) == [0.5, 0.5555555555555556, -1.1403508771929827]
