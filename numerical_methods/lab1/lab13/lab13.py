import numpy as np
from module13 import *

n = int(input())
A = np.array([[float(j) for j in input().split()] for i in range(n)])
b = np.array([float(i) for i in input().split()])
eps1 = float(input())
eps2 = float(input())
eps3 = float(input())

print(f"matrix A: \n\n {A} \n")
print(f"vector b: \n\n {b} \n")

x, k = simple_iterations_method(A, b, eps1)
print(f"Solution from simple iterations method with accuracy eps1 = {eps1}")
print(f"x = {x}")
print(f"Was found in k = {k} steps \n")

x, k = Seidel_method(A, b, eps1)
print(f"Solution from Seidel method with accuracy eps1 = {eps1}")
print(f"x = {x}")
print(f"Was found in k = {k} steps \n")

x, k = simple_iterations_method(A, b, eps2)
print(f"Solution from simple iterations method with accuracy eps2 = {eps2}")
print(f"x = {x}")
print(f"Was found in k = {k} steps \n")

x, k = Seidel_method(A, b, eps2)
print(f"Solution from Seidel method with accuracy eps1 = {eps2}")
print(f"x = {x}")
print(f"Was found in k = {k} steps \n")

x, k = simple_iterations_method(A, b, eps3)
print(f"Solution from simple iterations method with accuracy eps3 = {eps3}")
print(f"x = {x}")
print(f"Was found in k = {k} steps \n")

x, k = Seidel_method(A, b, eps3)
print(f"Solution from Seidel method with accuracy eps1 = {eps3}")
print(f"x = {x}")
print(f"Was found in k = {k} steps \n")