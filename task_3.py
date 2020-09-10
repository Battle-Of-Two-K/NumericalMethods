from python_code.main import *


try:
    # Матрица из задания
    matrix = Matrix([[7, -1, 0, 0, 0],
                     [5, -11, -4, 0, 0],
                     [0, 2, -8, 4, 0],
                     [0, 0, -4, 7, -4],
                     [0, 0, 0, 4, -8]
                     ])
    # Столбец свободных членов
    free_column = [10, 54, 42, 28, -16]

    print("Введенная матрица:\n")
    matrix.console_display()

    print("Решение методом прогонки:\n")
    result = iterations.triple_diagonal(matrix, free_column, print_middle_values=True)

    print("\nОтвет:")
    Matrix([result]).console_display()
except Exception as error:
    print(error)
input('Нажмите "Enter" чтобы выйти...')
