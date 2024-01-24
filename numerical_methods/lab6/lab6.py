import sys 
sys.path

sys.path.insert(0, r"c:\Users\никита\Desktop\учеба\чм\modules")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
sns.set()

from LinearAlgebra import *
a = 1

x_begin = 0
x_end = np.pi

t_begin = 0
t_end = 10

h = 0.01
tau = h / (1.01 * a)
sigma = a**2 * tau**2 / h**2

def check_sigma(sigma):
    res = True if sigma <= 1 else False
    #assert res == True
    return res

check_sigma(sigma)

def solution(x, t, a=1):
    u = np.sin(x - a * t) + np.cos(x + a * t)
    return u 

def phi_0(t, a=1):
    return 0

def phi_1(t, a=1):
    return 1
    
def psi_1(x, a=1):
    return np.sin(x) + np.cos(x)

def psi_2(x, a=1):
    return -a * (np.sin(x) + np.cos(x))

def dd_psi_1(x, a=1):
    return - (np.sin(x) + np.cos(x))

def get_initial_values(x_begin, x_end, h, tau, psi_1, psi_2, dd_psi_2, order):

    x = np.arange(x_begin, x_end + h, h)
    u = np.zeros((2, x.size))

    u[0, :] = psi_1(x)

    if order == 1:
        u[1, :] = psi_1(x) + psi_2(x) * tau

    if order == 2:
        u[1, :] = psi_1(x) + psi_2(x) * tau + a**2 * tau**2 * dd_psi_1(x) / 2

    return u

def get_boundary_values(u, h, sigma, type):

    if type == (2, 1):
        u_0 = u[-1, 1] / (1 + h)
        u_N = u[-1, -2] / (1 - h)

    if type == (3, 2):
        u_0 = (-4 * u[-1, 1] + u[-1, 2]) / (-3 - 2 * h)
        u_N = (-u[-1, -3] + 4 * u[-1, -2]) / (3 - 2 * h)

    if type == (2, 2):
        u_0 = (u[-1, 1] + u[-2, 0] / sigma - u[-3, 0] / (2 * sigma)) / (1 + h + 1 / (2 * sigma))
        u_N = (u[-1, -2] + u[-2, -1] / sigma - u[-3, -1] / (2 * sigma)) / (1 - h + 1 / (2 * sigma))

    return u_0, u_N

def get_boundary_coefficients(u, h, sigma, type):

    A = np.zeros((2, 2))
    b = np.zeros(2)

    if type == (2, 1):

        A[0, 0] = (1 + 2 * sigma - sigma / (1 + h))
        A[0, 1] = -sigma
        A[-1, -2] = -sigma
        A[-1, -1] = (1 + 2 * sigma - sigma / (1 - h))
        b[0] = 2 * u[-1, 1] - u[-2, 1]
        b[-1] = 2 * u[-1, -2] - u[-2, -2]

    if type == (3, 2):
        
        A[0, 0] = (-3 - 2 * h) * (1 + 2 * sigma) + 4 * sigma
        A[0, 1] = -sigma + (3 + 2 * h) * sigma
        A[-1, -2] = -(3 - 2 * h) * sigma + sigma
        A[-1, -1] = (3 - 2 * h) * (1 + 2 * sigma) - 4 * sigma
        b[0] = (-3 - 2 * h) * (2 * u[-1, 1] - u[-2, 1])
        b[-1] = (3 - 2 * h) * (2 * u[-1, -2] - u[-2, -2])

    if type == (2, 2):

        A[0, 0] = (1 + 2 * sigma) * (1 + h + 1 / (2 * sigma)) - sigma
        A[0, 1] = -sigma * (1 + h + 1 / (2 * sigma))
        A[-1, -2] = -sigma * (1 - h + 1 / (2 * sigma))
        A[-1, -1] = (1 + 2 * sigma) * (1 - h + 1 / (2 * sigma)) - sigma
        b[0] = (1 + h + 1 / (2 * sigma)) * (2 * u[-1, 1] - u[-2, 1]) + u[-1, 0] - u[-2, 0] / 2
        b[-1] = (1 - h + 1 / (2 * sigma)) * (2 * u[-1, -2] - u[-2, -2]) + u[-1, -1] - u[-2, -1] / 2


    return A[0, 0], A[0, 1], A[-1, -2], A[-1, -1], b[0], b[-1]

