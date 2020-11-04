def function(x, y):  # это типа функция из задания?
    return 2 * y - 3 * x * x + 1


class FirstOrderODE:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class EulerMethod(FirstOrderODE):  # если это метод, то почему он класс? лепишь классы по поводу и без повода
    def __init__(self, a, b, x_0, y_0, h):
        """
        Args:
            a (float): левая сторона отрезка
            b (float): правая сторона отрезка
            x_0 (float): точка, в которой известно решение ОДУ
            y_0 (float): значение функции в частном случае при аргументе равном x_0
            h (float): шаг разбиения отрезка
        """
        super().__init__(a, b)
        self.x_0 = x_0
        self.y_0 = y_0
        self.h = h

    def n(self):
        """
        Returns:
           int: Количество отрезков одинаковой длины
        """
        return int((self.b - self.a) / self.h)

    def list_(self):
        """
        Returns:
            list: Возвращает список индесов i
        """
        new_list = []
        for i in range(0, self.n() + 1):
            new_list.append(i)
        return new_list

    def x_i(self):
        """
        Returns:
            list: Возвращает список узлов x_i
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
            list: Возвращает список со значениями функции в узле x_i
        """
        s = self.y_0
        new_list = [s]
        for i in self.x_i():
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
            print("x = {: <4.1f} | y = {: ^10.12f}".format(s, z))
            print('----------------------------------')
            s += self.h
            z += self.h * function(i, z)
        print('\n')


class RungeKuttaMethod(FirstOrderODE):  # еще один класс-метод, даже забавно
    def __init__(self, a, b, x_0, y_0, h):
        super().__init__(a, b)
        self.x_0 = x_0
        self.y_0 = y_0
        self.h = h

    def n(self):
        """
        Returns:
            int: Количество отрезков одинаковой длины
        """
        return int((self.b - self.a) / self.h)

    def list_(self):
        """
        Returns:
            list: Возвращает список индесов i
        """
        new_list = []
        for i in range(0, self.n() + 1):
            new_list.append(i)
        return new_list

    def x_i(self):
        """
        Returns:
            list: Возвращает список узлов x_i
        """
        new_list_ = []
        s = self.x_0
        for i in range(0, self.n() + 1):
            new_list_.append(s)
            s += self.h
        return new_list_

    def y_i(self):
        new_list = []
        s = self.y_0
        for i in self.x_i():
            new_list.append(s)
            s += self.calculation(i, s)
        return new_list

    def y_i_print(self):
        new_list = []
        s = self.y_0
        for i in self.x_i():
            new_list.append(s)
            s += self.calculation_and_print(i, s)
        return new_list

    def calculation(self, x, y):
        k_1 = function(x, y)
        k_2 = function((x + self.h / 2), (y + (self.h / 2) * k_1))
        k_3 = function((x + self.h / 2), (y + (self.h / 2) * k_2))
        k_4 = function((x + self.h), (y + self.h * k_3))
        output = (self.h / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
        return output

    def calculation_and_print(self, x, y):
        k_1 = function(x, y)
        k_2 = function((x + self.h / 2), (y + (self.h / 2) * k_1))
        k_3 = function((x + self.h / 2), (y + (self.h / 2) * k_2))
        k_4 = function((x + self.h), (y + self.h * k_3))
        print('x = {: ^20} | y = {: ^20} | K1 = {: ^20} | K2 = {: ^20} | K3 = {: ^20} | K4 = {: ^20} '
              '|'.format(x, y, k_1, k_2, k_3, k_4))  # динозавры звонили, старое форматировние вернуть просили
        print('-------------------------------------------------------------------------------------------------'
              '--------------------------------------------------------------------')
        output = (self.h / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
        return output
