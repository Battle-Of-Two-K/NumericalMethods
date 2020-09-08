import pytest
import python_code.main as main


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
    m.console_display()
    # -1 Иногда выскакивает из-за "-0.0" - очень маленькое значение, но дает знак, см пример ниже
    assert round(main.det((~m) * m)) == 1


@pytest.mark.xfail(reason='(~m) * m)[2][0] равно "-0.0" или -2.7755575615628914e-17, достаточно, чтоб дать "-"')
def test_reverse_matrix2():
    m = main.Matrix([[2, -2, -7], [-4, 8, -8], [10, -7, 0]])
    assert round(main.det((~m) * m)) == 1
