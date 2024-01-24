import numpy as np
import matplotlib.pyplot as plt
from module31 import *

def func(x):
    return (np.pi / 2 - np.arctan(x)) + x

def der4_func(x):
    return 24 * x * (x**2 - 1) / (x**2 + 1)**4

def plot_setup():
    plt.figure(figsize=(10, 6))
    plt.grid()
    plt.legend()
    plt.xlabel('x')
    plt.xlabel('f(x)')

print("Given function:  f(x) = arcctg(x) + x \n")

x = np.arange(-5, 5, 0.01)

x1_nodes = np.fromstring(input(), dtype=float, sep=' ')
x2_nodes = np.fromstring(input(), dtype=float, sep=' ')
x_star = float(input())

y1_lagrange, y1_star = Lagrange_interpolation(func, x, x1_nodes, x_star)
y1_newton   = Newton_interpolation(func, x, x1_nodes)

plot_setup()
plt.plot(x, func(x), label='function')
plt.plot(x, y1_lagrange, label='lagrange interpolation')
plt.plot(x, y1_newton, label ='newton interpolation')
plt.legend()
plt.show()

y2_lagrange, y2_star = Lagrange_interpolation(func, x, x2_nodes, x_star)
y2_newton   = Newton_interpolation(func, x, x2_nodes)

plot_setup()
plt.plot(x, func(x), label='function')
plt.plot(x, y2_lagrange, label='lagrange interpolation')
plt.plot(x, y2_newton, label ='newton interpolation')
plt.legend()
plt.show()

print(f"At x* = {x_star} interpolation for {x1_nodes}: \n")
print(f"P(x*) = {y1_star} \n")

print(f"At x* = {x_star} interpolation for {x2_nodes}: \n")
print(f"P(x*) = {y2_star} \n")

#err = error_estimate(der4_func, x2_nodes, x_star)
#
#print(f"For interpolation of f(x) error")
#print(f"in the point X* = {x_star} satisfies: \n")
#print(f"|err| <= {err} \n")
