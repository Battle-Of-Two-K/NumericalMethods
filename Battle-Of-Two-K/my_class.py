import copy


class My_matrix:
    def __init__(self, list_):
        self.list_ = list_

    def mul_on_num(self, number):
        for row_ in self.range_row():
            for col_ in self.range_col():
                self.list_[row_][col_] *= number
        return My_matrix(self.list_)

    def transposed_matrix(self):
        """
        @return:
        Возвращает транспонированную матрицу
        """
        output = []
        for col_ in self.range_col():
            col_new = []
            for row_ in self.range_row():
                col_new.append(self.list_[row_][col_])
            output.append(col_new)
        return My_matrix(output)

    def number_of_matrix_elements(self):
        """
        @return:
        Количество элементов в матрице
        """
        s = 0
        for i in self.list_:
            s += len(i)
        return s

    def row(self):
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
        new_mat = My_matrix(list(copy.deepcopy(self.list_)))
        return new_mat


m = My_matrix([
    [1, 3, 4, 5],
    [1, 5, 7, 6],
    [3, 4, 6, 7],
    [8, 9, 4, 1]
])

print(m.transposed_matrix())

