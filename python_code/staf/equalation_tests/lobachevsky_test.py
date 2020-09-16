import pytest
from python_code import *


def test_quad_pol():
    polynom = [1, -5, 6]
    correct_roots = [3, 2]
    decision = methods.equation.polynomial.lobachevsky_method(polynom)
    solution = []
    for step in decision:
        solution = step.get('Решение')
    assert correct_roots == solution
