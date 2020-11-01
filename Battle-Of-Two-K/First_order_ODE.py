def function(x, y):
    return y - 2 * x * x + 3


class FirstOrderODE:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class EulerMethod(FirstOrderODE):
    def __init__(self, a, b, x_0, y_0, h):
        """
        Args:
            a: левая сторона отрезка
            b: правая сторона отрезка
            x_0: точка, в которой известно решение ОДУ
            y_0: значение функции в частном случае при аргументе равном x_0
            h: шаг разбиения отрезка
        """
        super().__init__(a, b)
        self.x_0 = x_0
        self.y_0 = y_0
        self.h = h

    def n(self):
        """
        Returns:
        Количество отрезков одинаковой длины
        """
        return int((self.b - self.a) / self.h)

    def list_(self):
        """
        Returns:
        Возвращает список индесов i
        """
        new_list = []
        for i in range(0, self.n() + 1):
            new_list.append(i)
        return new_list

    def x_i(self):
        """
        Returns:
        Возвращает список узлов x_i
        """
        new_list_ = []
        s = self.x_0
        for i in range(0, self.n() + 1):
            # print(f'x{i} = {self.x_0}')
            new_list_.append(s)
            s += self.h
        return new_list_

    def y_i(self):
        """
        Returns:
        Возвращает список со значениями функции в узле x_i
        """
        s = self.y_0
        new_list = [s]
        for i in self.x_i():
            # print(f'y{i} = {self.y_0} + {self.h} * {function(i, self.y_0)} = '
            #       f'{self.y_0 + self.h * function(i, self.y_0)}')
            new_list.append(s + self.h * function(i, s))
            s += self.h * function(i, s)
        new_list.pop()
        return new_list

    def print_(self):
        """
        Красивый вывод на экран значений x и y
        """
        s = self.x_0
        z = self.y_0
        print('----------------------------------')
        for i in self.x_i():
            # print(f'x{i} = {s} | y{i} = {z}')
            print("x = {: <4.1f} | y = {: ^10.12f}".format(s, z))
            print('----------------------------------')
            s += self.h
            z += self.h * function(i, z)
        print('\n')
