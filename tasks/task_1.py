import sys
import os
sys.path.append(os.path.pardir)

from NumericalMethods.first_problem_direct import gauss
from NumericalMethods import Matrix

# =============================================================
# Метод Гаусса для решения СЛАУ, обратная матрица и оределитель
# =============================================================


def main():
    # Матрица из задания
    matrix = Matrix([
        [-11, 7, -1, 6],
        [-11, -9, 2, -7],
        [9, -3, 1, -2],
        [-5, 4, -1, -11]
    ])
    # Столбец свободных членов
    free_column = [74, 60, -54, -66]

    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================

    print("Введенная матрица:")
    matrix.console_display()

    print(f'Определитель данной матрицы равен {matrix.det}\n')

    print("Матрица, обратная данной:")
    (matrix ** (-1)).console_display()

    print('\n' + " Решение методом Гаусса для данной СЛАУ: ".center(75, '='))
    decision = gauss(matrix.copy(), free_column, level_of_details=2)
    for step in decision:
        for info in step:
            if 'Матрица' in info:
                step[info].console_display()
            else:
                print(f"{info}: {step[info]}")


if __name__ == '__main__':
    # Файлы task_%.py сделаны для людей, для которых установка интерпретатора может стать испытанием.
    # Запускают эти люди двойными кликом. А если перед ними консоль будет мгновенно закрываться в случае ошибки,
    # это будет жуткий стресс, а я даже помочь быстро не смогу, а так хоть print ошибки есть.
    try:
        main()
    except Exception as error:
        print(error)
    input('Нажмите "Enter" чтобы выйти...')
