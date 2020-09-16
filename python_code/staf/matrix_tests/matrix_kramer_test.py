import pytest
from python_code import *


def test_kramer_2():
    matrix = Matrix([[5, 2], [2, 1]])
    free = [7, 9]
    decision = methods.matrix.kramer_method(matrix, free)
    solution = None
    for step in decision:
        solution = step.get("Решение")
    assert [-11, 31] == list(map(lambda x: round(x), solution))


def test_kramer_3():
    matrix = Matrix([[2, 1, 1], [1, -1, 0], [3, -1, 2]])
    free = [2, -2, 2]
    decision = methods.matrix.kramer_method(matrix, free)
    solution = None
    for step in decision:
        print(step)
        solution = step.get("Решение")
    assert [-1, 1, 3] == list(map(lambda x: round(x), solution))
