import numpy as np
import math

def maxNonDiagonal(A):
    n = A.shape[0]
    max = 0
    i_max = -1
    j_max = -1
    for i in range(0, n):
        for j in range(0, n):
            if(i != j):
                if(abs(A[i][j]) > abs(max)):
                        max = A[i][j]
                        i_max = i
                        j_max = j


    return max, i_max, j_max

def normAboveDiagonal(A):
    n = A.shape[0]    
    norm = 0
    for i in range(0, n):
        for j in range(0, i):
            norm += A[i][j] * A[i][j]

    return math.sqrt(norm)
     
def JacobiMethod(A_, eps):
    n = A_.shape[0]
    A = A_.copy()

    norm = normAboveDiagonal(A)
    U = np.identity(n)
    k = 0
    while(norm > eps and k < 100):
        max, i, j = maxNonDiagonal(A)
        k += 1
        if (A[i][i] != A[j][j]):
            phi = math.atan(2 * A[i][j] / (A[i][i] - A[j][j])) / 2
        else:
            phi = math.pi / 4

        U_k = np.identity(n)
        U_k[i][i] =  math.cos(phi) 
        U_k[i][j] = -math.sin(phi)
        U_k[j][i] =  math.sin(phi)
        U_k[j][j] =  math.cos(phi) 

        U_kT = U_k.transpose()
        A = U_kT @ A @ U_k

        U = U @ U_k

        norm = normAboveDiagonal(A)

    return np.diagonal(A), U, k