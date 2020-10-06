from sympy import symbols
from sympy.plotting import plot

x, y = symbols('x y')
p1 = plot(4 * x*x*x - 2 * y*y*y + 5, show=False)
p2 = plot(x, show=False)
p1.append(p2[0])


p1.show()
