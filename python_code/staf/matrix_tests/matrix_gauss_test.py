import pytest
import python_code.main as main


def test_gauss_metoda():
    """Тест из методички"""
    m = main.Matrix([[2, 5, 1], [-1, 2, -2], [6, 2, 1]])
    free = [1, 2, 3]
    assert main.gauss.gauss_method(m, free) == [0.6315789473684212, 0.17543859649122806, -1.1403508771929827]
