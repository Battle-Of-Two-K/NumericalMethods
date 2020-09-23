from python_code.methods.equation import dichotomy
from math import *

# =============================================
# Нахождение корней уравнения методом дихотомии
# =============================================


def f(x: (int, float)) -> (float, int):
    # Здесь нужно написать функцию из задания
    # Функция принимает единственное значение x (икс) и возвращает (return) значение функции f(x)
    # Ниже написано: икс в степени два минус 2
    return x ** 2 - 2
    # Например, число эйлера (экспонента) в степени икс минус пять икс плюс десять с половиной выглядит так:
    return e ** x - 5 * x + 10.5


# Отрезок из задания
section = (0, 8)

# ============================================================
# ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
# ATTENTION!  Not for timid people! Below is the program code!
# ============================================================

try:
    decision = dichotomy(f, section, accuracy_order=8, level_of_details=2)
    for step in decision:
        step_info = ''
        for info in step:
            if 'Решение' in step.keys():
                step_info += f'{info}: {round(step[info], 8) if isinstance(step[info], float) else step[info]}\n'
            else:
                step_info += f'{info}: ' \
                             f'{round(step[info], 8) if isinstance(step[info], float) else step[info]}'.center(20) + '|'
        if 'Решение' in step.keys():
            print(('-' * 20 + '+') * (len(step.keys()) + 3), '\n')
        else:
            print(('-' * 20 + '+') * len(step.keys()))
        print(step_info)

except Exception as error:
    print(error)

input('\nНажмите "Enter" чтобы выйти...')
