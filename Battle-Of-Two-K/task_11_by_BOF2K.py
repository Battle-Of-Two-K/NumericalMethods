from Numerical_methods.First_order_ODE import *
import numpy as np

print('_______________Решение задачи Коши методом Эйлера_______________\n')
eg1 = EulerMethod(7, 11, 7, 7, 1)
print(f'Введённые данные:\na = {eg1.a}; b = {eg1.b}; x0 = {eg1.x_0}; y0 = {eg1.y_0}; h = {eg1.h}\n')
print(f'-----------Для h1 = {eg1.h}-----------\n')
# print(f'x: {eg1.x_i()}')
# print(f'y: {eg1.y_i()}\n')
eg1.print_()
z1 = eg1.y_i().pop()
print(f'Уточнить y(6) = {z1}\n')

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

eg2 = EulerMethod(7, 11, 7, 7, .5)
print(f'Введённые данные:\na = {eg2.a}; b = {eg2.b}; x0 = {eg2.x_0}; y0 = {eg2.y_0}; h = {eg2.h}\n')
print(f'-----------Для h2 = {eg2.h}-----------\n')
# print(f'x: {eg2.x_i()}')
# print(f'y: {eg2.y_i()}\n')
eg2.print_()
z2 = eg2.y_i().pop()
print(f'Уточнить y(6) = {z2}\n')

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

eg3 = EulerMethod(7, 11, 7, 7, .4)
print(f'Введённые данные:\na = {eg3.a}; b = {eg3.b}; x0 = {eg3.x_0}; y0 = {eg3.y_0}; h = {eg3.h}\n')
print(f'-----------Для h3 = {eg3.h}-----------\n')
# print(f'x: {eg3.x_i()}')
# print(f'y: {eg3.y_i()}\n')
eg3.print_()
z3 = eg3.y_i().pop()
print(f'Уточнить y(6) = {z3}\n')

print('_______________Уточнение по формуле Рунге_______________\n')

d_1 = np.array([[z1, 1 ** 1, 1 ** 2], [z2, .5 ** 1, .5 ** 2], [z3, .4 ** 1, .4 ** 2]])
d_2 = np.array([[1, 1 ** 1, 1 ** 2], [1, .5 ** 1, .5 ** 2], [1, .4 ** 1, .4 ** 2]])

print(d_1)
print('------------------------------------------------------ = Zp')
print(d_2)
print(' \n')

D_1 = np.linalg.det(d_1)
D_2 = np.linalg.det(d_2)

print(D_1)
print('-------------------- = Zp')
print(D_2)

print(f'\nz_p = {D_1 / D_2}')