def get_analytical_solution(x_begin, x_end, t_begin, t_end, h, tau, a):

    x = np.arange(x_begin, x_end + h, h)
    t = np.arange(t_begin, t_end + tau, tau)

    u = np.zeros((t.size, x.size))
    for j in range(x.size):
        for k in range(t.size):
            u[k, j] = solution(x[j], t[k], a)
    
    return u

u_exact = get_analytical_solution(x_begin, x_end, t_begin, t_end, h, tau, a)

def explicit_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, psi_1, psi_2, dd_psi_2, order, type):

    sigma = a**2 * tau**2 / h**2
    x = np.arange(x_begin, x_end + h, h)
    t = np.arange(t_begin, t_end + tau, tau)
    u = np.zeros((t.size, x.size))

    u[0:2, :] = get_initial_values(x_begin, x_end, h, tau, psi_1, psi_2, dd_psi_2, order)

    for k in range(1, t.size - 1):

        u[k + 1, 1:-1] = sigma * u[k, 0:-2] + 2 * (1 - sigma) * u[k, 1:-1] + sigma * u[k, 2:] - u[k - 1, 1:-1]
        u[k + 1, 0], u[k + 1, -1] = get_boundary_values(u[k - 1:k + 2, :], h, sigma, type)
            
    return u

def implicit_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, psi_1, psi_2, dd_psi_1, order, type):

    sigma = a**2 * tau**2 / h**2
    x = np.arange(x_begin, x_end + h, h)
    t = np.arange(t_begin, t_end + tau, tau)
    u = np.zeros((t.size, x.size))

    u[0:2, :] = get_initial_values(x_begin, x_end, h, tau, psi_1, psi_2, dd_psi_1, order)

    for k in range(1, t.size - 1):
        
        A = np.zeros((x.size - 2, x.size - 2))

        for i in range(1, (x.size - 2) - 1):
            A[i, i - 1] = -sigma
            A[i, i] = 1 + 2 * sigma
            A[i, i + 1] = -sigma
        
        b = np.zeros(x.size - 2)
        b[1:-1] = 2 * u[k, 2:-2]  - u[k - 1, 2:-2]

        A[0, 0], A[0, 1], A[-1, -2], A[-1, -1], b[0], b[-1] = get_boundary_coefficients(u[k - 1: k + 1, :], h, sigma, type)

        u[k + 1, 1:-1] = sweep_method(A, b)
        u[k + 1, 0], u[k + 1, -1] = get_boundary_values(u[k - 1:k + 2, :], h, sigma, type)

    return u

order = 2 
type = (2, 1)

u_implicit = implicit_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, psi_1, psi_2, dd_psi_1, order, type)
u_explicit = explicit_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, psi_1, psi_2, dd_psi_1, order, type)

x = np.arange(x_begin, x_end + h, h)
t = np.arange(t_begin, t_end + tau, tau)


fig, axs = plt.subplots(figsize=(10, 6))

line1, = axs.plot(x, u_explicit[0, :], label="explicit scheme")
line2, = axs.plot(x, u_implicit[0, :], label="implicit scheme")
line3, = axs.plot(x, u_exact[0, :], label="exact solution")

plt.ylim(-2, 2)
plt.legend()

for k in range(t.size):

    line1.set_ydata(u_explicit[k, :])
    line2.set_ydata(u_implicit[k, :])
    line3.set_ydata(u_exact[k, :])

    plt.pause(0.001)