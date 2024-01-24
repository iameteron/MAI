import numpy as np
import math

def Lagrange_interpolation(func, x, x_nodes, x_star):

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

    return L, L[np.where(np.isclose(x, x_star))]        

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

def error_estimate(M, x_nodes, x_star):

    n = x_nodes.size
    omega = 1
    for i in range(n):
        omega *= abs(x_star - x_nodes[i])

    x = np.arange(x_nodes[0], x_nodes[-1], 0.001)
    M_max = np.max(abs(M(x)))
    n_fact = math.factorial(n)

    eps_est = M_max * omega / n_fact

    return eps_est