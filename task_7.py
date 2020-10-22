from python_code.methods.snlau.newton_linearization import newton_linearization
from python_code.methods.snlau.simple_iterations import simple_iterations, zeidel_method
from python_code import *

# ==========================================================================================================
# Нахождение решения системы нелинейных уравнений методом Ньютона (линеаризации), Зейделя и простых итераций
# ==========================================================================================================

try:
    # Переменные, для которых требуется решение (порядок имеет значение)
    variables = ['x', 'y']

    # Система уравнений
    system = [
        '4 * x*x*x - 2 * y*y*y + 5',
        '2 * x*y - 2 * y - 16'
    ]

    # Начальное приближение
    init_approx = (-3, -4)
    # init_approx = (4, 6)

    transformed_system = None
    # Пример ручного преобразования системы (оставить # в началах строк для автоматического преобразования)
    # transformed_system = {
    #     'x': 'sqrt(y)',
    #     'y': 'sqrt(4 - x ** 2)'
    # }

    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================

    print(' Решение методом Ньютона (линеаризации) '.center(100, '='))
    decision = newton_linearization(system, variables, init_approx,
                                    accuracy_order=8, level_of_details=2, iterations=5)
    for step in decision:
        for info in step:
            if isinstance(step[info], Matrix):
                print(f'{info}:\n')
                step[info].console_display()
            elif isinstance(step[info], dict):
                for key in step[info]:
                    print(f'{key}: {round(step[info][key], 8)}', end='; ')
                print()
            else:
                print(f'{info}: {round(step[info], 8) if isinstance(step[info], float) else step[info]}')
        print()

    print(' Решение методом простых итераций '.center(100, '='))
    decision = simple_iterations(system, variables, init_approx, transformed_system=transformed_system,
                                 level_of_details=2, accuracy_order=8, iterations=5)
    for step in decision:
        step_info = ''
        for info in step:
            if isinstance(step[info], Matrix):
                print(info, ':')
                step[info].console_display()
            else:
                try:
                    step_info += f'{info}: {round(step[info], 8)}'.center(25) + '|'
                except TypeError:
                    step_info += f'{info}: {step[info]}\n'
        print(step_info)

    print(' Решение методом Зейделя '.center(100, '='))
    decision = zeidel_method(system, variables, init_approx, transformed_system=transformed_system,
                             level_of_details=2, accuracy_order=8, iterations=5)
    for step in decision:
        step_info = ''
        for info in step:
            if isinstance(step[info], Matrix):
                print(info, ':')
                step[info].console_display()
            else:
                try:
                    step_info += f'{info}: {round(step[info], 8)}'.center(25) + '|'
                except TypeError:
                    step_info += f'{info}: {step[info]}\n'
        print(step_info)

except Exception as error:
    print(error)

input('\nНажмите "Enter" чтобы выйти...')
