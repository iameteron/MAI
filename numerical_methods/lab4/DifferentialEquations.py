import numpy as np
import matplotlib.pyplot as plt
from LinearAlgebra import *

#module41

def Euler_method(func, a, b, y0, x0, h):

    x = np.arange(a, b + h / 2, h)
    y = np.zeros((y0.size, x.size))
    y[:,0] = y0
    x[0] = x0

    for i in range(x.size - 1):
        y[:, i + 1] = y[:, i] + h * func(y[:, i], x[i])
        
    return x, y

def Runge_Kutta_method(func, a, b, y0, x0, h):

    x = np.arange(a, b + h / 2, h)
    y = np.zeros((y0.size, x.size))
    y[:,0] = y0
    x[0] = x0

    for i in range(x.size - 1):
        K1 = h * func(y[:, i], x[i])
        K2 = h * func(y[:, i] + K1 / 2, x[i] + h / 2)
        K3 = h * func(y[:, i] + K2 / 2, x[i] + h / 2)
        K4 = h * func(y[:, i] + K3, x[i] + h)
        y_del = (K1 + 2 * K2 + 2 * K3 + K4) / 6

        y[:, i + 1] = y[:, i] + y_del 
        
    return x, y

def Adams_method(func, a, b, y0, x0, h):
    
    x = np.arange(a, b + h / 2, h)
    y = np.zeros((y0.size, x.size))
    y[:,0] = y0
    x[0] = x0

    print(x)

    x[:4], y[:,:4] = Runge_Kutta_method(func, a, a + 2 * h, y0, x0, h)

    for i in range(3, x.size - 1):
        y_del = h * (55 * func(y[:, i], x[i]) 
                     - 59 * func(y[:, i - 1], x[i - 1])
                     + 37 * func(y[:, i - 2], x[i - 2]) 
                     - 9 * func(y[:, i - 3], x[i - 3])) / 24
                      
        y[:, i + 1] = y[:, i] + y_del 
        
    return x, y

#module42

def shooting_method(func, a, b, h):
    
    eta1 = 1
    eta2 = 0.8

    phi = lambda y: y[0] - y[1] - 3 

    y002 = 3

    y01 = np.array([eta1, y002])
    x, y1 = Runge_Kutta_method(func, a, b, y01, a, h)
    y02 = np.array([eta2, y002])
    x, y2 = Runge_Kutta_method(func, a, b, y02, a, h)

    y_prev = y1
    y_curr = y2

    eps = 0.001

    eta_prev = eta1
    eta_curr = eta2

    phi_prev = phi(y_prev[:,-1])
    phi_curr = phi(y_curr[:,-1])

    k = 0 
    while(abs(phi_curr) > eps and k < 100):

        k += 1

        eta_next = eta_curr - (eta_curr - eta_prev) / (phi_curr - phi_prev) * phi_curr

        y0 = np.array([eta_next, y002])
        x, y_next = Runge_Kutta_method(func, a, b, y0, a, h)

        phi_prev = phi_curr
        phi_curr = phi(y_next[:,-1])

        eta_prev = eta_curr
        y_prev = y_curr
        eta_curr = eta_next
        y_curr = y_next

    return x, y_curr

def finite_difference_method(func, a, b, h):

    p = lambda x: -(2 * x + 4) / (x * (x + 4))
    q = lambda x: 2 / (x * (x + 4))

    x = np.arange(a, b + h / 2, h)

    A = np.zeros((x.size, x.size))
    b = np.zeros(x.size)

    A[0][0] = 1 / h
    A[0][1] = -1 / h
    b[0] = -3

    A[-1][-2] = 1 / h
    A[-1][-1] = (1 - 1 / h)
    b[-1] = 3

    for i in range(1, x.size - 1):
        A[i][i - 1] = (1 - p(x[i]) * h / 2) / h**2
        A[i][i]     = (-2 + q(x[i]) * h**2) / h**2
        A[i][i + 1] = (1 + p(x[i]) * h / 2) / h**2

    y = sweep_method(A, b)

    return x, y

def Runge_Rombegr_method(I_h, I_kh, k):
        
    p = 1
    R = (I_h - I_kh) / (k**p - 1)

    return R