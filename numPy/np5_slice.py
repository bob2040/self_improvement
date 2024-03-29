"""
切片
"""
import numpy as np
# 一维数组的情况
a = np.arange(1, 10)
print(a)  # [1 2 3 4 5 6 7 8 9]
print(a[:3])  # [1 2 3]
print(a[3:6])  # [4 5 6]
print(a[6:])  # [7 8 9]
print(a[::-1])  # [9 8 7 6 5 4 3 2 1]
print(a[:-4:-1])  # [9 8 7]
print(a[-4:-7:-1])  # [6 5 4]
print(a[-7::-1])  # [3 2 1]
print(a[::])  # [1 2 3 4 5 6 7 8 9]
print(a[...])  # [1 2 3 4 5 6 7 8 9]
print(a[:])  # [1 2 3 4 5 6 7 8 9]
# print(a[])  # SyntaxError: invalid syntax
print(a[::3])  # [1 4 7]
print(a[1::3])  # [2 5 8]
print(a[2::3])  # [3 6 9]

# 多维数组的情况
b = np.arange(1, 25).reshape(2, 3, 4)  # reshape() 改变维度的方法，这里把一维数组变成三维数组
print(b)
'''
[[[ 1  2  3  4]
  [ 5  6  7  8]
  [ 9 10 11 12]]
 [[13 14 15 16]
  [17 18 19 20]
  [21 22 23 24]]]
'''
print(b[:, 0, 0])  # :表示取所有页的，0表示第0行，0表示第0列  运行结果：[ 1 13]
print(b[0, :, :])  # 也可以这样写b[0, ...]
# 0表示取第0页，:表示所有行，:表示所有列  运行结果：
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
print(b[0, ...])

print(b[0, 1, ::2])  # 0表示取第0页的，1表示第1行，::2表示在列上进行切片，步长为2  运行结果：[5 7]
print(b[:, :, 1])  # 也可以这样写b[..., 1]
# :表示取所有页的，:表示所有行，1表示第1列  运行结果：
# [[ 2  6 10]
#  [14 18 22]]
print(b[..., 1])

print(b[:, 1])  # 取所有页的第1行，与上面不同，注意！
# 运行结果：
# [[ 5  6  7  8]
#  [17 18 19 20]]

print(b[-1, 1:, 2:])
# -1表示最后1页，1:表示从第1行开始切到最后行，2:表示从第2列开始切到最后列 运行结果：
# [[19 20]
#  [23 24]]
