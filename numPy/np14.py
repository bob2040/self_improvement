import numpy as np

# 聚合操作
L = np.random.random(100)
print(L)
print(sum(L))  # 50.82209479044959  使用python自带的sum()
print(np.sum(L))  # 50.82209479044959  使用numpy中的sum()  效率比python的sum()高

A = np.random.rand(10)
print(A)
# [0.37731127 0.45686602 0.10585046 0.78601266 0.50573958 0.81797792
# 0.49302541 0.0776854  0.39959754 0.9703457 ]
big_array = np.array([1, 2, 3, 4, 5])
print(np.min(big_array))  # 1
print(big_array.min())  # 1

print(np.max(big_array))  # 5
print(big_array.max())  # 5

print(np.sum(big_array))  # 15
print(big_array.sum())  # 15

x = np.arange(16).reshape(4, -1)
print(x)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
print(np.sum(x))  # 120
# 求每一列的和，即沿着行的方向
print(np.sum(x, axis=0))  # [24 28 32 36]
# 求每一行的和，即沿着列的方向
print(np.sum(x, axis=1))  # [ 6 22 38 54]

# 所有元素的乘积
print(np.prod(x))  # 0
print(np.prod(x + 1))  # 2004189184  每一个元素都加1后，再所有相乘的积

# 求平均值
print(np.mean(x))  # 7.5

# 求中位数
print(np.median(x))  # 7.5

v = np.array([1, 1, 2, 2, 10])
print(np.mean(v))  # 3.2
print(np.median(v))  # 2.0

print(big_array)  # [1 2 3 4 5]
# 百分位
print(np.percentile(big_array, q=50))  # 3.0  表示在big_array数组的所有元素中，有50%的元素都小于3.0
print(np.median(big_array))  # 3.0

print(np.percentile(big_array, q=100))  # 5.0
print(np.max(big_array))  # 5

for percent in [0, 25, 50, 75, 100]:
    print(np.percentile(big_array, q=percent))
# 1.0
# 2.0
# 3.0
# 4.0
# 5.0

# 求方差
print(np.var(big_array))  # 2.0
# 求标准差
print(np.std(big_array))  # 1.4142135623730951

M = np.random.normal(0, 1, size=1000000)
print(np.mean(M))
print(np.std(M))
