import numpy as np
from module42 import *
import matplotlib.pyplot as plt

def plot_setup():
    plt.figure(figsize=(10, 6))
    plt.grid()
    plt.legend()
    plt.xlabel('x')
    plt.xlabel('f(x)')

def solution(x):
    return x**2 + x + 2

def func(y, x):
    return np.array([y[1], 2 * ((x + 2) * y[1] - y[0]) / (x * (x + 4))])

def func1(y, x):
    return np.array([y[1], np.e**x + np.sin(y[0])])

a = 1
b = 2

h = 0.1
x_shooting, y = shooting_method(func, a, b, h)
y_shooting = y[0,:]

h = 0.01
x, y_diff = finite_difference_method(func, a, b, h)

h = 0.1
x_solution = np.arange(a, b + h, h)
y_solution = solution(x_solution)

plot_setup()
plt.scatter(x_solution, y_solution, label='Exact solution')
plt.plot(x_shooting, y_shooting, label='Shooting method')
plt.plot(x, y_diff, label='Finite difference method')
plt.legend()
plt.show()


h = 0.1
x_2h, y_2h = shooting_method(func, a, b, 2 * h)
y_shooting_2h = y_2h[0,:]

h = 0.01
x_2h, y_diff_2h = finite_difference_method(func, a, b, 2 * h)

R_shooting = Runge_Rombegr_method(y_shooting[::2], y_shooting_2h, 2)
R_fin_diff = Runge_Rombegr_method(y_diff[::2], y_diff_2h, 2)

print(f"Errors: \n")
print(f"Shooting method: \n R = {R_shooting} \n")
print(f"Finite difference method: \n R = {R_fin_diff} \n")