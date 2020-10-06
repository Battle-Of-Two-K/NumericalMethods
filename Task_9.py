import matplotlib.pyplot as plt
import numpy as np
import numpy

x = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y = [2.4, 3.7, 4, 3.9, 4.8, 4.7, 4, 3.1, 2.4, 1.7]

# ///////////////////////////////////////////////////////////////////////////////////
# Пугливым не смотреть! Ниже програмный код!
# ///////////////////////////////////////////////////////////////////////////////////

n = len(x)
m = len(y)

print(f'n = {n}')
print('--------------------Вычислим коэффициенты системы--------------------\n')

#Функция, которая считает сумму введённого списка x:
def Summa_x(x):
	s = 0 
	for i in x:
		s += i
	return s

print(f'Сумма чисел списка x: {Summa_x(x)}')

#Функция, которая считает сумму квадратов:
def Summa_x2(x):
	s = 0 
	for i in x:
		s += i*i
	return s

print(f'Сумма квадратов чисел списка x: {Summa_x2(x)}')

#Функция, которая считает сумму кубов:
def Summa_x3(x):
	s = 0 
	for i in x:
		s += i*i*i
	return s

print(f'Сумма кубов чисел списка x: {Summa_x3(x)}')

#Функция, которая считает сумму чисел в 4-й степени:
def Summa_x4(x):
	s = 0 
	for i in x:
		s += i*i*i*i
	return s

print(f'Сумма чисел в 4-й степени списка x: {Summa_x4(x)}\n')

#Функция, которая считает сумму введённого списка y:
def Summa_y(y):
	s = 0 
	for i in y:
		s += i
	return s

print(f'Сумма чисел списка y: {Summa_y(y)}')

#Функция, которая находит сумму перемноженных элементов списков x и y:
def Summa_xy(x, y):
	s = list(map(lambda i, j: i * j, x, y))
	k = sum(s)
	return k
		
print(f'Сумма перемноженных чисел списков x и y: {Summa_xy(x, y)}')

#Функция, которая считает сумму x**2 * y:
def Summa_xxy(x, y):
	s = list(map(lambda i, j: (i ** 2) * j, x, y))
	k = sum(s)
	return k
		
print(f'Сумма x**2 * y: {Summa_xxy(x, y)}\n')

print('---------------------------Решим систему---------------------------\n')

Matrix = numpy.array([[Summa_x4(x), Summa_x3(x), Summa_x2(x)], [Summa_x3(x), Summa_x2(x), Summa_x(x)], [Summa_x2(x), Summa_x(x), n]]) # Матрица (левая часть системы)
Vector = numpy.array([Summa_xxy(x, y), Summa_xy(x, y), Summa_y(y)]) # Вектор (правая часть системы)

otvet = numpy.linalg.solve(Matrix, Vector)

print(f'a = {otvet[0]}')
print(f'b = {otvet[1]}')
print(f'c = {otvet[2]}\n')

def Function_P(x):
	P = otvet[0] * x*x + otvet[1]*x + otvet[2]
	return P

def Square_residual(x, y):
	s = list(map(lambda i, j: ((Function_P(i) - j)**2), x, y))
	k = sum(s)
	return k

print(f'Квадратическая невязка = {Square_residual(x, y)}')

x = np.linspace(-5, 2, 100)                     # от -5 до 2 сделать 100 точек
y = otvet[0] * x*x + otvet[1]*x + otvet[2]                         # y1 - тоже много точек

fig, ax = plt.subplots()                        # будет 1 график, на нем:
ax.plot(x, y, color="blue", label="y(x)")      # функция y1(x), синий, надпись y(x)
ax.set_xlabel("x")                              # подпись у горизонтальной оси х
ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                                     # показывать условные обозначения

plt.show()                                      # показать рисунок
fig.savefig('1.png')                            # сохранить в файл 1.png
