import numpy as np
from module41 import *
import matplotlib.pyplot as plt
from LinearAlgebra import *

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