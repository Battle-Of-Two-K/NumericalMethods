import copy


class My_matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        out = f'{self.matrix_size}\n'
        for row in self.matrix:
            out += str(row) + '\n'
        return out

    def null_matrix(self):
        return [[0 for i in self.range_row()] for j in self.range_col()]

    def determinant(self, mul):
        # TODO: В разработке...
        """
        Вычисление определителя квадратной матрицы

        Args:
            mul(int): расчётный коэффициент (при вызове функции = 1)

        Returns: определитель матрицы

        """
        width = len(self.matrix)
        if width == 1:
            return mul * self.matrix[0][0]
        else:
            sign = -1
            summa = 0
            for row in range(width):
                new_list = []
                for col in range(1, width):
                    buffer = []
                    for k in range(width):
                        if k != row:
                            buffer.append(self.matrix[col][k])
                    new_list.append(buffer)
                sign *= -1
                summa += mul * self.determinant(sign * self.matrix[0][row])
            return

    def matrix_multiplication(self, new_matrix):
        # TODO: В разработке...
        output = self.null_matrix
        for row_ in self.range_row():
            for col_ in self.range_col():
                for new_variable in range(1, len(new_matrix[0])):
                    output += self.matrix[row_][new_variable] * new_matrix[new_variable][col_]
        return My_matrix(output())

    def mul_on_num(self, number):
        """
        @param number: Число, на которое умножаем исходную матрица
        @return: матрица, кмноженная на число
        """
        for row_ in self.range_row():
            for col_ in self.range_col():
                self.matrix[row_][col_] *= number
        return My_matrix(self.matrix)

    def transposed_matrix(self):
        """
        @return: транспонировання матрица
        """
        output = []
        for col_ in self.range_col():
            col_new = []
            for row_ in self.range_row():
                col_new.append(self.matrix[row_][col_])
            output.append(col_new)
        return My_matrix(output)

    def matrix_addition(self, new_matrix):
        """
        @param new_matrix: Матрица, которую прибавляем к исходной
        @return: Сумма двух матриц
        """
        if len(new_matrix) == self.row() and len(new_matrix) == self.col():
            for row_ in self.range_row():
                for col_ in self.range_col():
                    self.matrix[row_][col_] += new_matrix[row_][col_]
            return My_matrix(self.matrix)
        else:
            return 'Невозможно сложить матрицы, так как их размеры не совпадают!'

    def number_of_matrix_elements(self):
        """
        @return:
        Количество элементов в матрице
        """
        s = 0
        for i in self.matrix:
            s += len(i)
        return s

    def matrix_size(self):
        """
        @return:
        Возвращает размер матрицы (строки, столбцы)
        """
        return self.row(), self.col()

    def row(self):
        """
        @return:
        Количество строк в матрице
        """
        return len(self.matrix)

    def col(self):
        """
        @return:
        Количество столбцов в матрице
        """
        return len(self.matrix[0])

    def range_row(self):
        """
        @return:
        range(self.line_length)
        """
        return range(self.row())

    def range_col(self):
        """
        @return:
        range(self.col)
        """
        return range(self.col())

    def copy(self):
        """
        Глубокая копия матрицы
        @return:
        Возвращает глубокую копию исходной матрицы
        """
        new_mat = My_matrix(list(copy.deepcopy(self.matrix)))
        return new_mat


if __name__ == '__main__':
    matrix = My_matrix([
        [1, 3, 4, 5],
        [1, 5, 7, 6],
        [3, 4, 6, 7],
        [8, 9, 4, 1]
    ])
