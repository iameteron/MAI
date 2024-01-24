import numpy as np
from module14 import *

n = int(input())
A = np.array([[float(j) for j in input().split()] for i in range(n)])
eps1 = float(input())
eps2 = float(input())
eps3 = float(input())

print(f"matrix A: \n\n {A} \n")

eigen_values, eigen_vectors, k = JacobiMethod(A, eps1)
print(f"Solution form Jacobi method with accuracy eps1 = {eps1}")
print(f"was found in k = {k} steps \n")
print(f"Eigen values: \n {eigen_values} \n")
print(f"Eigen vectors: \n {eigen_vectors} \n")

eigen_values, eigen_vectors, k = JacobiMethod(A, eps2)
print(f"Solution form Jacobi method with accuracy eps2 = {eps2} ")
print(f"was found in k = {k} steps \n")
print(f"Eigen values: \n {eigen_values} \n")
print(f"Eigen vectors: \n {eigen_vectors} \n")

eigen_values, eigen_vectors, k = JacobiMethod(A, eps3)
print(f"Solution form Jacobi method with accuracy eps3 = {eps3} ")
print(f"was found in k = {k} steps \n")
print(f"Eigen values: \n {eigen_values} \n")
print(f"Eigen vectors: \n {eigen_vectors} \n")