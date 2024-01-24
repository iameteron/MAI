import numpy as np
from module22 import *

def f(x):
    return np.array([x[0]**2 - x[0] + x[1]**2 - 1, x[1] - np.tan(x[0])])

def der_f(x):
    return np.array([[2 * x[0] - 1, 2 * x[1]], 
                     [-1 / np.cos(x[0]), 1]])

def phi(x):
    return np.array([np.arctan(x[1]), np.sqrt(5 / 4 - (x[0] - 1 / 2)**2)])

def der_phi(x):
    return np.array([[0, 1 / (1 + x[1]**2)], 
                     [-(5 / 4 - (x[0] - 1 / 2)**2)**(- 1 / 2), 0]])

eps1 = float(input())
eps2 = float(input())
eps3 = float(input())

x_0 = np.array([0.5, 1.2])

a = (0.7, 0.9)
b = (0.9, 1.1)

print("Given system of equations: \n")
print("x^2 - x + y^2 - 1 = 0")
print("y - tg(x) = 0 \n")

x, k = Newton_method(f, der_f, x_0, eps1)
print(f"Solution from Newton method with accuracy eps1 = {eps1}")
print(f"was found in k = {k} steps \n")
print(f"x = {x} \n")

x, k = Newton_method(f, der_f, x_0, eps2)
print(f"Solution from Newton method with accuracy eps2 = {eps2}")
print(f"was found in k = {k} steps \n")
print(f"x = {x} \n")

x, k = Newton_method(f, der_f, x_0, eps3)
print(f"Solution from Newton method with accuracy eps3 = {eps3}")
print(f"was found in k = {k} steps \n")
print(f"x = {x} \n")

x, k = simple_iteration_method(f, phi, der_phi, a, b, eps1)
print(f"Solution from method of simple iteration with accuracy eps1 = {eps1}")
print(f"was found in k = {k} steps \n")
print(f"x = {x} \n")

x, k = simple_iteration_method(f, phi, der_phi, a, b, eps2)
print(f"Solution from method of simple iteration with accuracy eps2 = {eps2}")
print(f"was found in k = {k} steps \n")
print(f"x = {x} \n")

x, k = simple_iteration_method(f, phi, der_phi, a, b, eps3)
print(f"Solution from method of simple iteration with accuracy eps3 = {eps3}")
print(f"was found in k = {k} steps \n")
print(f"x = {x} \n")