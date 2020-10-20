from math import *

try:
    n = 4  # Количество шагов
    a = 0  # Нижний предел (в градусах)
    b = 90  # Верхний предел (в градусах)

    list_1 = list()
    list_2 = list()


    def integrand(X):
        for i in range(n + 1):
            c = ((b - a) / n) * (pi / 180)
            A = sin(X)
            list_1.append(X)
            list_2.append(A)
            print(f'X: {X}')
            print(f'Y: {A}\n')
            X += c


    def summa(X):
        for i in list_1:
            if i % 2 == 0:
                sum





    print(summa(0))
    integrand(0)

    # h = ((b - a) * (pi / 180)) / n
    # T_n = (h / 2) * (sin(a * (pi / 180)) + 2 * summa(0) + sin(b * (pi / 180)))

    print(T_n)

except Exception as error:
    print(error)
input('\nНажмите "Enter" чтобы выйти...')