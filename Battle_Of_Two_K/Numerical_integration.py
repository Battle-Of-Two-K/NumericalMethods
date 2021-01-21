from sympy import *
import matplotlib.pyplot as plt
import numpy as np


def function(x):
    return (7 * x + 2) / (x * x + 5)


def func_sym():
    x = Symbol('x')
    return (7 * x + 2) / (x * x + 5)


class NumericalIntegration:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class TrapezoidalFormula(NumericalIntegration):  # опять класс-метод (формула)
    def __init__(self, a, b, h):
        """
        Формула трапеций

        Args:
            a: нижний отрезок
            b: верхний отрезок
        """
        super().__init__(a, b)
        self.h = h

    def generator_lists(self):
        """
        Returns:
            list: Возвращает список элементы которого все иксы x, с учётом шага h.
        """
        new_list = []
        i = self.a
        while i <= self.b:
            new_list.append(i)
            i += self.h
        return new_list

    def list_values(self):
        """
        Returns:
            list: Возвращает список, с элементами Y(x) без Y(a) и Y(b) с учётом шага
        """
        n_list = []
        for i in self.generator_lists():
            n_list.append(function(i))
        n_list.pop(0)
        n_list.pop()
        return n_list

    def list_values_a_b(self):
        """
        Returns:
            list: Возвращает список, с элементами Y(x) без Y(a) и Y(b) с учётом шага
        """
        n_list = []
        for i in self.generator_lists():
            n_list.append(function(i))
        return n_list

    def integral(self):
        """
        Returns:
            Возвращает интеграл введённой функции
        """
        x = Symbol('x')
        return integrate(func_sym(), (x, self.a, self.b))

    def n(self):
        """
        Returns:
            Количество равных по длине отрезков
        """
        return int((self.b - self.a) / self.h)

    def table_Y(self):
        """
        Красиво печатает выражение Y(x) = (-4 * x) / (x * x + 5) от Y(a) до Y(b) с учётом шага
        """
        s = self.a
        for i in self.generator_lists():
            print(f'Y({i}): {function(s)}')
            s += self.h

    def summa(self):
        """
        Returns:
            float: Сумму значений Y(x), без элеметнов Y(a) и Y(b)
        """
        s = 0
        for n in self.list_values():
            s += n
        return s

    def t_n(self):
        """
        Returns:
            float: Площадь криволинейной трапеции
        """
        return (self.h / 2) * (function(self.a) + 2 * self.summa() + function(self.b))

    def grafik(self):
        new_h = self.h

        z = np.linspace(-10, 10, 100)
        y = function(z)

        figure, axes = plt.subplots()

        axes.plot(z, y, color='Navy')  # Узнать про linewidth
        axes.scatter(self.generator_lists(), self.list_values_a_b(), color='red')

        axes.grid()

        # axes.scatter(X, Y, color='red')
        axes.set_title(f'Формула трапеций. h = {self.h}')

        figure.set_figwidth(9)
        figure.set_figheight(7)

        axes = plt.gca()
        axes.spines['left'].set_position('center')
        axes.spines['bottom'].set_position('center')
        axes.spines['top'].set_visible(False)
        axes.spines['right'].set_visible(False)

        plt.show()


class SimpsonFormula(NumericalIntegration):  # опять класс-метод (формула)
    def __init__(self, a, b, h, p):
        """
        Args:
            a: нижний предел интегрирования
            b: верхний предел интегрирования
            h: шаг
            p: порядок точности формулы Симпсона
        """
        super().__init__(a, b)
        self.h = h
        self.p = p

    def n(self):
        """
        Returns:
        Количество равных по длине отрезков
        """
        return int((self.b - self.a) / self.h)

    def generator_lists(self):
        """
        Returns:
        Возвращает список элементы которого все иксы x, с учётом шага h.
        """
        new_list = []
        i = self.a
        while i <= self.b:
            new_list.append(i)
            i += self.h
        return new_list

    def table_Y(self):
        """
        Красиво печатает выражение Y(x) = (-4 * x) / (x * x + 5) от Y(a) до Y(b) с учётом шага
        """
        s = self.a
        for i in self.generator_lists():
            print(f'Y({i}): {function(s)}')
            s += self.h

    def list_values(self):
        """
        Returns:
        Возвращает список, с элементами Y(x) без Y(a) и Y(b) с учётом шага
        """
        n_list = []
        for i in self.generator_lists():
            n_list.append(function(i))
        n_list.pop(0)
        n_list.pop()
        return n_list

    def list_values_a_b(self):
        """
        Returns:
        Возвращает список, с элементами Y(x) с учётом шага
        """
        n_list = []
        for i in self.generator_lists():
            n_list.append(function(i))
        return n_list

    def summa_odd(self):
        """
        Returns:
        Сумму нечетных значений Y(x), без элеметнов Y(a) и Y(b)
        """
        result_odd = 0
        result_even = 0
        s = 1
        for i in self.list_values():
            if not s % 2 == 0:
                s += 1
                result_odd += i
            else:
                s += 1
                result_even += i
        return result_odd

    def summa_even(self):
        """
        Returns:
        Сумму четных значений Y(x), без элеметнов Y(a) и Y(b)
        """
        result_odd = 0
        result_even = 0
        s = 1
        for i in self.list_values():
            if not s % 2 == 0:
                s += 1
                result_odd += i
            elif s < len(self.list_values()):
                s += 1
                result_even += i
        return result_even

    def S(self):
        return (self.h / 3) * (function(self.a) + 4 * self.summa_odd() + 2 * self.summa_even() + function(self.b))

    def grafik(self):
        """
        Красиво выводит график
        """
        z = np.linspace(-10, 10, 100)
        y = function(z)

        figure, axes = plt.subplots()

        axes.plot(z, y, color='Navy')  # Узнать про linewidth
        axes.scatter(self.generator_lists(), self.list_values_a_b(), color='red')

        axes.grid()

        # axes.scatter(X, Y, color='red')

        axes.set_title(f'Формула Симпсона. h = {self.h}')

        figure.set_figwidth(9)
        figure.set_figheight(7)

        axes = plt.gca()
        axes.spines['left'].set_position('center')
        axes.spines['bottom'].set_position('center')
        axes.spines['top'].set_visible(False)
        axes.spines['right'].set_visible(False)

        plt.show()
