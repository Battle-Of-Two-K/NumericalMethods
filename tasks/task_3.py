from NumericalMethods.first_problem_direct import triple
from NumericalMethods import Matrix
# =============================
# Решение СЛАУ методом прогонки
# =============================


def main():
    # Матрица из задания
    matrix = Matrix([
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
    matrix.console_display()

    print("Решение методом прогонки:\n")
    solution = triple(matrix, free_column, level_of_detail=2)
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


if __name__ == '__main__':
    # Файлы task_%.py сделаны для людей, для которых установка интерпретатора может стать испытанием.
    # Запускают эти люди двойными кликом. А если перед ними консоль будет мгновенно закрываться в случае ошибки,
    # это будет жуткий стресс, а я даже помочь быстро не смогу, а так хоть print ошибки есть.
    try:
        main()
    except Exception as error:
        print(error)
    input('Нажмите "Enter" чтобы выйти...')
