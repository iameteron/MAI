import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
sns.set()

import sys 
sys.path

sys.path.insert(0, r"c:\Users\никита\Desktop\учеба\чм\modules")

import LinearAlgebra

x_begin = 0
x_end = lambda mu_1: np.pi * mu_1 / 2

y_begin = 0
y_end = lambda mu_2: np.pi * mu_2 / 2

t_begin = 0
t_end = 2

a = 1

mu = [(1, 1), (2, 1), (1, 2)] 

mu_1, mu_2 = mu[0]

h_x = 0.1
h_y = 0.1
tau = 0.01

def solution(x, y, t, mu_1, mu_2, a=1):
    return np.cos(mu_1 * x) * np.cos(mu_2 * y) * np.exp(-(mu_1**2 + mu_2**2) * a * t)

x = np.arange(x_begin, x_end(mu_1) + h_x, h_x)
y = np.arange(y_begin, y_end(mu_2) + h_y, h_y)
t = np.arange(t_begin, t_end + tau, tau)

y, x = np.meshgrid(y, x)

def phi_3(y, t, mu_1, mu_2, a=1):
    return np.cos(mu_2 * y) * np.exp(-(mu_1**2 + mu_2**2) * a * t)

def phi_4(y, t, mu_1, mu_2, a=1):
    return 0

def phi_1(x, t, mu_1, mu_2, a=1):
    return np.cos(mu_1 * x) * np.exp(-(mu_1**2 + mu_2**2) * a * t)

def phi_2(x, t, mu_1, mu_2, a=1):
    return 0

def psi(x, y, mu_1, mu_2, a=1):
    return np.cos(mu_1 * x) * np.cos(mu_2 * y)

def fractional_steps_scheme(x_begin, x_end, y_begin, y_end, t_begin, t_end,
                                 h_x, h_y, tau, mu_1, mu_2, a=1):
                                 
    x = np.arange(x_begin, x_end(mu_1) + h_x, h_x)
    y = np.arange(y_begin, y_end(mu_2) + h_y, h_y)
    t = np.arange(t_begin, t_end + tau, tau)

    u = np.zeros((x.size, y.size, t.size))
    
    for i in range(x.size):
        for j in range(y.size):
            u[i, j, 0] = psi(x[i], y[j], mu_1, mu_2)

    for k in range(1, t.size):

        u_half = np.zeros((x.size, y.size))
        
        u[:, 0, k] = phi_1(x, t[k], mu_1, mu_2)
        u[:, -1, k] = phi_2(x, t[k], mu_1, mu_2)
        u[0, :, k] = phi_3(y, t[k], mu_1, mu_2)
        u[-1, :, k] = phi_4(y, t[k], mu_1, mu_2)

        u_half[:, 0] = phi_1(x, t[k] - tau / 2, mu_1, mu_2)
        u_half[:, -1] = phi_2(x, t[k] - tau / 2, mu_1, mu_2)
        u_half[0, :] = phi_3(y, t[k] - tau / 2, mu_1, mu_2)
        u_half[-1, :] = phi_4(y, t[k] - tau / 2, mu_1, mu_2)

        for j in range(1, y.size - 1):
            A = np.zeros((x.size - 2, x.size - 2))
            b = np.zeros((x.size - 2))

            A[0, 0] = h_x**2 + 2 * a * tau
            A[0, 1] = -a * tau
            for ind in range(1, x.size - 3):
                A[ind, ind - 1] = -a * tau
                A[ind, ind] = h_x**2 + 2 * a * tau
                A[ind, ind + 1] = -a * tau
            A[-1, -2] = -a * tau
            A[-1, -1] = h_x**2 + 2 * a * tau

            for i in range(1, x.size - 1):
                b[i - 1] = u[i, j, k - 1] * h_x**2
            b[0] -= (-a * tau) * phi_3(y[j], t[k] - tau / 2, mu_1, mu_2)
            b[-1] -= (-a * tau) * phi_4(y[j], t[k] - tau / 2, mu_1, mu_2)
            
            u_half[1:-1, j] = LinearAlgebra.sweep_method(A, b)
        
        for i in range(1, x.size - 1):
            A = np.zeros((y.size - 2, y.size - 2))
            b = np.zeros((y.size - 2))

            A[0, 0] = h_y**2 + 2 * a * tau
            A[0, 1] = -a * tau
            for ind in range(1, y.size - 3):
                A[ind, ind - 1] = -a * tau
                A[ind, ind] = h_y**2 + 2 * a * tau
                A[ind, ind + 1] = -a * tau
            A[-1, -2] = -a * tau
            A[-1, -1] = h_y**2 + 2 * a * tau

            for j in range(1, y.size - 1):
                b[j - 1] = u_half[i, j] * h_y**2
            b[0] -= (-a * tau) * phi_1(x[i], t[k], mu_1, mu_2)
            b[-1] -= (-a * tau) * phi_2(x[i], t[k], mu_1, mu_2)

            u[i, 1:-1, k] = LinearAlgebra.sweep_method(A, b)

    return u

