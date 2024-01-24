import numpy as np
from LinearAlgebra import *

def cubic_spline(x, f):
    
    n = x.size - 1

    h = np.zeros(n + 1)
    for i in range(1, n + 1):
        h[i] = x[i] - x[i - 1]

    A = np.zeros((n - 1, n - 1))
    b = np.zeros(n - 1)

    A[0][0] = 2 * (h[1] + h[2])
    A[0][1] = h[2]
    b[0] = 3 * ((f[2] - f[1]) / h[2] - (f[1] - f[0]) / h[1])

    A[n - 2][n - 3] = h[n - 1]
    A[n - 2][n - 2] = 2 * (h[n - 1] + h[n])
    b[n - 2] = 3 * ((f[n] - f[n - 1]) / h[n] - (f[n - 1] - f[n - 2]) / h[n - 1])

    for i in range(1, n - 2):
        A[i][i - 1] = h[i + 1]
        A[i][i] = 2 * (h[i + 2] + h[i + 1])
        A[i][i + 1] = h[i + 2]
        b[i] = 3 * ((f[i + 2] - f[i + 1]) / h[i + 2] - (f[i + 1] - f[i]) / h[i + 1])

    c = np.zeros(n + 1)
    c[2:] = sweep_method(A, b)

    a = np.zeros(n + 1)
    b = np.zeros(n + 1)
    d = np.zeros(n + 1)

    a[n] = f[n - 1]
    b[n] = (f[n] - f[n - 1]) / h[n] - 2 / 3 * h[n] * c[n]
    d[n] = -c[n] / (3 * h[n])

    for i in range(1, n):
        a[i] = f[i - 1]
        b[i] = (f[i] - f[i - 1]) / h[i] - 1 / 3 * h[i] * (c[i + 1] + 2 * c[i])
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    k = 100
    f_spline = np.zeros(n * k)
    x_spline = np.zeros(n * k)
    for i in range(1, n + 1):
        x_spline[(i - 1) * k: i * k] = np.linspace(x[i - 1], x[i], k, endpoint=False)
        x_del = x_spline[(i - 1) * k: i * k] - x[i - 1]
        f_spline[(i - 1) * k: i * k] = a[i] + b[i] * x_del + c[i] * x_del**2 + d[i] * x_del**3 
        

    return x_spline, f_spline, a, b, c, d