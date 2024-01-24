import numpy as np

def get_LU(A):
    A_ = A.copy()
    n = A_.shape[0]
    U = np.zeros((n, n))
    L = np.identity(n)

    for k in range(0, n):
        for i in range(k + 1, n):
            mu = A_[i][k] / A_[k][k]
            L[i][k] = mu
            for j in range(k, n):
                A_[i][j] = A_[i][j] - mu * A_[k][j]

    U = A_
    return L, U 

def solve_LU(L, U, b):
    n = L.shape[0]
    z = np.zeros(n)
    for i in range(0, n):
        s = 0
        for j in range(0, i):
            s += L[i][j] * z[j]
        z[i] = b[i] - s 

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i, n):
            s += U[i][j] * x[j]
        x[i] = (z[i] - s) / U[i][i]

    return x

def get_determinant(A):
    n = A.shape[0]
    L, U = get_LU(A)

    det = 1
    for i in range(n):
        det *= U[i][i]

    return det

def get_inverse(A):
    n = A.shape[0]
    A_ = A.copy()

    if get_determinant(A_) == 0:
        return False

    A_inv = np.zeros((n, n))
    B = np.identity(n)

    for k in range(0, n):
        for i in range(k + 1, n):
            mu = A_[i][k] / A_[k][k]
            for j in range(0, n):
                A_[i][j] = A_[i][j] - mu * A_[k][j]
                B[i][j] = B[i][j] - mu * B[k][j]

    for k in range(0, n):
        for i in range(n - 1, -1, -1):
            s = 0
            for j in range(i, n):
                s += A_[i][j] * A_inv[j][k]
            A_inv[i][k] = (B[i][k] - s) / A_[i][i]

    return A_inv