import numpy as np
from module11 import *

n = int(input())
A = np.array([[float(j) for j in input().split()] for i in range(n)])
b = np.array([float(i) for i in input().split()])

print(f"matrix A: \n\n {A} \n")
print(f"vector b: \n\n {b} \n")

L, U = get_LU(A)
print(f"matrix L: \n\n {L} \n")
print(f"matrix U: \n\n {U} \n")
print(f"matrix product L * U: \n\n {L @ U} \n")

x = solve_LU(L, U, b)
print(f"vector x: \n\n {x} \n")

det = get_determinant(A)
print(f"determinant of A: det(A) = {det} \n")

A_inv = get_inverse(A)
print(f"matrix A_inv: \n\n {A_inv} \n")
print(f"matrix product A * A_inv: \n\n {A @ A_inv} \n")