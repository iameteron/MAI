import numpy as np
from module34 import *
from matplotlib import pyplot as plt

x_star = float(input())
x = np.fromstring(input(), dtype=float, sep=' ')
y = np.fromstring(input(), dtype=float, sep=' ')

y_left, y_der, y_right = numerical_first_derivative(x, y, x_star)

print(f"First numerical derivative of a function y at a point x* = {x_star}: \n")
print(f"y'(x*) =  {y_left}   (left)  \n")
print(f"y'(x*) =  {y_right}  (right) \n")
print(f"y'(x*) =  {y_der}    (mid)   \n")

print(f"Second numerical derivative of a function y at a point x* = {x_star}: \n")
print(f"y''(x*) =  {numerical_second_derivative(x, y, x_star)} \n")

plt.plot(x, y)
plt.show()