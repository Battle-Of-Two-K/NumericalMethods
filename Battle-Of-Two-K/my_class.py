def addition_of_lists(a, b):
    return [x + y for x, y in zip(a, b)]

def multiplying_list(a, b):
    return [a * i for i in b]

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
        return My_matrix(output)

    # def triangulation(self):
    #     s = 0
    #     new_matrix = []
    #     for i in self.list_:
    #         if s < 2:
    #             m = addition_of_lists(self.list_[s + 1], multiplying_list((-self.list_[s + 1][s] / self.list_[s][s]), self.list_[s]))
    #             new_matrix.append(m)
    #             s += 1
    #     z = self.list_[0]
    #     k = z.append(new_matrix)
    #     return My_matrix(k)

    def triangulation(self):
        first_str = self.list_[0] # 1-я строчка матрицы
        for counter_1 in range(1, len(self.list_)):
            for counter_2 in range(0, 1):
                m = addition_of_lists(self.list_[counter_1], multiplying_list((-self.list_[counter_1][counter_2]), first_str))
                first_str.append(m)


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
    [1, 3, 4, 5],
    [1, 5, 7, 6],
    [3, 4, 6, 7],
    [8, 9, 4, 1]
])

print(m.triangulation())

