from python_code.main import *

# Матрица из задания
matrix = Matrix([[-34, -26, 0, 0, 0],
                 [64, -124, -56, 0, 0],
                 [0, 94, -274, -86, 0],
                 [0, 0, 124, -484, -116],
                 [0, 0, 0, 154, -754]
                 ])
# Столбец свободных членов
free_column = [34, 38, 42, 46, 50]

print("Введенная матрица:\n")
matrix.console_display()

print("Решение методом прогонки:\n")
result = iterations.triple_diagonal(matrix, free_column, print_middle_values=True)

print("\nОтвет:")
Matrix([result]).console_display()

input('Нажмите "Enter" чтобы выйти...')
