import numpy as np
from numpy import linalg as LA
import math

# lab11

def get_LU(A_, b_):
    A = A_.copy()
    b = b_.copy()
    n = A.shape[0]
    U = np.zeros((n, n))
    L = np.identity(n)

    for k in range(0, n):
        if(A[k][k] == 0):
            for i in range(k, n):
                if(A[i][k] != 0):
                    A[[k, i]] = A[[i, k]]
                    b[k], b[i] = b[i], b[k]
                    break
        for i in range(k + 1, n):
            mu = A[i][k] / A[k][k]
            L[i][k] = mu
            for j in range(k, n):
                A[i][j] = A[i][j] - mu * A[k][j]

    U = A

    return L, U, b

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
    b = np.zeros(n)
    L, U, b = get_LU(A, b)

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


# lab12

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


# lab13

def simple_iterations_method(A, b, eps, x_cur=[], c=0):
    n = A.shape[0]

    beta = np.zeros(n)
    Alpha = np.zeros((n, n))
    for i in range(0, n):
        beta[i] = b[i] / A[i][i]
        for j in range(0, n):
            Alpha[i][j] = -A[i][j] / A[i][i]
            if (i == j):
                Alpha[i][i] = 0

    Alpha_norm = LA.norm(Alpha, np.inf)
    if (Alpha_norm < 1):
        conv_coef = Alpha_norm / (1 - Alpha_norm)
    else:
        conv_coef = 1

    if len(x_cur) == 0:
        x_cur = beta

    k = 0
    eps_k = eps + 1
    while (eps_k > eps):
        x = (1 - c) * (beta + Alpha @ x_cur) + c * x_cur
        k += 1
        eps_k = conv_coef * LA.norm(x - x_cur, np.inf)
        x_cur = x

    return x, k


def Seidel_method(A, b, eps, x_cur=[], c=0):
    n = A.shape[0]

    beta = np.zeros(n)
    Alpha = np.zeros((n, n))
    for i in range(0, n):
        beta[i] = b[i] / A[i][i]
        for j in range(0, n):
            Alpha[i][j] = -A[i][j] / A[i][i]
            if (i == j):
                Alpha[i][i] = 0

    B = np.zeros((n, n))
    C = np.zeros((n, n))
    E = np.identity(n)

    for i in range(0, n):
        for j in range(0, n):
            if (j >= i):
                C[i][j] = Alpha[i][j]
            else:
                B[i][j] = Alpha[i][j]

    D = E - B
    D_inv = np.linalg.inv(D)
    Alpha = D_inv @ C
    beta = D_inv @ beta

    Alpha_norm = LA.norm(Alpha, np.inf)
    C_norm = LA.norm(C, np.inf)
    if (Alpha_norm < 1):
        conv_coef = C_norm / (1 - Alpha_norm)
    else:
        conv_coef = 1

    if len(x_cur) == 0:
        x_cur = beta

    k = 0
    eps_k = eps + 1
    while (eps_k > eps):
        x = (1 - c) * (beta + Alpha @ x_cur) + c * x_cur
        k += 1
        eps_k = conv_coef * LA.norm(x - x_cur, np.inf)
        x_cur = x

    return x, k


# lab14

def maxNonDiagonal(A):
    n = A.shape[0]
    max = 0
    i_max = -1
    j_max = -1
    for i in range(0, n):
        for j in range(0, n):
            if (i != j):
                if (abs(A[i][j]) > abs(max)):
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
    while (norm > eps and k < 100):
        max, i, j = maxNonDiagonal(A)
        k += 1
        if (A[i][i] != A[j][j]):
            phi = math.atan(2 * A[i][j] / (A[i][i] - A[j][j])) / 2
        else:
            phi = math.pi / 4

        U_k = np.identity(n)
        U_k[i][i] = math.cos(phi)
        U_k[i][j] = -math.sin(phi)
        U_k[j][i] = math.sin(phi)
        U_k[j][j] = math.cos(phi)

        U_kT = U_k.transpose()
        A = U_kT @ A @ U_k

        U = U @ U_k

        norm = normAboveDiagonal(A)

    return np.diagonal(A), U, k

# lab15

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
