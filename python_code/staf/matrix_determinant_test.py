import pytest
import python_code.main as main


def test_ones():
    m = main.Matrix(3)
    m.autofill('ones')
    assert main.det(m) == 1


def test_sequence():
    m = main.Matrix(3)
    m.autofill('sequence')
    assert main.det(m) == 0

@pytest.mark.xfail(reason='(~m) * m)[2][0] равно "-0.0" или -2.7755575615628914e-17, достаточно, чтоб дать "-"')
def test_reverse_matrix2():
    m = main.Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(main.det((~m) * m)) == 1
