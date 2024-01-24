import numpy as np
from module35 import *

def func(x):
    return x * (2 * x + 3)**(1 / 2)

print(f"Given function:   f(x) = x * (2x + 3)^(1/2) \n")

a = float(input())
b = float(input())
h1 = float(input())
h2 = float(input())

I1_rectangle = rectangle_rule(func, a, b, h1)
I2_rectangle = rectangle_rule(func, a, b, h2)

I1_trapezoid = trapezoid_rule(func, a, b, h1)
I2_trapezoid = trapezoid_rule(func, a, b, h2)

I1_Simpsons = Simpsons_rule(func, a, b, h1)
I2_Simpsons = Simpsons_rule(func, a, b, h2)

print(f"Integral of f(x) from a = {a}, to b = {b} with step h = {h2}: \n")

print(f"Rectangle rule: I = {I2_rectangle}")
print(f"Trapezoid rule: I = {I2_trapezoid}")
print(f"Simpson's rule: I = {I2_Simpsons} \n")

print(f"Integral of f(x) from a = {a}, to b = {b} with step h = {h1}: \n")

print(f"Rectangle rule: I = {I1_rectangle}")
print(f"Trapezoid rule: I = {I1_trapezoid}")
print(f"Simpson's rule: I = {I1_Simpsons} \n")

R_rectangle = Runge_Rombegr_method(I2_rectangle, I1_rectangle, h2 / h1, 2)
R_trapezoid = Runge_Rombegr_method(I2_trapezoid, I1_trapezoid, h2 / h1, 2)
R_Simpsons = Runge_Rombegr_method(I2_Simpsons, I1_Simpsons, h2 / h1, 4)                       

print(f"Runge-Romberg refinement: \n")
print(f"Rectangle rule: R = {I2_rectangle + R_rectangle}")
print(f"Trapezoid rule: R = {I2_trapezoid + R_trapezoid}")
print(f"Simpson's rule: R = {I2_Simpsons + R_Simpsons} \n")

