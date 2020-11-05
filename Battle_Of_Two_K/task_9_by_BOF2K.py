import matplotlib.pyplot as plt
import numpy as np

__author__ = 'Battle_Of_Two_K'

# /////////////////////////////////////////////
# Аппроксимация  методом  наименьших  квадратов
# Требуется установка модулей numpy, matplotlib
# /////////////////////////////////////////////


x = [-6, -5, -4, -2]
y = [36, 27, 19, 7]

# ///////////////////////////////////////////////////////////////////////////////////
# Пугливым не смотреть! Ниже програмный код!
# ///////////////////////////////////////////////////////////////////////////////////

n = len(x)
m = len(y)

print(f'n = {n}')
print('--------------------Вычислим коэффициенты системы--------------------\n')

print(f'Сумма чисел списка x: {sum(x)}')


def summa_xn(x_list, n_power):
    """Функция, которая считает сумму элементов в указанной степени"""
    return sum((elem ** n_power for elem in x_list))


def summa_x2(x):
    """Функция, которая считает сумму квадратов"""
    s = 0
    for i in x:
        s += i * i
    return s


print(f'Сумма квадратов чисел списка x: {summa_x2(x)}')


def summa_x3(x):
    """Функция, которая считает сумму кубов"""
    s = 0
    for i in x:
        s += i * i * i
    return s


print(f'Сумма кубов чисел списка x: {summa_x3(x)}')


def summa_x4(x):
    """Функция, которая считает сумму чисел в 4-й степени"""
    s = 0
    for i in x:
        s += i * i * i * i
    return s


print(f'Сумма чисел в 4-й степени списка x: {summa_x4(x)}\n')

print(f'Сумма чисел списка y: {sum(y)}')


def summa_xy(x, y):
    """Функция, которая находит сумму перемноженных элементов списков x и y"""
    s = list(map(lambda i, j: i * j, x, y))
    k = sum(s)
    return k


print(f'Сумма перемноженных чисел списков x и y: {summa_xy(x, y)}')


def summa_xxy(x, y):
    """Функция, которая считает сумму x**2 * y"""
    s = list(map(lambda i, j: (i ** 2) * j, x, y))
    k = sum(s)
    return k


print(f'Сумма x**2 * y: {summa_xxy(x, y)}\n')

print('---------------------------Решим систему---------------------------\n')

Matrix = np.array([[summa_x4(x), summa_x3(x), summa_x2(x)],
                      [summa_x3(x), summa_x2(x), sum(x)],
                      [summa_x2(x), sum(x), n]])  # Матрица (левая часть системы)
Vector = np.array([summa_xxy(x, y), summa_xy(x, y), sum(y)])  # Вектор (правая часть системы)

otvet = np.linalg.solve(Matrix, Vector)

print(f'a = {otvet[0]}')
print(f'b = {otvet[1]}')
print(f'c = {otvet[2]}\n')


def function_P(x):
    P = otvet[0] * x * x + otvet[1] * x + otvet[2]
    return P


def square_residual(x, y):
    s = list(map(lambda i, j: ((function_P(i) - j) ** 2), x, y))
    k = sum(s)
    return k


print(f'Квадратическая невязка = {square_residual(x, y)}')

x = np.linspace(-5, 2, 100)  # от -5 до 2 сделать 100 точек
y = otvet[0] * x * x + otvet[1] * x + otvet[2]  # y1 - тоже много точек

fig, ax = plt.subplots()  # будет 1 график, на нем:
ax.plot(x, y, color="blue", label="y(x)")  # функция y1(x), синий, надпись y(x)
ax.set_xlabel("x")  # подпись у горизонтальной оси х
ax.set_ylabel("y")  # подпись у вертикальной оси y
ax.legend()  # показывать условные обозначения

plt.show()  # показать рисунок
fig.savefig('1.png')  # сохранить в файл 1.png
