import numpy as np
from module15 import *

n = int(input())
A = np.array([[float(j) for j in input().split()] for i in range(n)])
eps1 = float(input())
eps2 = float(input())
eps3 = float(input())

print(f"matrix A: \n\n {A} \n")

Q, R = get_QR(A)
print(f"QR-decomposition of a matrix A: \n")
print(f"Q = \n {Q} \n")
print(f"R = \n {R} \n")
print(f"Q * R = \n {Q @ R} \n")

eigen_values, eigen_vectors, k = QR_method(A, eps1)
print(f"Solution form QR method with accuracy eps1 = {eps1}")
print(f"was found in k = {k} steps \n")
print(f"Eigen values: \n {eigen_values} \n")
print(f"Eigen vectors: \n {eigen_vectors} \n")

eigen_values, eigen_vectors, k = QR_method(A, eps2)
print(f"Solution form QR method with accuracy eps2 = {eps2} ")
print(f"was found in k = {k} steps \n")
print(f"Eigen values: \n {eigen_values} \n")
print(f"Eigen vectors: \n {eigen_vectors} \n")

eigen_values, eigen_vectors, k = QR_method(A, eps3)
print(f"Solution form QR method with accuracy eps3 = {eps3} ")
print(f"was found in k = {k} steps \n")
print(f"Eigen values: \n {eigen_values} \n")
print(f"Eigen vectors: \n {eigen_vectors} \n")



