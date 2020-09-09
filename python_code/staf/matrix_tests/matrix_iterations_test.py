import pytest
import python_code.main as main


def test_norma_1():
    m = main.Matrix([[0, -1 / 5, 2 / 5], [1 / 5, 0, -1 / 3], [1 / 3, 1 / 6, 0]])
    assert round(m.norma_1, 8) == 0.6


def test_norma_2():
    m = main.Matrix([[0, -1 / 5, 2 / 5], [1 / 5, 0, -1 / 3], [1 / 3, 1 / 6, 0]])
    assert round(m.norma_2, 8) == 0.73333333


def test_simple_iterations():
    """По примеру из методички"""
    m = main.Matrix([[20, 4, -8], [-3, 15, 5], [6, 3, -18]])
    free = [1, -2, 3]
    assert main.iterations.simple_iterations(m, free, stop_level=8) == [-0.007760768395061721, -0.07433375684194482, -0.1816226104557232]


def test_zeidel_method():
    """По примеру из методички"""
    m = main.Matrix([[20, 4, -8], [-3, 15, 5], [6, 3, -18]])
    free = [1, -2, 3]
    assert main.iterations.zeidel_method(m, free, stop_level=6) == \
           [-0.0077777779120662555, -0.07434465044708496, -0.18165003437853625]


def test_triple_diagonal():
    m = main.Matrix([[-34, -26, 0, 0, 0],
                     [64, -124, -56, 0, 0],
                     [0, 94, -274, -86, 0],
                     [0, 0, 124, -484, -116],
                     [0, 0, 0, 154, -754]
                     ])
    free = [34, 38, 42, 46, 50]
    solution = [-.6181818, -.4993007, -.2794706, -.1437131, -.0956655]
    test_solution = list(map(lambda x: round(x, 7), main.iterations.triple_diagonal(m, free)))
    assert solution == test_solution
