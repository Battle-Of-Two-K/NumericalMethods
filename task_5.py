from python_code import *

# ==============================================================
# Нахождение собственных чисел и векторов методом вращения Якоби
# ==============================================================

try:
    # Матрица из задания
    matrix = Matrix([[19, 5, 8],
                     [5, -1, -6],
                     [8, -6, -3]])

    # Количество итераций
    number_of_iterations = 8

    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================

    print("Введенная матрица:\n")
    matrix.console_display()

    print("Нахождение собственных чисел и векторов методом вращения Якоби:\n")
    decision = method_rot_yakobi(matrix, level_of_detail=2, iterations=number_of_iterations)
    for step in decision:
        for info in step:
            if 'матрица' in info.lower():
                print(info, end=':\n\n')
                step[info].console_display()
            elif info == 'Решение':
                print('\n', ' Решение '.center(75, '='), '\n')
                solution = step['Решение']
                for own_num_no in range(len(solution['Собственные числа'])):
                    print(f'{own_num_no + 1} собственное число: {round(solution["Собственные числа"][own_num_no], 8)}')
                    print(f'{own_num_no + 1} собственный вектор: '
                          f'{[round(_, 8) for _ in solution["Собственные векторы"][own_num_no]]}\n')
            elif info == 'Угол поворота фи':
                print(f'\n{info}: {step[info]}\n')
            else:
                print(f' {info}: {step[info]} '.center(75, '='))
except Exception as error:
    print(error)
input('Нажмите "Enter" чтобы выйти...')
