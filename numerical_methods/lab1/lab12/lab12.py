import numpy as np
from module12 import *

n = int(input())
A = np.array([[float(j) for j in input().split()] for i in range(n)])
b = np.array([float(i) for i in input().split()])

print(f"matrix A: \n\n {A} \n")
print(f"vector b: \n\n {b} \n")

if is_tridiagonal(A) == True:
    print(f"A is tridiagonal. \nThan apply sweep method \n")
    x = sweep_method(A, b)
    print(f"x = {x} \n")
else: 
    print(f"A is NOT tridiagonal. Use some other method \n")
    