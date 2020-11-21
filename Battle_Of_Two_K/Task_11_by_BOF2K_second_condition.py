from sympy.abc import *
from python_code.main import Matrix
import matplotlib.pyplot as plt

# Вариант 7
function = 2 * z - y - 3 * x + 6
a = -4
b = -2
x_0 = -4
y_0 = 6
z_0 = -3

# Вариант 1
# function = 2 * z + 2 * y + 4 * x - 5
# a = -2
# b = 0
# x_0 = -2
# y_0 = -4
# z_0 = -1

# Вариант 18
# function = 2 * z - 2 * y + 2 * x + 2
# a = 3
# b = 5
# x_0 = 3
# y_0 = 5
# z_0 = -6


# Условие задачи из методички
# function = -z / (2 * x)
# a = 1
# b = 10
# x_0 = 1
# y_0 = 2
# z_0 = 1


def number_of_segments(h):
    """
    Returns:
        int: количество отрезков одинаковой длины
    """
    return int((b - a) / h)


def index_generator():
    """
    Returns:
        list: список индексов i
    """
    output_list = []
    for index in range(0, number_of_segments(h) + 1):
        output_list.append(index)
    return output_list


def decision_Euler_1(h):
    y_0_ = y_0
    z_0_ = z_0
    x_0_ = x_0
    a_ = a
    list_1 = []
    list_2 = []
    matrix = Matrix(0)
    matrix.columns = 4
    matrix.matrix[0] = ['i', 'x', 'y', 'z']

    for step in range(0, number_of_segments(h) + 1):
        list_1.append(x_0_)
        list_2.append(y_0_)
        matrix.append_row([step, x_0_, y_0_, z_0_])
        y_0_ += h * z_0_
        z_0_ += h * function.evalf(subs={x: x_0_, z: z_0_, y: y_0_})
        x_0_ += h
        a_ += h
    return list_1


def decision_Euler_2(h):
    y_0_ = y_0
    z_0_ = z_0
    x_0_ = x_0
    a_ = a
    list_1 = []
    list_2 = []
    matrix = Matrix(0)
    matrix.columns = 4
    matrix.matrix[0] = ['i', 'x', 'y', 'z']

    for step in range(0, number_of_segments(h) + 1):
        list_1.append(x_0_)
        list_2.append(y_0_)
        matrix.append_row([step, x_0_, y_0_, z_0_])
        y_0_ += h * z_0_
        z_0_ += h * function.evalf(subs={x: x_0_, z: z_0_, y: y_0_})
        x_0_ += h
        a_ += h
    return list_2


def decision_Runge_Kutta(h):
    y_0_ = y_0
    z_0_ = z_0
    x_0_ = x_0
    a_ = a
    index = 1
    matrix = Matrix(0)
    matrix.columns = 12
    matrix.matrix[0] = ['i', 'K1y', 'K1z', 'K2y', 'K2z', 'K3y', 'K3z', 'K4y', 'K4z', 'X', 'Y', 'Z']

    while a_ < b:
        k1y = z_0_
        k1z = function.evalf(subs={x: x_0_, y: y_0_, z: z_0_})
        k2y = z_0_ + (h / 2) * k1z
        k2z = function.evalf(subs={x: x_0_ + (h / 2), y: y_0_ + (h / 2) * k1y, z: z_0_ + (h / 2) * k1z})
        k3y = z_0_ + (h / 2) * k2z
        k3z = function.evalf(subs={x: x_0_ + (h / 2), y: y_0_ + (h / 2) * k2y, z: z_0_ + (h / 2) * k2z})
        k4y = z_0_ + h * k3z
        k4z = function.evalf(subs={x: x_0_ + h, y: y_0_ + h * k3y, z: z_0_ + h * k3z})

        x_0_ += h
        y_0_ += (h / 6) * (k1y + 2 * k2y + 2 * k3y + k4y)
        z_0_ += (h / 6) * (k1z + 2 * k2z + 2 * k3z + k4z)

        matrix.append_row([index, k1y, k1z, k2y, k2z, k3y, k3z, k4y, k4z, x_0_, y_0_, z_0_])

        index += 1
        a_ += h
    print(matrix.T.to_pretty_string())


def grafik(h):
    figure, axes = plt.subplots()

    axes.scatter(decision_Euler_1(h), decision_Euler_2(h), color='red')
    axes.grid()
    axes.set_title(f'Метод Рунге-Кутты. h = {h}')

    plt.show()


# Условие из методички
# decision_Euler(0.9)
# decision_Runge_Kutta(1.8)

# print('______________________________________________________________')
# print('-------------Метод Эйлера для ОДУ второго порядка-------------')
# print('\nh = 0.5')
# decision_Euler(0.5)
# print('\nh = 0.25')
# decision_Euler(0.25)
# print('\nh = 0.2')
# decision_Euler(0.2)
#
# print('----------------Уточнение по формуле Рунге----------------\n')
#
# d_1 = np.array([[9, 1 ** 1, 1 ** 2], [17.4609375000000, .5 ** 1, .5 ** 2], [26.6972070587799, .25 ** 1, .25 ** 2]])
# d_2 = np.array([[1, 1 ** 1, 1 ** 2], [1, .5 ** 1, .5 ** 2], [1, .25 ** 1, .25 ** 2]])
#
# print(d_1)
# print('----------------------------------------- = Zp')
# print(d_2)
# print('\nВыислим определители:\n')
#
# D_1 = np.linalg.det(d_1)
# D_2 = np.linalg.det(d_2)
#
# print(D_1)
# print('-------------------- = Zp')
# print(D_2)
#
# print(f'\nz_p = {D_1 / D_2}')

print('_' * 70)
print(' Метод Рунге-Кутты для ОДУ второго порядка '.center(70, '-'))
print('\nh = 1')
decision_Runge_Kutta(1)
grafik(1)
print('\nh = 0.5')
decision_Runge_Kutta(0.5)
grafik(0.5)

print('\n' + ' Уточнение по формуле Рунге-Ромберга '.center(70, '-'))

R = .5

Zpp = 48.6562500000000 + ((48.6562500000000 - 50.1638414636254) / (R ** 4 - 1))

print(f'\nZpp = {Zpp}\n')


input()
