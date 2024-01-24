import numpy as np

a = np.zeros((6, 6))
for i in range(36):
    a[i // 6][i % 6] = float(input())
    
print(a)
