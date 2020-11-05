import pytest
from Battle_Of_Two_K.MNK import amount_elem, sum_x, square_sum_x, cubic_sum_x, fourth_degree_sum_x, sum_y, sum_x_y, \
    square_x_sum_y

X = [-6, -5, -4, -2]
Y = [30, 22, 16, 6]


def test_MNK():
    a = amount_elem()
    b = sum_x()
    c = square_sum_x()
    d = cubic_sum_x()
    e = fourth_degree_sum_x()
    f = sum_y()
    g = sum_x_y()
    h = square_x_sum_y()
    assert a == 4
    assert b == -17
    assert c == 81
    assert d == -413
    assert e == 2193
    assert f == 74
    assert g == -366
    assert h == 1910


test_MNK()
