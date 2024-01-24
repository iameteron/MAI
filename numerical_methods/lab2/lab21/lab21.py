import numpy as np
from module21 import *

def f(x):
    return 10**x - 5 * x - 2

def der_f(x):
    return 10**x * np.log(10) - 5

def phi1(x):
    return np.log10(5 * x + 2)

def der_phi1(x):
    return 5 / ((5 * x + 2) * np.log(10))

def phi2(x):
    return (10**x - 2) / 5

def der_phi2(x):
    return 10**x * np.log(10) / 5

eps1 = float(input())
eps2 = float(input())
eps3 = float(input())

a = 0.1
b = 1

x_0 = 0.9

print("Given equation: 10**x - 5*x - 2 = 0 \n")

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

x, k = simple_iteration_method(f, phi1, der_phi1, a, b, eps1)
print(f"Solution from method of simple iteration with accuracy eps1 = {eps1}")
print(f"was found in k = {k} steps \n")
print(f"x = {x} \n")

x, k = simple_iteration_method(f, phi1, der_phi1, a, b, eps2)
print(f"Solution from method of simple iteration with accuracy eps2 = {eps2}")
print(f"was found in k = {k} steps \n")
print(f"x = {x} \n")

x, k = simple_iteration_method(f, phi1, der_phi1, a, b, eps3)
print(f"Solution from method of simple iteration with accuracy eps3 = {eps3}")
print(f"was found in k = {k} steps \n")
print(f"x = {x} \n")