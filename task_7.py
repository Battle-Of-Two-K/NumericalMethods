from python_code.methods.snlau.newton_linearization import newton_linearization
from python_code import *

# ==============================================================================
# Нахождение решения системы нелинейных уравнений методом Ньютона (линеаризации)
# ==============================================================================

try:
    # Переменные, для которых требуется решение (порядок имеет значение)
    variables = ['x', 'y']

    # Система уравнений
    system = [
        '4 * x*x*x - 2 * y*y*y + 5',
        '2 * x*y - 2 * y - 16'
    ]

    # Начальное приближение
    init_approx = (2, 2)

    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================

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

except Exception as error:
    print(error)

input('\nНажмите "Enter" чтобы выйти...')
