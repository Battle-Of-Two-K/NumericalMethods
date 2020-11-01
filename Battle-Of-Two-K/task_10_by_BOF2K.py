from Battle-Of-Two-K.Numerical_integration import *
import numpy as np

try:
    my_variant_1 = TrapezoidalFormula(-3, 1, 1)

    print('---------------------------ФОРМУЛА ТРАПЕЦИЙ---------------------------')
    print(f'--------------------------------h1 = {my_variant_1.h}--------------------------------')
    print(f'Кол-во отрезков n = {my_variant_1.n()}\n')
    print(my_variant_1.table_Y())
    print(f'\nT_n = {my_variant_1.t_n()}')

    my_variant_2 = TrapezoidalFormula(-3, 1, 0.5)

    print(f'--------------------------------h2 = {my_variant_2.h}--------------------------------')
    print(f'Кол-во отрезков n = {my_variant_2.n()}\n')
    print(my_variant_2.table_Y())
    print(f'\nT_n = {my_variant_2.t_n()}\n')

    my_variant_3 = TrapezoidalFormula(-3, 1, 0.25)

    print(f'--------------------------------h3 = {my_variant_3.h}--------------------------------')
    print(f'Кол-во отрезков n = {my_variant_3.n()}\n')
    print(my_variant_3.table_Y())
    print(f'\nT_n = {my_variant_3.t_n()}\n')
    print('----------------Уточнение по формуле Рунге----------------\n')
    d_1 = np.array([[my_variant_1.t_n(), 1 ** 2, 1 ** 3], [my_variant_2.t_n(), .5 ** 2, .5 ** 3],
                    [my_variant_3.t_n(), .25 ** 2, .25 ** 3]])

    d_2 = np.array([[1, 1 ** 2, 1 ** 3], [1, .5 ** 2, .5 ** 3], [1, .25 ** 2, .25 ** 3]])

    print(d_1)
    print('------------------------------------ = Zp')
    print(d_2)
    print(' \n')

    D_1 = np.linalg.det(d_1)
    D_2 = np.linalg.det(d_2)

    print(D_1)
    print('-------------------- = Zp')
    print(D_2)

    print(f'\nz_p = {D_1 / D_2}')

    my_variant = SimpsonFormula(-3, 1, 1, 4)

    print('---------------------------ФОРМУЛА СИМПСОНА---------------------------')
    print(f'---------------------------h1 = {my_variant.h}---------------------------')
    print(f'Кол-во отрезков n = {my_variant.n()}\n')
    print(my_variant.table_Y())

    print(f'\nT_n = {my_variant.S()}\n')

    my_variant_0 = SimpsonFormula(-3, 1, 0.5, 4)
    print(f'---------------------------h2 = {my_variant_0.h}---------------------------')
    print(f'Кол-во отрезков n = {my_variant_0.n()}\n')
    print(my_variant_0.table_Y())
    print(f'\nT_n = {my_variant_0.S()}\n')
    print('\n----------------Уточнение по формуле Рунге-Ромберга----------------')

    R = my_variant_0.h / my_variant.h

    z_pp = my_variant.S() + ((my_variant.S() - my_variant_0.S()) / (R ** my_variant.p - 1))

    print(f'R = {R}')
    print(f'Zp = {z_pp}')

except Exception as error:
    print(error)
input('Нажмите "Enter" чтобы выйти...')
