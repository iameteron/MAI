import numpy as np
from module32 import *
import matplotlib.pyplot as plt

def plot_setup():
    plt.figure(figsize=(10, 6))
    plt.grid()
    plt.legend()
    plt.xlabel('x')
    plt.xlabel('f(x)')

x_star = float(input())
x = np.fromstring(input(), dtype=float, sep=' ')
f = np.fromstring(input(), dtype=float, sep=' ')

x_spline, f_spline, a, b, c, d = cubic_spline(x, f)

plot_setup()
plt.scatter(x, f, label='function points')
plt.plot(x_spline, f_spline, label='cubic spline')
plt.legend()
plt.show()

print("Cubic spline: \n")
for i in range(x.size - 1):
    print(f"On interval [{x[i]}, {x[i + 1]}]")
    print(f"{a[i + 1]} + {b[i + 1]} * (x - {x[i]}) + {c[i + 1]} * (x - {x[i]})^2 + {d[i + 1]} * (x - {x[i]})^3 \n")

print(f"Function value at point x* = {x_star}: \n")
print(f"f(x*) = {f_spline[np.where(x_spline == x_star)]}")