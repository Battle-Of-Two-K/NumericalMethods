from python_code import *

# ==================================================
# Нахождение спектрального радиуса степенным методом
# ==================================================


def main():
    # Матрица из задания
    matrix = Matrix([
                     [-4, 4, -4],
                     [4, 2, -8],
                     [-4, -8, 15]
    ])

    # Количество итераций
    number_of_iterations = 12

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


if __name__ == '__main__':
    # Файлы task_%.py сделаны для людей, для которых установка интерпретатора может стать испытанием.
    # Запускают эти люди двойными кликом. А если перед ними консоль будет мгновенно закрываться в случае ошибки,
    # это будет жуткий стресс, а я даже помочь быстро не смогу, а так хоть print ошибки есть.
    try:
        main()
    except Exception as error:
        print(error)
    input('Нажмите "Enter" чтобы выйти...')
