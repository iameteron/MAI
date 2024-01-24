
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
sns.set()

x_begin = 0
x_end = 1

y_begin = 0
y_end = 1

h_x = 0.05
h_y = 0.05

def solution(x, y):
    return x**2 + y**2

x = np.arange(x_begin, x_end + h_x, h_x)
y = np.arange(y_begin, y_end + h_y, h_y)

x, y = np.meshgrid(x, y)

z = solution(x, y)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

surf = ax.plot_surface(x, y, z)

plt.show()