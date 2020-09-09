import copy
import pickle
import random as rnd
import warnings

import python_code.methods.matrix.determinant as determinant
import python_code.methods.matrix.gauss as gauss
import python_code.methods.matrix.iterations as iterations


def det(*args, **kwargs):
    return determinant.auto_det(*args, **kwargs)


def solve(matrix, free_column, *args, **kwargs):
    if matrix.is_dominant:
        return iterations.auto_iterate(matrix, free_column, *args, **kwargs)
    else:
        return gauss.gauss_method(matrix, free_column, *args, **kwargs)


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
            raise ValueError("Слишком много аргументов")
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
            matrix = self.copy()
            for _ in range(self.rows):
                for __ in range(self.columns):
                    matrix[_][__] += other
            return Matrix(matrix)
        elif isinstance(other, Matrix):
            if self.size != other.size:
                raise ArithmeticError("Нельзя сложить матрицы разного размера")
            matrix = self.copy()
            for _ in range(self.rows):
                for __ in range(self.columns):
                    matrix[_][__] += other[_][__]
            return Matrix(matrix)

    def __mul__(self, other):
        """Перегрузка умножения"""
        if isinstance(other, (float, int)):
            matrix = self.copy()
            for _ in range(self.rows):
                for __ in range(self.columns):
                    matrix[_][__] *= other
            return Matrix(matrix.matrix)
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

    def autofill(self, mode='random', options: tuple = None):
        """Автоматическое заполнение матрицы
        Режимы:
            'random' - случайные числа в диапазоне options если в options int,
                то целые, иныче - не целые (по умолчанию (-10, 10))
            'ones' - заполняет единицами
            'diagonal_ones' - приводит матрицу к единичной
            'sequence' - матрица, заполненная числами от 1 до Matrix.rows * Matrix.columns
            'H_grid' - прямая сетка значений (по умолчанию (1, 0, 2))
            'X_grid' - косая сетка значений (по умолчанию (1, 0)
            'dominant' - матрица с доминантной диагональю, options как у 'random'
            'exchange' - обменная матрица
            'triple_diagonal' - Трёхдиагональная матрица"""

        def get_options():
            if options:
                if not (options[1] - options[0] > 0):
                    raise IndexError("В указанном диапазоне нет значений")
                return options
            else:
                return -10, 10

        def rnd_generate():
            _val1, _val2 = get_options()
            if isinstance(_val1, float) or isinstance(_val2, float):
                return rnd.uniform(_val1, _val2)
            else:
                return rnd.randint(_val1, _val2)

        if mode == 'random':
            self.matrix = [[rnd_generate() for __ in range(self.columns)] for _ in range(self.rows)]
        elif mode == 'ones':
            self.matrix = [[1 for _ in range(self.columns)] for __ in range(self.rows)]
        elif mode == 'diagonal_ones':
            if not self.is_square:
                raise LookupError("Невозможно составить единичную матрицу из не квадратной матрицы")
            self.matrix = [[1 if _ == __ else 0 for __ in range(self.columns)] for _ in range(self.rows)]
        elif mode == 'H_grid':
            if options:
                if len(options) == 2:
                    val1, val2 = options
                    step = 2
                else:
                    val1, val2, step = options
            else:
                val1, val2, step = 1, 0, 2
            self.matrix = [[val1 if bool(_ % step) or bool(__ % step) else val2 for __ in range(self.columns)]
                           for _ in range(self.rows)]
        elif mode == 'X_grid':
            if options:
                val1, val2 = options
            else:
                val1, val2 = 1, 0
            self.matrix = [[val1 if _ % 2 == __ % 2 else val2 for __ in range(self.columns)] for _ in range(self.rows)]
        elif mode == 'sequence':
            self.matrix = [[1 + _ + __ * self.columns for _ in range(self.columns)] for __ in range(self.rows)]
        elif mode == 'dominant':
            if not self.is_square:
                raise ArithmeticError("Доминантной можно сделать только квадратную матрицу")
            new_matrix = Matrix(self.size[0], self.size[1])
            new_matrix.autofill('random', options)
            for row_no in range(new_matrix.rows):
                for col_no in range(new_matrix.columns):
                    if row_no == col_no:
                        container = 0
                        for col_no_inner in range(new_matrix.columns):
                            if col_no_inner != col_no:
                                container += abs(new_matrix[row_no][col_no_inner])
                        # Гарантия доминации диагонали
                        new_matrix[row_no][col_no] = container + abs(rnd_generate())
                        # Добавление отрицательных значений
                        new_matrix[row_no][col_no] *= 1 if rnd.random() < 1 / self.rows else -1
            self.matrix = new_matrix.copy().matrix
        elif mode == 'exchange':
            if not self.is_square:
                raise ArithmeticError("Обменной можно сделать только квадратную матрицу")
            self.matrix = [[int((_ + __) == self.rows - 1) for _ in range(self.columns)] for __ in range(self.rows)]
        elif mode == 'triple_diagonal':
            self.matrix = [[rnd_generate() if i == j or i - 1 == j or i == j - 1 else 0 for i in range(self.columns)]
                           for j in range(self.rows)]
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
        new_matrix = self.copy()
        new_matrix[row_1], new_matrix[row_2] = new_matrix[row_2], new_matrix[row_1]
        return Matrix(new_matrix)

    def swap_columns(self, column_1: int, column_2: int):
        """Меняет два столбца матрицы местами"""
        matrix = self.copy()
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
        """Добавляет новую строку в матрицу. Меняет исходную матрицу"""
        if len(new_row) == self.columns:
            self.matrix.append(new_row)
        else:
            raise IndexError("Длина новой строки не равна количеству столбцов матрицы")

    def append_column(self, new_column: list):
        """Добавляет новый столбец в матрицу. Меняет исходную матрицу"""
        if len(new_column) != self.rows:
            raise IndexError("Высота нового столбца не равна количеству строк матрицы")
        else:
            for row, new_val in zip(self.matrix, new_column):
                row.append(new_val)

    def pop_column(self, col_no: int) -> list:
        """Удаляет столбец из матрицы. Меняет исходную матрицу"""
        out_col = []
        for row_no in range(self.rows):
            out_col.append(self.matrix[row_no].pop(col_no))
        return out_col

    def pop_row(self, row_no: int) -> list:
        """Удаляет строку из матрицы. Меняет исходную матрицу"""
        return self.matrix.pop(row_no)

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

    def to_pretty_string(self, round_to: int = 8):
        pretty_string = ' ' + '_' * (self.columns * (self.max_len_num + 3) - 1) + ' \n'
        for row_no in range(self.rows):
            for col_no in range(self.columns):
                pretty_string += f'|{str(round(self.matrix[row_no][col_no], round_to)).center(self.max_len_num + 2)}'
            pretty_string += "|\n" + ("|" + "_" * (self.max_len_num + 2)) * self.columns + "|\n"
        return pretty_string

    def copy(self):
        """Функция копирования матрицы (нужно для корректной работы python)"""
        new_mat = Matrix(list(copy.deepcopy(self.matrix)))
        return new_mat

    # В разработке!

    def normal_round(self):
        warnings.warn(message='Данная функция в разработке, может работать некорректно',
                      category=FutureWarning)
        for row_no in range(self.rows):
            for col_no in range(self.columns):
                self.matrix[row_no][col_no] = 0 if round(self.matrix[row_no][col_no], 16) == 0 \
                    else self.matrix[row_no][col_no]

    def triangulate(self):
        """Возвращает триангулированную матрицуц"""

        def mul_row(row, n):
            return [val * n for val in row]

        def subtract_rows(row1, row2):
            return [val1 - val2 for val1, val2 in zip(row1, row2)]

        triangulated_matrix = self.copy()
        for col_no in range(min(triangulated_matrix.columns, triangulated_matrix.rows)):
            for row_no in range(triangulated_matrix.rows - 1, 0, -1):
                if col_no == row_no:
                    break
                try:
                    multiplexed_row = mul_row(triangulated_matrix[row_no - 1],
                                              triangulated_matrix[row_no][col_no] /
                                              triangulated_matrix[row_no - 1][col_no])
                    triangulated_matrix[row_no] = subtract_rows(triangulated_matrix[row_no], multiplexed_row)
                except ZeroDivisionError:
                    continue
        return triangulated_matrix

    def triangulate_to_ones(self):
        """Возвращает триангулированную матрицу с единицами в главной диагонали (возможно и нулями)"""

        def mul_row(row, n):
            return [val * n for val in row]

        matrix = self.copy()
        matrix = matrix.triangulate()
        for row_no in range(matrix.rows):
            for col_no in range(matrix.columns):
                if row_no == col_no:
                    try:
                        matrix.matrix[row_no] = mul_row(matrix[row_no], 1 / matrix[row_no][col_no])
                    except ZeroDivisionError:
                        continue
        return matrix

    @property
    def norma_1(self) -> float:
        """Первая норма матрицы (по строкам)"""
        return max([sum(map(lambda x: abs(x), row)) for row in self.matrix])

    @property
    def norma_2(self) -> float:
        """Вторая норма матрицы (по столбцам)"""
        norma = []
        for col_no in range(self.columns):
            col_value = 0
            for row_no in range(self.rows):
                col_value += abs(self[row_no][col_no])
            norma.append(col_value)
        norma = max(norma)
        return norma

    @property
    def is_dominant(self) -> bool:
        """Определяет является ли диагональ матрицы доминантной"""
        if not self.is_square:
            return False
        for _ in range(self.rows):
            summat = 0
            for __ in range(self.rows):
                if _ == __:
                    continue
                summat += abs(self[_][__])
            if summat > abs(self[_][_]):
                return False
        else:
            return True

    @property
    def max_len_num(self, round_to: int = 8):
        """Длина максимального строкового представления чисел. Для to_pretty_string"""
        container = len(str(round(self[0][0], round_to)))
        for _ in self.matrix:
            for __ in _:
                container = max(len(str(round(__, round_to))), container)
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

    @property
    def is_triple_diagonal(self) -> bool:
        if not self.is_square:
            return False
        for _ in range(self.rows):
            for __ in range(self.columns):
                if not (_ == __ or _ - 1 == __ or _ == __ - 1):
                    if self[_][__] != 0:
                        return False
        else:
            return True


class Integral:
    ...


m = Matrix(10)
m.autofill('triple_diagonal')
m.console_display()
print(m.is_triple_diagonal)