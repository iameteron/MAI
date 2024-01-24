import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp


def Rot2D(X,Y,Phi):
    RotX = X * np.cos(Phi) - Y * np.sin(Phi)
    RotY = X * np.sin(Phi) + Y * np.cos(Phi)
    return RotX, RotY


t = sp.Symbol('t')
x = sp.cos(t) * (1 + sp.sin(t))
y = sp.sin(t) * (1 + sp.sin(t))
Vx = sp.diff(x, t)
Vy = sp.diff(y, t)
V = sp.sqrt(Vx * Vx + Vy * Vy)
Wx = sp.diff(Vx, t)
Wy = sp.diff(Vy, t)
W = sp.sqrt(Wx * Wx + Wy * Wy)
Wtao = sp.diff(V)
Taox = Vx / (sp.sqrt(Vx * Vx + Vy * Vy))
Taoy = Vy / (sp.sqrt(Vx * Vx + Vy * Vy))
R = V * V / sp.sqrt(W * W - Wtao * Wtao)

F_x = sp.lambdify(t, x)
F_y = sp.lambdify(t, y)
F_Vx = sp.lambdify(t, Vx)
F_Vy = sp.lambdify(t, Vy)
F_Wx = sp.lambdify(t, Wx)
F_Wy = sp.lambdify(t, Wy)
F_Taox = sp.lambdify(t, Taox)
F_Taoy = sp.lambdify(t, Taoy)
F_V = sp.lambdify(t, V)
F_Wtao = sp.lambdify(t, Wtao)
F_W = sp.lambdify(t, W)
F_R = sp.lambdify(t, R)

Steps = 1001
T = np.linspace(0, 20, Steps)
alpha = np.linspace(0, 6.28, 100)

X = np.zeros_like(T)
Y = np.zeros_like(T)
VX = np.zeros_like(T)
VY = np.zeros_like(T)
WX = np.zeros_like(T)
WY = np.zeros_like(T)
TaoX = np.zeros_like(T)
TaoY = np.zeros_like(T)
V_ = np.zeros_like(T)
WTao = np.zeros_like(T)
W_ = np.zeros_like(T)
R_ = np.zeros_like(T)
NX = np.zeros_like(T)
NY = np.zeros_like(T)
CircleX = np.zeros((len(T),len(alpha)))
CircleY = np.zeros((len(T),len(alpha)))

Theta = 3.14 / 2

for i in np.arange(len(T)):
    X[i] = F_x(T[i])
    Y[i] = F_y(T[i])
    VX[i] = F_Vx(T[i])
    VY[i] = F_Vy(T[i])
    WX[i] = F_Wx(T[i])
    WY[i] = F_Wy(T[i])
    TaoX[i] = F_Taox(T[i])
    TaoY[i] = F_Taoy(T[i])
    V_[i] = F_V(T[i])
    WTao[i] = F_Wtao(T[i])
    W_[i] = F_W(T[i])
    R_[i] = F_R(T[i])
    NX[i], NY[i] = Rot2D(R_[i] * TaoX[i], R_[i] * TaoY[i], Theta)
    for j in np.arange(len(alpha)):
        CircleX[i][j] = R_[i] * np.cos(alpha[j])
        CircleY[i][j] = R_[i] * np.sin(alpha[j])


Phi = np.arctan2(VY, VX)
Psi = np.arctan2(WY, WX)

fig = plt.figure()  # создаем рисунок
ax = fig.add_subplot(1, 1, 1)   # создаем график
Max = max(VX + VY + WX + WY + R_)
midX = max(X) - min(X)
midY = max(Y) - min(Y)
ax.set(xlim = [ min(X) - midX, max(X) + midX],
       ylim = [ min(Y) - midY, max(Y) + midY])
ax.plot(X, Y, color=[0, 0, 0])   # рисуем

P = ax.plot(X[0], Y[0], marker='o')[0]
V_Line = ax.plot(X[0], X[0] + VX[0], Y[0], Y[0] + VY[0], color=[1, 0, 0])[0]
W_Line = ax.plot(X[0], X[0] + WX[0], Y[0], Y[0] + WY[0], color=[0, 1, 0])[0]
#Tao_Line = ax.plot(X[0], X[0] + TaoX[0], Y[0], Y[0] + TaoY[0], color=[0, 0, 1])[0]
N_Line = ax.plot(X[0], X[0] + NX[0], Y[0], Y[0] + NY[0], color=[0, 0, 1])[0]
CenterPoint = ax.plot(NX[0], NY[0], marker='o', color=[0, 0, 1])[0]

Circle = ax.plot(CircleX[50], CircleY[50], color=[0, 0, 1])[0]

XArrow = np.array([-0.15, 0, -0.15])
YArrow = np.array([0.1, 0, -0.1])
RarrowX, RarrowY = Rot2D(XArrow, YArrow, Phi[0])
V_Arrow = ax.plot(X[0] + RarrowX, Y[0] + RarrowY, color=[1, 0, 0])[0]       #red
W_Arrow = ax.plot(X[0] + RarrowX, Y[0] + RarrowY, color=[0, 1, 0])[0]       #green
#Tao_Arrow = ax.plot(X[0] + RarrowX, Y[0] + RarrowY, color=[0, 0, 1])[0]     #blue


def MagicOfTheMovement(i):
    P.set_data(X[i], Y[i])
    V_Line.set_data([X[i], X[i] + VX[i]], [Y[i], Y[i] + VY[i]])
    W_Line.set_data([X[i], X[i] + WX[i]], [Y[i], Y[i] + WY[i]])
#    Tao_Line.set_data([X[i], X[i] + TaoX[i]], [Y[i], Y[i] + TaoY[i]])
    N_Line.set_data([X[i], X[i] + NX[i]], [Y[i], Y[i] + NY[i]])

    RarrowX, RarrowY = Rot2D(XArrow, YArrow, Phi[i])
    V_Arrow.set_data(X[i] + VX[i] + RarrowX, Y[i] + VY[i] + RarrowY)
#    Tao_Arrow.set_data(X[i] + TaoX[i] + RarrowX, Y[i] + TaoY[i] + RarrowY)

    RarrowX, RarrowY = Rot2D(XArrow, YArrow, Psi[i])
    W_Arrow.set_data(X[i]+WX[i]+RarrowX, Y[i]+WY[i]+RarrowY)

    Circle.set_data(X[i] + NX[i] + CircleX[i], Y[i] + NY[i] + CircleY[i])
    CenterPoint.set_data(X[i] + NX[i], Y[i] + NY[i])


    return [P, V_Line, V_Arrow]


nechto = FuncAnimation(fig, MagicOfTheMovement, frames=10*Steps, interval=10)

plt.show()  # просим его показать
