from sympy.abc import *
from python_code.main import Matrix

function = -z / (2 * x)
a = 1
b = 10
x_0 = 1
y_0 = 2
z_0 = 1
h = 1.8


def number_of_segments():
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
    for index in range(0, number_of_segments() + 1):
        output_list.append(index)
    return output_list


def decision():
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
        k1z = function.evalf(subs={x: x_0_, z: z_0_})
        k2y = z_0_ + (h / 2) * k1z
        k2z = function.evalf(subs={x: x_0_ + (h / 2), z: z_0_ + (h / 2) * k1z})
        k3y = z_0_ + (h / 2) * k2z
        k3z = function.evalf(subs={x: x_0_ + (h / 2), z: z_0_ + (h / 2) * k2z})
        k4y = z_0_ + h * k3z
        k4z = function.evalf(subs={x: x_0_ + h, z: z_0_ + h * k3z})

        x_0_ += h
        y_0_ += (h / 6) * (k1y + 2 * k2y + 2 * k3y + k4y)
        z_0_ += (h / 6) * (k1z + 2 * k2z + 2 * k3z + k4z)
        matrix.append_row([index, k1y, k1z, k2y, k2z, k3y, k3z, k4y, k4z, x_0_, y_0_, z_0_])

        # print('i:{: ^20} | K1y:{: ^20} | K1z:{: ^20} | K2y:{: ^20} | K2z:{: ^20} | K3y:{: ^20} | K3z:{: ^20}'
        #       ' |K4y:{: ^20} |K4z:{: ^20} |X:{: ^20} |Y:{: ^20}'
        #       ' |Z:{: ^20} |'.format(index, str(k1y), str(k1z), str(k2y), str(k2z), str(k3y), str(k3z), str(k4y),
        #                              str(k4z), str(x_0_), str(y_0_), str(z_0_)))
        # print('------------------------------------------------------------------------------------------------------'
        #       '-------------------------------------------------------------------------------------------------------'
        #       '-------------------------------------------------------------------------------------------------------')

        index += 1
        a_ += h
    matrix.console_display()


decision()
input()
