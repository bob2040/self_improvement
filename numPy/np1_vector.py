"""
使用numpy可以节省运行时间
"""
import numpy as np
import time

n = 100000
# 使用传统方法
start = time.time()
A, B = [], []
for i in range(n):
    A.append(i**2)
    B.append(i**3)
C = []
for a, b in zip(A, B):
    C.append(a + b)
print(time.time() - start)  # 0.13507390022277832

# 使用numpy
start = time.time()
C = np.arange(n)**2 + np.arange(n)**3
print(time.time() - start)  # 0.0

