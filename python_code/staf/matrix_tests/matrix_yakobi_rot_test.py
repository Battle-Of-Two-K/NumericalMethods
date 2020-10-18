import pytest
from python_code import *


def test_yakobi_rot_1():
    matrix = Матрица([[17, 1, 1], [1, 17, 2], [1, 2, 4]])
    decision = method_rot_yakobi(matrix, iterations=8)
    solution = None
    for step in decision:
        solution = step.get("Решение")
    assert [16.03490, 18.31907, 3.64603] == list(map(lambda x: round(x, 5), solution['Собственные числа']))
