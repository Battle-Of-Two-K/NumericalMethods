import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(-5, 5, 100)
y = x**3 - 2*x**2 + 3*x - 4

ax.plot(x, y)

plt.show()