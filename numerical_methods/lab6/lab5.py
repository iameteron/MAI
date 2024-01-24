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
x_end = 1

t_begin = 0
t_end = 1

h = 0.1
tau = h**2 / (2 * a**2)
sigma = a**2 * tau / h**2


def solution(x, t, a=1):
    u = x + np.exp(-np.pi**2 * a * t) * np.sin(np.pi * x)
    return u 

def phi_0(t=0, a=1):
    return 0

def phi_1(t=0, a=1):
    return 1
    
def psi(x):
    return x + np.sin(np.pi * x)

def get_analytical_solution(x_begin, x_end, t_begin, t_end, h, tau, a):

    x = np.arange(x_begin, x_end + h, h)
    t = np.arange(t_begin, t_end + tau, tau)

    res = np.zeros((len(t), len(x)))
    for idx in range(len(x)):
        for idt in range(len(t)):
            res[idt][idx] = solution(x[idx], t[idt], a)
    
    return res

u_exact = get_analytical_solution(x_begin, x_end, t_begin, t_end, h, tau, a)

def explicit_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, phi_0, phi_1, psi):

    sigma = a**2 * tau / h**2
    x = np.arange(x_begin, x_end + h, h)
    t = np.arange(t_begin, t_end + tau, tau)
    res = np.zeros((len(t), len(x)))

    res = np.zeros((len(t), len(x)))
    for col_id in range(len(x)):
        res[0][col_id] = psi(x[col_id])

    for row_id in range(1, len(t)):
        res[row_id][0] = phi_0(t[row_id], a)
        for col_id in range(1, len(x)-1):
            res[row_id][col_id] = (
                sigma * res[row_id-1][col_id-1] 
                + (1 - 2*sigma) * res[row_id-1][col_id]
                + sigma * res[row_id-1][col_id+1]
            )

        res[row_id][-1] = phi_1(t[row_id], a)
    
    return res

u_explicit = explicit_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, phi_0, phi_1, psi)


def implicit_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, phi_0, phi_1, psi):

    sigma = a**2 * tau / h**2
    x = np.arange(x_begin, x_end + h, h)
    t = np.arange(t_begin, t_end + tau, tau)
    res = np.zeros((len(t), len(x)))

    for col_id in range(len(x)):
        res[0][col_id] = psi(x[col_id])

    for row_id in range(1, len(t)):
        A = np.zeros((len(x)-2, len(x)-2))

        A[0][0] = -(1 + 2*sigma)
        A[0][1] = sigma
        for i in range(1, len(A) - 1):
            A[i][i-1] = sigma
            A[i][i] = -(1 + 2*sigma)
            A[i][i+1] = sigma
        A[-1][-2] = sigma
        A[-1][-1] = -(1 + 2*sigma)

        b = -res[row_id-1][1:-1]
        b[0] -= sigma * phi_0(t[row_id])
        b[-1] -= sigma * phi_1(t[row_id])

        res[row_id][0] = phi_0(t[row_id])
        res[row_id][-1] = phi_1(t[row_id])
        res[row_id][1:-1] = sweep_method(A, b)

    return res

u_implicit = implicit_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, phi_0, phi_1, psi)


def crank_nickolson_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, phi_0, phi_1, psi, theta=1/2):

    sigma = a**2 * tau / h**2
    x = np.arange(x_begin, x_end + h, h)
    t = np.arange(t_begin, t_end + tau, tau)
    res = np.zeros((len(t), len(x)))

    for col_id in range(len(x)):
        res[0][col_id] = psi(x[col_id])

    for row_id in range(1, len(t)):
        A = np.zeros((len(x)-2, len(x)-2)) 

        A[0][0] = -(1 + 2*sigma*theta)
        A[0][1] = sigma * theta
        for i in range(1, len(A) - 1):
            A[i][i-1] = sigma * theta
            A[i][i] = -(1 + 2*sigma*theta)
            A[i][i+1] = sigma * theta
        A[-1][-2] = sigma * theta
        A[-1][-1] = -(1 + 2*sigma*theta)

        b = np.array([-(res[row_id-1][i] + (1-theta) * sigma * (res[row_id-1][i-1] - 2*res[row_id-1][i] + res[row_id-1][i+1])) for i in range(1, len(res[row_id-1])-1)])
        # apply boundary conditions
        b[0] -= sigma * theta * phi_0(t[row_id])
        b[-1] -= sigma * theta * phi_1(t[row_id])

        res[row_id][0] = phi_0(t[row_id])
        res[row_id][-1] = phi_1(t[row_id])
        res[row_id][1:-1] = sweep_method(A, b)

    return res

u_crank_nickolson = crank_nickolson_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, phi_0, phi_1, psi)


x = np.arange(x_begin, x_end + h, h)
t = np.arange(t_begin, t_end + tau, tau)


fig, axs = plt.subplots(figsize=(10, 6))

line1, = axs.plot(x, u_explicit[0, :], label="explicit scheme")
line2, = axs.plot(x, u_implicit[0, :], label="implicit scheme")
line3, = axs.plot(x, u_exact[0, :], label="exact solution")
line4, = axs.plot(x, u_crank_nickolson[0, :], label="crank nickolson scheme")

plt.legend()

for k in range(t.size):

    line1.set_ydata(u_explicit[k, :])
    line2.set_ydata(u_implicit[k, :])
    line3.set_ydata(u_exact[k, :])
    line4.set_ydata(u_crank_nickolson[k, :])

    plt.pause(0.4)
