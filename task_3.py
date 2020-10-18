from python_code.main import *

# =============================
# Решение СЛАУ методом прогонки
# =============================

try:
    # Матрица из задания
    matrix = Матрица([
                     [7, -1, 0, 0, 0],
                     [5, -11, -4, 0, 0],
                     [0, 2, -8, 4, 0],
                     [0, 0, -4, 7, -4],
                     [0, 0, 0, 4, -8]
    ])
    # Столбец свободных членов
    free_column = [10, 54, 42, 28, -16]

    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================

    print(f"Столбец свободных членов: {free_column}\n")

    print("Введенная матрица:\n")
    matrix.показать_в_консоли()

    print("Решение методом прогонки:\n")
    solution = iterations.triple_diagonal(matrix, free_column, level_of_detail=2)
    for step in solution:
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
