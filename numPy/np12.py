import numpy as np

# 数组合并
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])

z = np.concatenate([x, y])
print(z)  # [1 2 3 3 2 1]

A = np.concatenate([x, y, z])
print(A)  # [1 2 3 3 2 1 1 2 3 3 2 1]

B = np.array([[1, 2, 3],
              [4, 5, 6]])
C = np.concatenate([B, B])
print(C)
# [[1 2 3]
#  [4 5 6]
#  [1 2 3]
#  [4 5 6]]

D = np.concatenate([B, B], axis=0)  # axis=0，沿着第0个维度进行拼接，即行的方向
print(D)
# [[1 2 3]
#  [4 5 6]
#  [1 2 3]
#  [4 5 6]]

E = np.concatenate([B, B], axis=1)  # axis=1，沿着第1个维度进行拼接，即列的方向
print(E)
# [[1 2 3 1 2 3]
#  [4 5 6 4 5 6]]

# F = np.concatenate([B, x.reshape(1, -1)])  # 注意 concatenate([]) 只能拼接维数相同的数组，所以x要变维后拼接，否则报错
F = np.vstack([B, x])  # vstack不需要变维
print(F)
# [[1 2 3]
#  [4 5 6]
#  [1 2 3]]

# 数组分割
a = np.arange(10)
print(a)  # [0 1 2 3 4 5 6 7 8 9]
a1, a2, a3 = np.split(a, [3, 7])
# a是被分割数组，[3, 7]是分割点，3和7是a数组中元素的索引，0到3(不包含3)，3到7(不包含7)，7到最后，这样就分成三个数组
print(a1, a2, a3)  # [0 1 2] [3 4 5 6] [7 8 9]

a4, a5 = np.split(a, [5])  # 分成两个数组，分割点要这样写[5]，也要有中括号[]
print(a4, a5)  # [0 1 2 3 4] [5 6 7 8 9]

b = np.arange(16).reshape((4, 4))
print(b)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
b1, b2 = np.split(b, [2])  # axis默认值是0，即在行的维度上，所以[2]分割点是行，0到2(不包括2),2到最后，分成两个数组
print(b1)
# [[0 1 2 3]
#  [4 5 6 7]]
print(b2)
# [[ 8  9 10 11]
#  [12 13 14 15]]

b3, b4 = np.split(b, [2], axis=1)  # axis=1，指定在列的维度上进行分割，所以[2]分割点是列，0到2(不包括2),2到最后，分成两个数组
print(b3)
# [[ 0  1]
#  [ 4  5]
#  [ 8  9]
#  [12 13]]
print(b4)
# [[ 2  3]
#  [ 6  7]
#  [10 11]
#  [14 15]]

upper, lower = np.vsplit(b, [2])
print(upper)
# [[0 1 2 3]
#  [4 5 6 7]]
print(lower)
# [[ 8  9 10 11]
#  [12 13 14 15]]

left, right = np.hsplit(b, [2])
print(left)
# [[ 0  1]
#  [ 4  5]
#  [ 8  9]
#  [12 13]]
print(right)
# [[ 2  3]
#  [ 6  7]
#  [10 11]
#  [14 15]]
b5, b6 = np.hsplit(b, [-1])  # b6就是最后1列，b5是前3列
print(b5)
# [[ 0  1  2]
#  [ 4  5  6]
#  [ 8  9 10]
#  [12 13 14]]
print(b6)
# [[ 3]
#  [ 7]
#  [11]
#  [15]]
print(b6[:, 0])  # [ 3  7 11 15]
