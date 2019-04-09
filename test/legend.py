__author__ = 'zoulida'
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y1, y2 = np.sin(x), np.cos(x)

plt.plot(x, y1, label='y = sin(x)')
plt.plot(x, y2, label='y = cos(x)')
plt.legend()
plt.show()