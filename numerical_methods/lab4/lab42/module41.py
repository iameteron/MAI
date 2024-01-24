import numpy as np

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