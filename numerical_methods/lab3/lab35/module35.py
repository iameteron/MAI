import numpy as np

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
    x_nodes = np.arange(a, b + 2 * h, 2 * h)

    I = 0
    for i in range(x_nodes.size - 1):
        x_mean = (x_nodes[i] + x_nodes[i + 1]) / 2 
        I += h * (func(x_nodes[i]) + 4 * func(x_mean) + func(x_nodes[i + 1])) / 3

    return I

def Runge_Rombegr_method(I_kh, I_h, k, p):

    R = (I_kh - I_h) / ((1 / k)**p - 1)

    return R