import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 2, 100)                     # от -5 до 2 сделать 100 точек
y1 = x**3 + 5*x**2 + 10                         # y1 - тоже много точек

fig, ax = plt.subplots()                        # будет 1 график, на нем:
ax.plot(x, y1, color="blue", label="y(x)")      # функция y1(x), синий, надпись y(x)
ax.set_xlabel("x")                              # подпись у горизонтальной оси х
ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                                     # показывать условные обозначения

plt.show()                                      # показать рисунок
fig.savefig('1.png')                            # сохранить в файл 1.png