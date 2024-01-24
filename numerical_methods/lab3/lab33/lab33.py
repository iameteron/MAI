import numpy as np
from module33 import *
import matplotlib.pyplot as plt

def plot_setup():
    plt.figure(figsize=(10, 6))
    plt.grid()
    plt.legend()
    plt.xlabel('x')
    plt.xlabel('f(x)')

x = np.fromstring(input(), dtype=float, sep=' ')
y = np.fromstring(input(), dtype=float, sep=' ')

n1 = 1
x1, y1, a1 = least_squares(x, y, n1)

n2 = 2
x2, y2, a2 = least_squares(x, y, n2)

plot_setup()
plt.scatter(x, y, label='function points')
plt.plot(x1, y1, label='linear polynomial')
plt.plot(x2, y2, label='quadratic polynomial')
plt.legend()
plt.show()

print(f"Least squared method: \n")
print(f"n1 = {n1}: F(x) = {a1[0]} + {a1[1]} * x \n")
print(f"n2 = {n2}: F(x) = {a2[0]} + {a2[1]} * x + {a2[2]} * x^2\n")

print(f"Squared error of a linear polynomial: \n")
print(f"error = {squared_error(x1, y1, x, y)} \n")

print(f"Squared error of a quadratic polynomial: \n")
print(f"error = {squared_error(x2, y2, x, y)} \n")