def alternating_directions_scheme(x_begin, x_end, y_begin, y_end, t_begin, t_end,
                                  h_x, h_y, tau, mu_1, mu_2, a=1):
                                 
    x = np.arange(x_begin, x_end(mu_1) + h_x, h_x)
    y = np.arange(y_begin, y_end(mu_2) + h_y, h_y)
    t = np.arange(t_begin, t_end + tau, tau)

    u = np.zeros((x.size, y.size, t.size))
    
    for i in range(x.size):
        for j in range(y.size):
            u[i, j, 0] = psi(x[i], y[j], mu_1, mu_2)

    for k in range(1, t.size):

        u[:, 0, k] = phi_1(x, t[k], mu_1, mu_2)
        u[:, -1, k] = phi_2(x, t[k], mu_1, mu_2)
        u[0, :, k] = phi_3(y, t[k], mu_1, mu_2)
        u[-1, :, k] = phi_4(y, t[k], mu_1, mu_2)

        u_half = np.zeros((x.size, y.size))
        
        u_half[:, 0] = phi_1(x, t[k] - tau / 2, mu_1, mu_2)
        u_half[:, -1] = phi_2(x, t[k] - tau / 2, mu_1, mu_2)
        u_half[0, :] = phi_3(y, t[k] - tau / 2, mu_1, mu_2)
        u_half[-1, :] = phi_4(y, t[k] - tau / 2, mu_1, mu_2)

        for j in range(1, y.size - 1):
            A = np.zeros((x.size - 2, x.size - 2))
            b = np.zeros((x.size - 2))

            A[0, 0] = 2 * h_x**2 * h_y**2 + 2 * a * tau * h_y**2
            A[0, 1] = -a * tau * h_y**2
            for ind in range(1, x.size - 3):
                A[ind, ind - 1] = -a * tau * h_y**2
                A[ind, ind] = 2 * h_x**2 * h_y**2 + 2 * a * tau * h_y**2
                A[ind, ind + 1] = -a * tau * h_y**2
            A[-1, -2] = -a * tau * h_y**2
            A[-1, -1] = 2 * h_x**2 * h_y**2 + 2 * a * tau * h_y**2

            for i in range(1, x.size - 1):
                b[i - 1] = (
                    u[i, j - 1, k - 1] * a * tau * h_x**2
                    + u[i, j, k - 1] * (2 * h_x**2 * h_y**2 - 2 * a * tau * h_x**2)
                    + u[i, j + 1, k - 1] * a * tau * h_x**2
                )
            b[0] -= (-a * tau * h_y**2) * phi_3(y[j], t[k] - tau / 2, mu_1, mu_2)
            b[-1] -= (-a * tau * h_y**2) * phi_4(y[j], t[k] - tau / 2, mu_1, mu_2)

            u_half[1:-1, j] = LinearAlgebra.sweep_method(A, b)

        for i in range(1, x.size - 1):
            A = np.zeros((y.size - 2, y.size - 2))
            b = np.zeros((y.size - 2))

            A[0, 0] = 2 * h_x**2 * h_y**2 + 2 * a * tau * h_x**2
            A[0, 1] = -a * tau * h_x**2
            for ind in range(1, y.size - 3):
                A[ind, ind - 1] = -a * tau * h_x**2
                A[ind, ind] = 2 * h_x**2 * h_y**2 + 2 * a * tau * h_x**2
                A[ind, ind + 1] = -a * tau * h_x**2
            A[-1, -2] = -a * tau * h_x**2
            A[-1, -1] = 2 * h_x**2 * h_y**2 + 2 * a * tau * h_x**2

            for j in range(1, y.size - 1):
                b[j - 1] = (
                    u_half[i - 1, j] * a * tau * h_y**2
                    + u_half[i, j] * (2 * h_x**2 * h_y**2 - 2 * a * tau * h_y**2)
                    + u_half[i + 1, j] * a * tau * h_y**2
                )
            b[0] -= (-a * tau * h_x**2) * phi_1(x[i], t[k], mu_1, mu_2)
            b[-1] -= (-a * tau * h_x**2) * phi_2(x[i], t[k], mu_1, mu_2)

            u[i, 1:-1, k] = LinearAlgebra.sweep_method(A, b)
            
    return u

def get_analytical_solution(x_begin, x_end, y_begin, y_end, t_begin, t_end, h_x, h_y, tau, mu_1, mu_2):

    x = np.arange(x_begin, x_end(mu_1) + h_x, h_x)
    y = np.arange(y_begin, y_end(mu_2) + h_y, h_y)
    t = np.arange(t_begin, t_end + tau, tau)

    u = np.zeros((x.size, y.size, t.size))
    for i in range(x.size):
        for j in range(y.size):
            for k in range(t.size):
                u[i, j, k] = solution(x[i], y[j], t[k], mu_1, mu_2)
    
    return u

u_exact = get_analytical_solution(x_begin, x_end, y_begin, y_end, t_begin, t_end, h_x, h_y, tau, mu_1, mu_2)

u_alternating = alternating_directions_scheme(x_begin, x_end, y_begin, y_end, t_begin, t_end,
                                              h_x, h_y, tau, mu_1, mu_2, a=1)


u_fractional = fractional_steps_scheme(x_begin, x_end, y_begin, y_end, t_begin, t_end,
                                       h_x, h_y, tau, mu_1, mu_2, a=1)


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})


for j in range(t.size):

    ax.clear()
    ax.set_zlim(0, 1)
    ax.plot_surface(x, y, u_fractional[:, :, j])
    ax.plot_surface(x, y, u_alternating[:, :, j])
    ax.plot_surface(x, y, u_exact[:, :, j], color='red')
    
    plt.pause(0.05)