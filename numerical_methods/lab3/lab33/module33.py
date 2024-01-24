import numpy as np
from LinearAlgebra import *

def least_squares(x, y, n):
    N = x.size - 1
    A = np.zeros((n + 1, n + 1))
    b = np.zeros((n + 1))

    for k in range(n + 1):

        for j in range(N + 1):
            b[k] += y[j] * x[j]**k

        for i in range(n + 1):
            for j in range(N + 1):
                A[k][i] += x[j]**(k + i)

    L, U, b = get_LU(A, b)
    a = solve_LU(L, U, b)

    step = 0.01
    x_ls = np.arange(x[0], x[-1] + step, step)
    y_ls = np.zeros(x_ls.size)

    for i in range(n + 1):
        y_ls += a[i] * x_ls**i 

    return x_ls, y_ls, a

def squared_error(x_ls, y_ls, x, y):
    for i in range(x_ls.size):
        x_ls[i] = round(x_ls[i], 4)

    error = 0
    for i in range(x.size):
        error += (y[i] - y_ls[np.where(x_ls == x[i])])**2

    return error