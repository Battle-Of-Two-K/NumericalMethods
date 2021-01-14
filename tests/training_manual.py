import pytest

import NumericalMethods.first_problem_iteration as first_problem_iteration
import NumericalMethods.second_problem as second_problem
from NumericalMethods import Matrix
from NumericalMethods.first_problem_direct import gauss, triple
from NumericalMethods.util import get_solution


def list_round(list_, accuracy=8):
    return list(map(lambda value: round(value, accuracy), list_))


# =======================================================
# Первая проблема линейной алгебры. Прямые методы решения
# =======================================================


@pytest.mark.skip
def test_gauss():
    matrix = Matrix([
        [2, 5, 1],
        [-1, 2, -2],
        [6, 2, 1]
    ])
    free = [1, 2, 3]
    true_solution = [12 / 9, 10 / 57, -65 / 57]

    solution = get_solution(gauss(matrix, free))

    assert list_round(solution) == list_round(true_solution)


def test_reverse_matrix():
    matrix = Matrix([
        [2, 3, 6],
        [3, 6, 2],
        [6, 2, 8],
    ])
    true_solution = Matrix([
        [-11 / 32, 3 / 32, 15 / 64],
        [3 / 32, 5 / 32, -7 / 64],
        [15 / 64, -7 / 64, -3 / 128]
    ])

    solution = matrix ** -1

    assert solution.map(round, 8) == true_solution.map(round, 8)


def test_triple_solve():
    matrix = Matrix([
        [-34, -26, 0, 0, 0],
        [64, -124, -56, 0, 0],
        [0, 94, -274, -86, 0],
        [0, 0, 124, -484, -116],
        [0, 0, 0, 154, -754]
    ])
    free = [34, 38, 42, 46, 50]
    true_solution = [-.6181818, -.4993007, -.2794706, -.1437131, -.0956655]

    solution = get_solution(triple(matrix, free))

    assert list_round(solution, 7) == list_round(true_solution, 7)


# ==================================================================
# Первая проблема линейной алгебры. Итерационные методы решения СЛАУ
# ==================================================================

def test_first_problem_iteration_simple():
    matrix = Matrix([
        [20, 4, -8],
        [-3, 15, 5],
        [6, 3, -18],
    ])
    free = [1, -2, 3]
    true_solution = [-.0077608, -.0743338, -.1816226]

    solution = get_solution(first_problem_iteration.simple(matrix, free, iterations=7))

    assert list_round(solution, 7) == list_round(true_solution, 7)


def test_first_problem_iteration_zeidel():
    matrix = Matrix([
        [20, 4, -8],
        [-3, 15, 5],
        [6, 3, -18],
    ])
    free = [1, -2, 3]
    true_solution = [-.0077778, -.0743447, -.18165]

    solution = get_solution(first_problem_iteration.zeidel(matrix, free, iterations=5))

    assert list_round(solution, 7) == list_round(true_solution, 7)


def test_second_problem_power_method():
    matrix = Matrix([
        [-12, 4, 8],
        [4, 11, -6],
        [8, -6, 2],
    ])
    true_solution = -17

    solution = get_solution(second_problem.power_method(matrix))

    assert round(solution) == true_solution


def test_second_problem_yakobi_rotation():
    matrix = Matrix([
        [17, 1, 1],
        [1, 17, 2],
        [1, 2, 4],
    ])
    true_solution = [16.0349, 18.31907, 3.646025]

    solution = get_solution(second_problem.yakobi_rotation(matrix))['Собственные числа']

    assert list_round(solution, 4) == list_round(true_solution, 4)
