class My_matrix:
    def __init__(self, list_):
        self.list_ = list_

    def transposed_matrix(self):
        """
        @return:
        Возвращает транспонированную матрицу
        """
        output = []
        for col_ in self.range_col():
            col_new = []
            for row_ in self.range_line_length():
                col_new.append(self.list_[row_][col_])
            output.append(col_new)
        return output

    def number_of_matrix_elements(self):
        """
        @return:
        Количество элементов в матрице
        """
        s = 0
        for i in self.list_:
            s += len(i)
        return s

    def line_length(self):
        """
        @return:
        Количество строк в матрице
        """
        return len(self.list_)

    def col(self):
        """
        @return:
        Количество столбцов в матрице
        """
        return len(self.list_[0])

    def range_line_length(self):
        """
        @return:
        range(self.line_length)
        """
        return range(self.line_length())

    def range_col(self):
        """
        @return:
        range(self.col)
        """
        return range(self.col())


m = My_matrix([
    [1, 3, 4],
    [1, 5, 7],
    [3, 4, 6]
])

print(m.transposed_matrix())
