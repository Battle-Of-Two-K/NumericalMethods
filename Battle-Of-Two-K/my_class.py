import copy


class My_matrix:
    def __init__(self, list_):
        self.list_ = list_

    def transposed_matrix(self):
        """
        @return:
        Возвращает транспонированную матрицу
        """
        output = []
        for col_ in self.range_col:
            col_new = []
            for row_ in self.range_line_length:
                col_new.append(self.list_[row_][col_])
            output.append(col_new)
        return output

    @property
    def minor(self, i=None, j=None):
        matrix = copy.deepcopy(self.list_)
        del matrix[i]
        for i in range(self.col - 1):
            del matrix[i][j]
        return matrix

    @property
    def determinant(self):
        """
        @return:
        Возвращает определитель матрицы
        """
        if self.line_length != self.col:
            return None
        if self.line_length == 1:
            return self.list_[0][0]
        sign = 1
        det = 0
        for j in range(self.col):
            det += self.list_[0][j] * sign * self.determinant(self.minor(self, i=0, j=None))
            sign *= -1
        return det

    @property
    def number_of_matrix_elements(self):
        """
        @return:
        Количество элементов в матрице
        """
        s = 0
        for i in self.list_:
            s += len(i)
        return s

    @property
    def line_length(self):
        """
        @return:
        Количество строк в матрице
        """
        return len(self.list_)

    @property
    def col(self):
        """
        @return:
        Количество столбцов в матрице
        """
        return len(self.list_[0])

    @property
    def range_line_length(self):
        """
        @return:
        range(self.line_length)
        """
        return range(self.line_length)

    @property
    def range_col(self):
        """
        @return:
        range(self.col)
        """
        return range(self.col)


m = My_matrix([
    [1, 3, 4],
    [1, 5, 7],
    [3, 4, 6]
])

print(m.determinant())
