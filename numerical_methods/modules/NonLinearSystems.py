import numpy as np
from numpy import linalg as LA
from LinearAlgebra import *

#module21

def Newton_method(f, der_f, x_0, eps):

    if(f(x_0) * der_f(x_0) <= 0):
        return
    
    k = 0
    x_prev = x_0
    norm = eps + 1
    while(norm > eps and k < 100):
        k += 1
        x_curr = x_prev - f(x_prev) / der_f(x_prev)
        
        norm = abs(x_curr - x_prev)
        x_prev = x_curr

    return x_curr, k

def simple_iteration_method(f, phi, der_phi, a, b, eps):

    x = np.linspace(a, b, 100)
    q = max(der_phi(x))

    if (q >= 1):
        return

    k = 0
    x_prev = (a + b) / 2
    norm = eps + 1
    while(norm > eps and k < 100):
        k += 1
        x_curr = phi(x_prev)

        norm = abs(x_curr - x_prev)
        x_prev = x_curr

    return x_curr, k

#module22

def Newton_method(f, der_f, x_0, eps):
    
    k = 0
    x_prev = x_0
    norm = eps + 1
    while(norm > eps and k < 100):
        k += 1
        L, U, b = get_LU(der_f(x_prev), -f(x_prev))
        x_del = solve_LU(L, U, b)
        x_curr = x_prev + x_del

        norm = LA.norm(x_curr - x_prev)
        x_prev = x_curr

    return x_curr, k
        

def simple_iteration_method(f, phi, der_phi, a, b, eps):

    x = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    q = LA.norm(der_phi(x), np.inf)

    if (q >= 1):
        return

    k = 0
    x_prev = x
    norm = eps + 1
    while(norm > eps and k < 100):
        k += 1
        x_curr = phi(x_prev)

        norm = LA.norm(x_curr - x_prev)
        x_prev = x_curr

    return x_curr, k