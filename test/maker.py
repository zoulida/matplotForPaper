__author__ = 'zoulida'
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 10)
y1, y2 = np.sin(x), np.cos(x)

plt.plot(x, y1, marker='o', mec='r', mfc='w')
plt.plot(x, y2, marker='*', ms=10)
plt.show() 