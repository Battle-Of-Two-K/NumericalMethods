from my_class import *

my_matrix = [[-11, 7, -1, 6],
             [-11, -9, 2, -7],
             [9, -3, 1, -2],
             [-5, 4, -1, -11]]

matrix_ = My_matrix(my_matrix)


def determinant(matrix: list):
    """
    Вычисление определителя квадратной матрицы

    Args:
        matrix(list): матрица
        mul(int): расчётный коэффициент (при вызове функции = 1)

    Returns: определитель матрицы

    """
    width = len(matrix)
    if width == 1:
        return matrix[0][0]
    else:
        sign = -1
        summa = 0
        for row in range(width):
            new_list = []
            for col in range(1, width):
                buffer = []
                for k in range(width):
                    if k != row:
                        buffer.append(matrix[col][k])
                new_list.append(buffer)
            sign *= -1
            summa += sign * matrix[0][row] * determinant(new_list)
        return


# def print_matrix(matrix):


print(f'Определитель введённой матрицы равен: {matrix_.determinant(1)}')
