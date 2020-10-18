import pytest
from python_code import *


def test_method_data():
    matrix = Матрица([[-12, 4, 8], [4, 11, -6], [8, -6, 2]])
    decision = methods.matrix.power_method(matrix)
    solution = None
    for step in decision:
        solution = step.get("Решение")
    true_solution = -17
    assert true_solution == round(solution)


def test_mathprofi_data():
    matrix = Матрица([[-1, -6], [2, 6]])
    decision = methods.matrix.power_method(matrix)
    solution = None
    for step in decision:
        solution = step.get("Решение")
    true_solution = 3
    assert true_solution == round(solution)
