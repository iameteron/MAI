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
t_end = 1

h = 0.1
tau = h / (2 * a)
sigma = a**2 * tau**2 / h**2

def check_sigma(sigma):
    res = True if sigma <= 1 else False
    return res

check_sigma(sigma)

def phi_0(t, a=1):
    return 0

def phi_1(t, a=1):
    return 0
    
def psi_1(x, a=1):
    return 0.2 * (1 - x) * np.sin(np.pi * x)

def psi_2(x, a=1):
    return 0

def dd_psi_2(x, a=1):
    return a * (np.sin(x) + np.cos(x))


def explicit_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, psi_1, psi_2, order=None, type=None):

    sigma = a**2 * tau**2 / h**2
    x = np.arange(x_begin, x_end + h, h)
    t = np.arange(t_begin, t_end + tau, tau)
    u = np.zeros((t.size, x.size))

    u[0:2, :] = get_initial_values(x_begin, x_end, h, tau, psi_1, psi_2, dd_psi_2, order)

    for k in range(1, t.size - 1):

        u[k + 1, 1:-1] = sigma * u[k, 0:-2] + 2 * (1 - sigma) * u[k, 1:-1] + sigma * u[k, 2:] - u[k - 1, 1:-1]
        u[k + 1, 0], u[k + 1, -1] = 0
            
    return u


u_explicit = explicit_scheme(x_begin, x_end, t_begin, t_end, h, tau, a, psi_1, psi_2)

x = np.arange(x_begin, x_end + h, h)
t = np.arange(t_begin, t_end + tau, tau)


fig, axs = plt.subplots(figsize=(10, 6))

line1, = axs.plot(x, u_explicit[0, :], label="explicit scheme")
#line2, = axs.plot(x, u_implicit[0, :], label="implicit scheme")
line3, = axs.plot(x, u_exact[0, :], label="exact solution")

plt.ylim(-2, 2)
plt.legend()

for k in range(t.size):

    line1.set_ydata(u_explicit[k, :])
    #line2.set_ydata(u_implicit[k, :])
    line3.set_ydata(u_exact[k, :])

    plt.pause(0.1)

