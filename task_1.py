from python_code.main import *

# =============================================================
# Метод Гаусса для решения СЛАУ, обратная матрица и оределитель
# =============================================================


try:
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

    print(f'Определитель данной матрицы равен {det(matrix)}\n')

    print("Матрица, обратная данной:")
    (~matrix).console_display()

    print("\nРешение методом Гаусса для данной СЛАУ:")
    Matrix([gauss.gauss_method(matrix.copy(), free_column, print_middle_values=True)]).console_display()
except Exception as error:
    print(error)
input('Нажмите "Enter" чтобы выйти...')
