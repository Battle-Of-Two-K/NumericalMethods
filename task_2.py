from python_code.main import *

# Матрица из задания
matrix = Matrix([
    [42, 6, 1],
    [-8, -37, 10],
    [-3, -5, -39],
])
# Столбец свободных членов
free_column = [307, -23, -299]

print("Введенная матрица:")
matrix.console_display()

if not matrix.is_dominant:
    print("Матрица не сходится")
    input('Нажмите "Enter" чтобы выйти...')
else:
    print("Решение методом простых итераций:")
    iterations.simple_iterations(Matrix(matrix.matrix[:]), free_column, stop_level=10, print_middle_values=True)

    print("\nРешение методом Зейделя")
    iterations.zeidel_method(matrix, free_column, stop_level=5, print_middle_values=True)

input('Нажмите "Enter" чтобы выйти...')