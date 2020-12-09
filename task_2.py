from python_code.main import *

# =======================================================
# Решение СЛАУ методом простых итераций и методом Зейделя
# =======================================================

try:
    # Матрица из задания
    matrix = Matrix([
        [38, -10, -1],
        [2, -36, 9],
        [6, -1, -37],
    ])
    # Столбец свободных членов
    free_column = [-293, -23, -303]

    print("Введенная матрица:")
    matrix.console_display()

    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================

    print(f"Столбец свободных членов: {free_column}\n")

    if not matrix.is_dominant:
        print("Матрица не сходится")
        input('Нажмите "Enter" чтобы выйти...')
        exit()
    else:
        print(f"\n{' Решение методом простых итераций '.center(50, '=')}\n")
        solution = iterations.simple_iterations(matrix, free_column, iterations=10, level_of_detail=2)
        for step in solution:
            step_info = ''
            for info in step:
                if info not in ['Матрица']:
                    if info in ['Нормы матрицы', 'Нормы вектора', 'Решение']:
                        step_info += f'{info}: {list(map(lambda x: round(x, 8), step[info]))}\n'
                    else:
                        step_info += f'{info}: ' \
                                     f'{step[info] if not isinstance(step[info], float) else round(step[info], 8)}\n'
            print(step_info)

        print(f"\n{' Решение методом Зейделя '.center(50, '=')}\n")
        solution = iterations.zeidel_method(matrix, free_column, iterations=5, level_of_detail=2)
        for step in solution:
            step_info = ''
            for info in step:
                if info not in ['Матрица']:
                    if info in ['Нормы матрицы', 'Нормы вектора', 'Решение']:
                        step_info += f'{info}: {list(map(lambda x: round(x, 8), step[info]))}\n'
                    else:
                        step_info += f'{info}: ' \
                                     f'{step[info] if not isinstance(step[info], float) else round(step[info], 8)}\n'
            print(step_info)

except Exception as error:
    print(error)
input('Нажмите "Enter" чтобы выйти...')
