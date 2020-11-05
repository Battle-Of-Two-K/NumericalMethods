import numpy as np
from sympy.abc import x

# /////////////////////////////////////////////
# Аппроксимация  методом  наименьших  квадратов
# /////////////////////////////////////////////

# Мой вариант
X = [-6, -5, -4, -2]
Y = [36, 27, 19, 7, 6]

# Вариант из методички
# X = [-2, -1, 0, 1, 2]
# Y = [3, 4, 2, 1, 1]

# Вариант 11 (Сергей)
# X = [-6, -5, -4, -2]
# Y = [30, 22, 16, 6]

# /////////////////////////////////////////////
# Ниже програмный код!
# /////////////////////////////////////////////


def amount_elem():
    if len(X) != len(Y):
        print('Error: the lengths of the lists must be equal!')
        print('Ошибка: длины списков должны быть равны!')
    else:
        print(f'Количество элементов (последняя итерация суммы): {len(X)}')

    return len(X)


def sum_x():
    result = 0
    for value in X:
        result += value
    return float(result)


def square_sum_x():
    result = 0
    for value in X:
        result += value ** 2
    return float(result)


def cubic_sum_x():
    result = 0
    for value in X:
        result += value ** 3
    return float(result)


def fourth_degree_sum_x():
    result = 0
    for value in X:
        result += value ** 4
    return float(result)


def sum_y():
    result = 0
    for value in Y:
        result += value
    return float(result)


def sum_x_y():
    result = 0
    for value_x, value_y in zip(X, Y):
        result += value_x * value_y
    return float(result)


def square_x_sum_y():
    result = 0
    for value_x, value_y in zip(X, Y):
        result += value_x ** 2 * value_y
    return float(result)


print(f'n = {amount_elem()}')
print(f' {sum_x()}')
print(square_sum_x())
print(cubic_sum_x())
print(fourth_degree_sum_x())
print(sum_y())
print(sum_x_y())
print(square_x_sum_y())

matrix = np.array([[fourth_degree_sum_x(), cubic_sum_x(), square_sum_x()],
                   [cubic_sum_x(), square_sum_x(), sum_x()],
                   [square_sum_x(), sum_x(), len(X)]])  # Матрица (левая часть системы)

print('Матрица:')
print(matrix)

vector = np.array([square_x_sum_y(), sum_x_y(), sum_y()])  # Вектор (правая часть системы)

res = np.linalg.solve(matrix, vector)
print(res)

p = res[0] * x ** 2 + res[1] * x + res[2]
print(f'P(x) = {res[0]}x^2 + {res[1]}x + {res[2]}')


def squared_residual():
    result = 0
    for value_x, value_y in zip(X, Y):
        result += (p.evalf(subs={x: value_x}) - value_y) ** 2
    return result


print(squared_residual())
