import random as rnd
import python_code.methods.matrix.determinant as determinant
import pickle


def det(matrix):
    return determinant.minor_method(matrix)


class Matrix:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], int):
                self.matrix = [[0 for j in range(args[0])] for i in range(args[0])]
            elif isinstance(args[0], list):
                self.matrix = args[0]
            else:
                raise TypeError("Неизвестный тип данных, используйте list")
        elif len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], int):
                self.matrix = [[0 for j in range(args[1])] for i in range(args[0])]
        else:
            raise LookupError("Слишком много аргументов")
        if not self.check_for_equal_len():
            raise LookupError("Строки матрицы имеют разную длину")

    def __getitem__(self, item):
        return self.matrix[item]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __str__(self):
        """Перегрузка строкового представления"""
        out = f'Матрица {self.size}\n'
        for row in self.matrix:
            out += str(row) + '\n'
        return out

    def __add__(self, other):
        """Перегрузка сложения"""
        if isinstance(other, (float, int)):
            matrix = self.matrix.copy()
            for _ in range(self.rows):
                for __ in range(self.columns):
                    matrix[_][__] += other
            return Matrix(matrix)
        elif isinstance(other, Matrix):
            assert self.size == self.size, "Нельзя сложить матрицы разного размера"
            matrix = self.matrix.copy()
            for _ in range(self.rows):
                for __ in range(self.columns):
                    matrix[_][__] += other[_][__]
            return Matrix(matrix)

    def __mul__(self, other):
        """Перегрузка умножения"""
        if isinstance(other, (float, int)):
            matrix = self.matrix.copy()
            for _ in range(self.rows):
                for __ in range(self.columns):
                    matrix[_][__] *= other
            return Matrix(matrix)
        else:
            if self.columns != other.rows:
                raise IndexError("Количество столбцов первой матрицы не совпадает с количеством строк второй")
            matrix = Matrix(self.rows, other.columns).matrix
            for i in range(self.rows):
                for j in range(other.columns):
                    for s in range(self.columns):
                        if self.rows > 1:
                            matrix[i][j] += self.matrix[i][s] * other.matrix[s][j]
                        else:
                            matrix[i][j] += self.matrix[s] * other.matrix[s][j]
            return Matrix(matrix)

    def __neg__(self):
        """Перегрузка унарного минуса"""
        return self * -1

    def __sub__(self, other):
        """Перегрузка вычитания"""
        self + (-other)

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            return self * (1 / other)
        else:
            return self * ~other

    def __invert__(self):
        if det(self) == 0:
            raise ArithmeticError("Невозможно найти обратную матрицу так как определитель равен нулю")
        else:
            return self.complements.T * 1 / det(self)

    def console_display(self):
        """Красиво печатет матрицу в консоль"""
        print(f'Матрица {self.size}'.center(self.columns * (self.max_len_num + 3) - 1))
        print(self.to_pretty_string())

    def check_for_equal_len(self):
        """Провряет равны ли длины строк в матрице"""
        reference = len(self[0])
        for line in self.matrix:
            if len(line) != reference:
                return False
        else:
            return True

    def autofill(self, mode='random', value_range: tuple = None):
        """Автоматическое заполнение матрицы
        Режимы:
            'random' - случайные числа в диапазоне value_range если в value_range int,
                то целые, иныче - не целые (по умолчанию (-10, 10))
            'ones' - приводит матрицу к единичной
            'sequence' - матрица, заполненная числами от 1 до Matrix.rows * Matrix.columns
            'H_grid' - прямая сетка значений (по умолчанию (1, 0, 2))
            'X_grid' - косая сетка значений (по умолчанию (1, 0)"""
        if mode == 'random':
            if value_range:
                assert (value_range[1] - value_range[0] > 0), "В указанном диапазоне нет значений"
                val1, val2 = value_range
            else:
                val1, val2 = -10, 10
            if isinstance(val1, float) or isinstance(val2, float):
                self.matrix = [[rnd.uniform(val1, val2) for __ in range(self.columns)] for _ in range(self.rows)]
            else:
                self.matrix = [[rnd.randint(val1, val2) for __ in range(self.columns)] for _ in range(self.rows)]
        elif mode == 'ones':
            assert self.is_square, "Невозможно составить единичную матрицу изне квадратной матрицы"
            self.matrix = [[1 if _ == __ else 0 for __ in range(self.columns)] for _ in range(self.rows)]
        elif mode == 'H_grid':
            if value_range:
                if len(value_range) == 2:
                    val1, val2 = value_range
                    step = 2
                else:
                    val1, val2, step = value_range
            else:
                val1, val2, step = 1, 0, 2
            self.matrix = [[val1 if bool(_ % step) or bool(__ % step) else val2 for __ in range(self.columns)]
                           for _ in range(self.rows)]
        elif mode == 'X_grid':
            if value_range:
                val1, val2 = value_range
            else:
                val1, val2 = 1, 0
            self.matrix = [[val1 if _ % 2 == __ % 2 else val2 for __ in range(self.columns)] for _ in range(self.rows)]
        elif mode == 'sequence':
            self.matrix = [[1 + _ + __ * self.columns for _ in range(self.columns)] for __ in range(self.rows)]
        else:
            raise AttributeError(f"Неизветный режим {mode}")

    def minor(self, row: int, column: int):
        """Находит минор матрицы по заданой ячейке"""
        out = []
        for row_no in range(self.rows):
            if row_no == row:
                continue
            new_row = []
            for col_no in range(self.columns):
                if col_no == column:
                    continue
                new_row.append(self[row_no][col_no])
            out.append(new_row)
        return Matrix(out)

    def swap_rows(self, row_1: int, row_2: int):
        """Меняет 2 строки местами"""
        new_matrix = self.matrix.copy()
        new_matrix[row_1], new_matrix[row_2] = new_matrix[row_2], new_matrix[row_1]
        return Matrix(new_matrix)

    def swap_columns(self, column_1: int, column_2: int):
        """Меняет два столбца матрицы местами"""
        matrix = self.matrix.copy()
        for _ in range(self.rows):
            matrix[_][column_1], matrix[_][column_2] = matrix[_][column_2], matrix[_][column_1]
        return matrix

    def search_for_max_num_count(self, num=0):
        """Ищет строку с наибольшим количеством указаной величины (по умолчанию 0), если такой нет - вернет 0"""
        counter = self.matrix.count(num)
        max_nums_row_no = 0
        for row_no in range(self.rows):
            if self[row_no].count(num) > counter:
                counter = self[row_no].count(num)
                max_nums_row_no = row_no
        return max_nums_row_no

    def append_row(self, new_row: list):
        """Добавляет новую строку в матрицу"""
        matrix = self.matrix.copy()
        if len(new_row) == self.columns:
            matrix.append(new_row)
            return matrix
        else:
            raise IndexError("Длина новой строки не равна количеству столбцов матрицы")

    def append_column(self, new_column: list):
        """Добавляет новый столбец в матрицу"""
        if len(new_column) != self.rows:
            raise IndexError("Высота нового столбца не равна количеству строк матрицы")
        else:
            matrix = self.matrix.copy()
            for row, new_val in zip(matrix, new_column):
                row.append(new_val)
            return matrix

    def dump_to_file(self, filename: str):
        """Записывает матрицу в файл без потери точности"""
        with open(filename + '.matrix', 'wb') as file:
            pickle.dump(self.matrix, file)

    def load_from_file(self, filename: str):
        """Восстанавливает матрицу из файла"""
        with open(filename + '.matrix', 'rb') as file:
            self.matrix = pickle.load(file)

    def write_to_file(self, filename: str):
        """Записывает матрицу в файл (с потерей точности) в виде таблицы"""
        with open(filename + '.txt', 'w') as file:
            file.write(self.to_pretty_string())

    def read_from_file(self, filename: str):
        """Читает матрицу из файла (из таблицы)"""
        with open(filename + '.txt', 'r') as file:
            data = file.read()
        data = data.replace('_', '').replace(" ", '').split('\n')[1::2]
        new_matrix = []
        for new_row in data:
                new_matrix.append(new_row.split('|')[1:-1])
        new_matrix = new_matrix[:-1]
        for row_no in range(len(new_matrix)):
            for col_no in range(len(new_matrix[row_no])):
                if float(new_matrix[row_no][col_no]) == int(new_matrix[row_no][col_no]):
                    new_matrix[row_no][col_no] = int(new_matrix[row_no][col_no])
                else:
                    new_matrix[row_no][col_no] = float(new_matrix[row_no][col_no])
        self.matrix = new_matrix

    def to_pretty_string(self):
        pretty_string = ' ' + '_' * (self.columns * (self.max_len_num + 3) - 1) + ' \n'
        for row_no in range(self.rows):
            for col_no in range(self.columns):
                pretty_string += f'|{str(round(self.matrix[row_no][col_no], 3)).center(self.max_len_num + 2)}'
            pretty_string += "|\n" + ("|" + "_" * (self.max_len_num + 2)) * self.columns + "|\n"
        return pretty_string

    @property
    def max_len_num(self):
        """Длина максимального строкового представления чисел"""
        container = len(str(round(self[0][0], 3)))
        for _ in self.matrix:
            for __ in _:
                container = max(len(str(round(__, 3))), container)
        return container

    @property
    def complements(self):
        mat = Matrix(self.rows, self.columns)
        mid = mat.matrix
        for i in range(self.columns):
            for j in range(self.rows):
                mid[i][j] = det(self.minor(i, j))
        for i in range(self.columns):
            for j in range(self.rows):
                if bool((i + j) % 2):
                    mid[i][j] = -mid[i][j]
        mat.matrix = mid
        return mat

    @property
    def T(self):
        out = []
        for column_no in range(self.columns):
            new_column = []
            for row_no in range(self.rows):
                new_column.append(self.matrix[row_no][column_no])
            out.append(new_column)
        return Matrix(out)

    @property
    def size(self) -> tuple:
        """Размер матрицы (строки, колонки)"""
        return self.rows, self.columns

    @property
    def rows(self) -> int:
        """Количество строк в матрице"""
        return len(self.matrix)

    @property
    def columns(self) -> int:
        """Количество столбцов в матрице"""
        return len(self.matrix[0])

    @property
    def is_square(self) -> bool:
        """Проверяет, является ли матрица квадратной"""
        return self.columns == self.rows


class Integral:
    ...
