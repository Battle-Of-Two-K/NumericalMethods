from python_code import *

# ==================================================
# Нахождение спектрального радиуса степенным методом
# ==================================================
try:
    # Матрица из задания
    matrix = Matrix([[19, 5, 8],
                     [5, -1, -6],
                     [8, -6, -3]])

    # Количество итераций
    number_of_iterations = 21

    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================

    print("Введенная матрица:\n")
    matrix.console_display()

    print("Нахождение спектрального радиуса степенным методом:\n")
    decision = spectral_rad_power_method(matrix, level_of_detail=2, iterations=number_of_iterations)
    for step in decision:
        step_info = ''
        for info in step:
            if info not in ['Матрица']:
                if isinstance(step[info], (tuple, list)):
                    step_info += f'{info}: {list(map(lambda x: round(x, 8), step[info]))}\n'
                elif isinstance(step[info], float):
                    step_info += f'{info}: {round(step[info], 8)}\n'
                else:
                    step_info += f'{info}: {step[info]}\n'
        print(step_info)

except Exception as error:
    print(error)
input('Нажмите "Enter" чтобы выйти...')
