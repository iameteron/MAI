import numpy as np
from numpy import linalg as LA
from module11 import *
from module13 import *

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

    print(f"max||phi'(x)|| = {q} \n")

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