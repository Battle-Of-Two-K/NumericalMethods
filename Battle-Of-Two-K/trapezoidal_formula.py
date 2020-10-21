from math import *

try:
    n = 3  # Количество шагов
    a = -3  # Нижний предел (в градусах)
    b = 1  # Верхний предел (в градусах)


    def integrand(x):
        for i in range(n + 1):
            c = (b - a) / n
            A = (7 * x + 2) / (x * x + 5)
            print(f'X: {x}')
            print(f'Y: {A}\n')
            x += c


    def summa(x):
        Summa_ = 0
        for i in range(n):
            c = (b - a) / n
            A = (7 * x + 2) / (x * x + 5)
            Summa_ += A
            x += c
        return Summa_ - A(a)


    integrand(0)

    h = ((b - a) * (pi / 180)) / n
    T_n = (h / 2) * (A(a)) + 2 * A(0) + A(b)

    print(T_n)

except Exception as error:
    print(error)
input('\nНажмите "Enter" чтобы выйти...')
