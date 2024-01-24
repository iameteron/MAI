import numpy as np
import math
from LinearAlgebra import *

#module31

def Lagrange_interpolation(func, x, x_nodes):

    n = x_nodes.size
    N = x.size
        
    L = np.zeros(N)
    L_str = ""

    for i in range(n):
        coef_str = ""
        l_i = 1
        denom = 1
        for j in range(n):
            if (i != j):
                l_i *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])

                denom *= (x_nodes[i] - x_nodes[j])
                coef_str += f" * (x - {x_nodes[j]})"

        L += func(x_nodes[i]) * l_i
        L_str += f"+ {func(x_nodes[i]) / denom}" + coef_str + " "
 
    print(f"Lagrange polynomial: \n\n {L_str} \n")

    return L        

def Newton_interpolation(func, x, x_nodes):

    n = x_nodes.size
    N = x.size

    P = np.zeros(N)
    P_str = ""
    coef_str = ""
    for i in range(n):
        p = 1
        for j in range(i):
            p *= (x - x_nodes[j])
        
        f = divided_differences(func, x_nodes[:i + 1])
        P += p * f

        P_str += f" + {f} {coef_str}"
        coef_str += f" * (x - {x_nodes[i]})"

    print(f"Newton polynomial: \n\n {P_str} \n")

    return P

def divided_differences(func, x):

    if (x.size == 1):
        return func(x)

    f1 = divided_differences(func, x[:-1])
    f2 = divided_differences(func, x[1:])

    f = (f2 - f1) / (x[-1] - x[0])

    return f

def error_estimate(M, x_nodes, x_0):

    n = x_nodes.size
    omega = 1
    for i in range(n):
        omega *= abs(x_0 - x_nodes[i])

    x = np.arange(x_nodes[0], x_nodes[-1], 0.1)
    M_max = np.max(abs(M(x)))
    n_fact = math.factorial(n)

    eps_est = M_max * omega / n_fact
    return eps_est


#module32

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
        

    return x_spline, f_spline

#module33

def least_squares(x, y, n):
    N = x.size - 1
    A = np.zeros((n + 1, n + 1))
    b = np.zeros((n + 1))

    for i in range(n + 1):
        for k in range(N + 1):
            b[i] += y[k] * x[k]**i

        for j in range(n + 1):
            for k in range(N + 1):
                A[i][j] += x[k]**(i + j)

    L, U, b = get_LU(A, b)
    a = solve_LU(L, U, b)

    step = 0.01
    x_ls = np.arange(x[0], x[-1] + step, step)
    y_ls = np.zeros(x_ls.size)

    for i in range(n + 1):
        y_ls += a[i] * x_ls**i 

    return x_ls, y_ls

def squared_error(x_ls, y_ls, x, y):
    for i in range(x_ls.size):
        x_ls[i] = round(x_ls[i], 3)

    error = 0
    for i in range(x.size):
        error += (y[i] - y_ls[np.where(x_ls == x[i])])**2

    return error

#module34

def numerical_first_derivative(x, y, x_star):

    i = 0
    for j in range(x.size):
        if(x[j] > x_star):
            i = j - 1 
            break

    y_left  = (y[i] - y[i - 1]) / (x[i] - x[i - 1])
    y_der   = (y[i + 1] - y[i - 1]) / (x[i + 1] - x[i - 1])
    y_right = (y[i + 1] - y[i]) / (x[i + 1] - x[i])

    return y_left, y_der, y_right

def numerical_second_derivative(x, y, x_star):

    i = 0
    for j in range(x.size):
        if(x[j] > x_star):
            i = j - 1 
            break

    y_der = (y[i + 1] - 2 * y[i] + y[i - 1]) / ((x[i + 1] - x[i - 1]) / 2)**2

    return y_der
    
#module35

def rectangle_rule(func, a, b, h):
    x_nodes = np.arange(a, b + h, h)
    
    I = 0
    for i in range(x_nodes.size - 1):
        I += h * func((x_nodes[i] + x_nodes[i + 1]) / 2)
        
    return I

def trapezoid_rule(func, a, b, h):
    x_nodes = np.arange(a, b + h, h)
    
    I = 0
    for i in range(x_nodes.size - 1):
        I += h * (func(x_nodes[i]) + func(x_nodes[i + 1])) / 2
        
    return I

def Simpsons_rule(func, a, b, h):
    x_nodes = np.arange(a, b + h, h)

    I = 0
    for i in range(x_nodes.size - 1):
        x_mean = (x_nodes[i] + x_nodes[i + 1]) / 2 
        I += h * (func(x_nodes[i]) + 4 * func(x_mean) + func(x_nodes[i + 1])) / 6

    return I

def Runge_Rombegr_method(I_h, I_kh, k, p):

    R = - (I_h - I_kh) / ((1 / k)**p - 1)

    return R