import numpy as np
from module41 import *
import matplotlib.pyplot as plt

def plot_setup():
    plt.figure(figsize=(10, 6))
    plt.grid()
    plt.legend()
    plt.xlabel('x')
    plt.xlabel('f(x)')

def solution(x):
    return np.sin(x - 1) + np.cos(x - 1) / x

def func(y, x):
    return np.array([y[1], (2 / x**2 - 1) * y[0]])

a = float(input())
b = float(input())
x0 = float(input())
y0 = float(input())
y0_der = float(input())
h = float(input())

x = np.arange(a, b + h, h)
y_solution = solution(x)

x, y = Euler_method(func, a, b, np.array([y0, y0_der]), x0, h)
y_euler = y[0,:]

x, y = Runge_Kutta_method(func, a, b, np.array([y0, y0_der]), x0, h)
y_runge_kutta = y[0,:]

x, y = Adams_method(func, a, b, np.array([y0, y0_der]), x0, h)
y_adams = y[0,:]

plot_setup()
plt.scatter(x, y_solution, label='Exact solution')
plt.plot(x, y_euler, label='Euler method')
plt.plot(x, y_runge_kutta, label='Runge-Kutta method')
plt.plot(x, y_adams, label='Adams method')
plt.legend()
plt.show()

x_2h, y_2h = Euler_method(func, a, b, np.array([y0, y0_der]), x0, 2 * h)
y_euler_2h = y_2h[0,:]

x_2h, y_2h = Runge_Kutta_method(func, a, b, np.array([y0, y0_der]), x0, 2 * h)
y_runge_kutta_2h = y_2h[0,:]

x_2h, y_2h = Adams_method(func, a, b, np.array([y0, y0_der]), x0, 2 * h)
y_adams_2h = y_2h[0,:]

R_Eueler = Runge_Rombegr_method(y_euler[::2], y_euler_2h, 2)
R_Runge_kutta = Runge_Rombegr_method(y_runge_kutta[::2], y_runge_kutta_2h, 2)
R_Adams = Runge_Rombegr_method(y_adams[::2], y_adams_2h, 2)

print(f"Errors: \n")
print(f"Euler method: \n R = {R_Eueler} \n")
print(f"Runge-Kutta method: \n R = {R_Runge_kutta} \n")
print(f"Adams method: \n R = {R_Adams}  \n")