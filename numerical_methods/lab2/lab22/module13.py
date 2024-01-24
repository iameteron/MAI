import numpy as np
from numpy import linalg as LA
from module11 import *

def simple_iterations_method(A, b, eps):
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

    x_cur = beta
    k = 0
    eps_k = eps + 1
    while (eps_k > eps):
        x = beta + Alpha @ x_cur
        k += 1
        eps_k = conv_coef * LA.norm(x - x_cur, np.inf)  
        x_cur = x
        
    return x, k

def Seidel_method(A, b, eps):
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
    D_inv = get_inverse(D)
    Alpha = D_inv @ C
    beta = D_inv @ beta

    Alpha_norm = LA.norm(Alpha, np.inf)
    C_norm = LA.norm(C, np.inf)
    if (Alpha_norm < 1):
        conv_coef = C_norm / (1 - Alpha_norm)
    else: 
        conv_coef = 1

    x_cur = beta
    k = 0
    eps_k = eps + 1
    while (eps_k > eps):
        x = beta + Alpha @ x_cur
        k += 1
        eps_k = conv_coef * LA.norm(x - x_cur, np.inf)  
        x_cur = x
        
    return x, k