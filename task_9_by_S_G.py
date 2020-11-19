from python_code.methods.approx.minimal_sqr import minimal_sqr
from python_code.methods.approx.linear_approx import linear_approx
from python_code.staf.sympy_init import *

__author__ = 'simens_green'

# =========================================================
# Аппроксимация методом наименьших квадратов (квадратичная)
# =========================================================

try:
    # Таблица из задания
    table_for_minimal_sqr = {
        'x': [-6, -5, -4, -2],
        'y': [36, 27, 19, 7],
        'Подставить значения': [-2, -1, 0, 1, 2],
        'Построить график?': 'нет'
    }

    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================
    function = None
    polynomial = None
    print(' Аппроксимация методом минимальных квадратов '.center(100, '='))
    decision = minimal_sqr([table_for_minimal_sqr['x'], table_for_minimal_sqr['y']], level_of_details=2)
    for step in decision:
        for info in step:
            if 'Матрица' in info:
                step[info].console_display()
            elif 'python' in info:
                function = step[info]
                continue
            else:
                print(f"{info}: {step[info]}")
            if 'Многочлен' in info:
                polynomial = step['Многочлен']
        print()

    for val in table_for_minimal_sqr['Подставить значения']:
        print(f'y({val}) = {round(function(val), 8)}')

    if table_for_minimal_sqr['Построить график?'].lower() == 'да':
        plot(polynomial)

except Exception as error:
    print(error)

input('\nНажмите "Enter" чтобы выйти...')
