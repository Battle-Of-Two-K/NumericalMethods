from math import *

try:
    n = 4  # Количество шагов
    a = 0  # Нижний предел (в градусах)
    b = 90  # Верхний предел (в градусах)


    def integrand(X):
        for i in range(n + 1):
            c = ((b - a) / n) * (pi / 180)
            A = sin(X)
            print(f'X: {X}')
            print(f'Y: {A}\n')
            X += c


    def summa(X):
        Summa_ = 0
        for i in range(n):
            c = ((b - a) / n) * (pi / 180)
            A = sin(X)
            Summa_ += A
            X += c
        return Summa_ - sin(a)


    integrand(0)

    h = ((b - a) * (pi / 180)) / n
    T_n = (h / 2) * (sin(a * (pi / 180)) + 2 * summa(0) + sin(b * (pi / 180)))

    print(T_n)

except Exception as error:
    print(error)
input('\nНажмите "Enter" чтобы выйти...')
