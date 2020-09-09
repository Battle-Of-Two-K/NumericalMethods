from python_code.main import *


# Матрица из задания
matrix = Matrix([
    [-11, 7, -1, 6],
    [-11, -9, 2, -7],
    [9, -3, 1, -2],
    [-5, 4, -1, -11]
])
# Столбец свободных членов
free_column = [74, 60, -54, -66]

print("Введенная матрица:")
matrix.console_display()

print(f'Определитель данной матрицы равен {det(matrix)}\n')

print("Матрица, обратная данной:")
(~matrix).console_display()

print("\nРешение методом Гаусса для данной СЛАУ:")
Matrix([solve_gauss(matrix.copy(), free_column)]).console_display()

input('Нажмите "Enter" чтобы выйти...')
