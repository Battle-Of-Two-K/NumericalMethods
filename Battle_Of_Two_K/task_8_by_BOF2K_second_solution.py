import numpy as np
from sympy.abc import x
import matplotlib.pyplot as plt

# /////////////////////////////////////////////
# Аппроксимация  методом  наименьших  квадратов
# /////////////////////////////////////////////

# # Мой вариант
X = [-6, -5, -4, -2]
Y = [36, 27, 19, 7]

# Вариант из методички (рабортает, можно проверить)
# X = [-2, -1, 0, 1, 2]
# Y = [3, 4, 2, 1, 1]

# /////////////////////////////////////////////
# Ниже програмный код!
# /////////////////////////////////////////////


def amount_elem():
    if len(X) != len(Y):
        print('Error: the lengths of the lists must be equal!')
        print('Ошибка: длины списков должны быть равны!')
    else:
        print(f'n = {len(X)}')

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
        result += (value_x ** 2) * value_y
    return float(result)


def squared_residual():
    result = 0
    for value_x, value_y in zip(X, Y):
        result += (p.evalf(subs={x: value_x}) - value_y) ** 2
    return result


# \\\\\\\\\\\\\\\\\\\\\\\\
# Красивый вывод на экран
# \\\\\\\\\\\\\\\\\\\\\\\\

amount_elem()
print('Коэффициенты системы: ')
print(f'Сумма x............{sum_x()}')
print(f'Сумма x^2..........{square_sum_x()}')
print(f'Сумма x^3..........{cubic_sum_x()}')
print(f'Сумма x^4..........{fourth_degree_sum_x()}')
print(f'Сумма y............{sum_y()}')
print(f'Сумма x * y........{sum_x_y()}')
print(f'Сумма x^2 * y......{square_x_sum_y()}')

matrix = np.array([[fourth_degree_sum_x(), cubic_sum_x(), square_sum_x()],
                   [cubic_sum_x(), square_sum_x(), sum_x()],
                   [square_sum_x(), sum_x(), len(X)]])  # Матрица (левая часть системы)

print('-' * 40)
print('\nМатрица:')
print(matrix)

vector = np.array([square_x_sum_y(), sum_x_y(), sum_y()])  # Вектор (правая часть системы)
print(f'\nСтолбец свободных членов: {vector}')
print('-' * 40)

res = np.linalg.solve(matrix, vector)

print(f'\na = {res[0]}')
print(f'b = {res[1]}')
print(f'c = {res[2]}\n')

p = res[0] * x ** 2 + res[1] * x + res[2]
print('Многочлен:')
print(f'P(x) = {res[0]}x^2 + {res[1]}x + {res[2]}\n')

print('/' * 41)
print(f'Квадратичная невязка: {squared_residual()}')
print('/' * 41)

# \\\\\\\\\\\\\\\\\\\\\\\
# Красивый вывод графика:
# \\\\\\\\\\\\\\\\\\\\\\\

x = np.linspace(-15, 15, 100)
y = res[0] * x ** 2 + res[1] * x + res[2]
figure, axes = plt.subplots()
axes.plot(x, y, color='Navy')  # Узнать про linewidth
axes.grid()
axes.scatter(X, Y, color='red')
axes.set_title('Аппроксимация методом наименьших квадратов')
plt.show()

input()
