import numpy as np
from module31 import *

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