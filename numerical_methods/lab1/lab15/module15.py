import numpy as np
import math

def sign(x):
    return abs(x) / x

def matrix_norm(A):
    n = A.shape[0]
    norm = 0
    for j in range(n):
        for i in range(j + 1, n):
            norm += A[i][j] ** 2

    return math.sqrt(norm)

def get_QR(A):
    n = A.shape[0]
    Q = np.identity(n)

    for k in range(0, n - 1):
        v = np.zeros(n)
        s = 0
        for i in range(k, n):
            v[i] = A[i][k]
            s += A[i][k] * A[i][k]
        v[k] = A[k][k] + sign(A[k][k]) * math.sqrt(s)

        E = np.identity(n)
        v = v.reshape((3, 1))
        v_T = v.reshape((1 ,3))
        H_k = E - 2 * (v @ v_T) / (v_T @ v) 

        A = H_k @ A
        Q = Q @ H_k

    R = A

    return Q, R

def QR_method(A, eps):
    n = A.shape[0]
    A_k = A.copy()
    k = 0
    Q = np.identity(n)

    A_norm = matrix_norm(A_k) 
    while(A_norm >= eps):
        Q_k, R_k = get_QR(A_k)
        A_k = R_k @ Q_k

        k += 1
        A_norm = matrix_norm(A_k)
        Q = Q @ Q_k

    return np.diagonal(A_k), Q, k
