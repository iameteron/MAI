import numpy as np

def sweep_method(A, b):
    n = A.shape[0]
    A_new = np.zeros((n, n + 1))
    for i in range(n):
        A_new[i] = np.append(A[i], 0)

    P = np.zeros(n)
    Q = np.zeros(n)
    for i in range(0, n):
        P[i] = -A_new[i][i + 1] / (A_new[i][i] + A_new[i][i - 1] * P[i - 1]) 
        Q[i] = (b[i] - A_new[i][i - 1] * Q[i - 1]) / (A_new[i][i] + A_new[i][i - 1] * P[i - 1]) 
    
    x = np.zeros(n + 1)
    for i in range(n - 1, -1, -1):
        x[i] = P[i] * x[i + 1] + Q[i]
                
    return x[:n]

def is_tridiagonal(A):
    n = A.shape[0]
    for i in range(0, n):
        if (i == 0):
            for j in range(2, n):
                if (A[i][j] != 0):
                    return False
        if (i == n - 1):
            for j in range(0, n - 2):
                if (A[i][j] != 0):
                    return False
        else:
            for j in range(0, n - 3):
                if (A[i][(j + i + 2) % n] != 0):
                    return False

    return True