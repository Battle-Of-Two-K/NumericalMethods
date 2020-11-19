from python_code.methods.boundary_problem.final_diff import final_difference_method
from python_code.staf.sympy_init import *


# =========================================================
# Решение краевой задачи для ОДУ методом конечных разностей
# =========================================================


try:
    expression = "2 * x ** 2 * y'' + x * y' + y= 2 * sqrt(x)"

    section_corners = (1, 10)

    number_of_sections = 4

    boundaries = {
        'S': 1,
        'T': 2,
        'R': 0,
        'V': 0,
    }


    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================

    decision = final_difference_method(expression,
                                       boundaries,
                                       section_corners,
                                       number_of_sections,
                                       level_of_detail=2)
    for step in decision:
        for key in step:
            if 'Матрица' in key:
                step[key].console_display()
            elif isinstance(step[key], float):
                print(f'{key}: {round(step[key], 8)}')
            elif isinstance(step[key], list):
                print(f'{key}: {list(map(lambda val: round(float(val), 8), step[key]))}')
            else:
                print(f'{key}: {step[key]}')

except Exception as error:
    print(error)

input('\nНажмите "Enter" чтобы выйти...')
