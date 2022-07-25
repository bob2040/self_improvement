import numpy as np

# Fancy Indexing
x = np.arange(16)
print(x)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
ind = [3, 5, 8]
print(x[ind])  # [3 5 8]  获取索引为3，5和8对应的元素值

ind = np.array([[0, 2],  # 索引数组
               [1, 3]])
print(x[ind])  # 获得索引数组对应的元素数组
# [[0 2]
#  [1 3]]

X = x.reshape(4, -1)
print(X)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
row = np.array([0, 1, 2])  # 感兴趣的行索引
col = np.array([1, 2, 3])  # 感兴趣的列索引
print(X[row, col])  # [ 1  6 11]  得到X[0,1] X[1,2] X[2,3]
print(X[0, col])  # [1 2 3]  得到X[0,1] X[0,2] X[0,3]
print(X[:2, col])
# [[1 2 3]  X[0,1] X[0 2] X[0 3]
#  [5 6 7]]  X[1,1] X[1,2] X[1,3]
print(X[row, 0])  # [0 4 8]  得到X[0,0] X[1,0] X[2,0]

col = [True, False, True, True]
print(X[1:3, col])  # 只对列的索引为0，2，3的元素感兴趣，不要列的索引为1的元素，即：True的留下，False的舍弃
# [[ 4  6  7]
#  [ 8 10 11]]

# numpy.array的比较
print(x)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
print(x < 3)  # 将x中的所有元素都去与3比较，小于3的为True，其他为False
# [ True  True  True False False False False False False False False False
#  False False False False]
print(x > 3)
# [False False False False  True  True  True  True  True  True  True  True
#   True  True  True  True]
print(x <= 3)
print(x >= 3)
print(x == 3)
# [False False False  True False False False False False False False False
#  False False False False]
print(x != 3)
# [ True  True  True False  True  True  True  True  True  True  True  True
#   True  True  True  True]

print(2 * x == 24 - 4 * x)
# [False False False False  True False False False False False False False
#  False False False False]

print(X)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
print(X < 6)
# [[ True  True  True  True]
#  [ True  True False False]
#  [False False False False]
#  [False False False False]]

print(x)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
# 求x数组中有多少个数是小于等于3的
print(np.sum(x <= 3))  # 4
print(np.count_nonzero(x <= 3))  # 4  4个Ture,传进去的 x <= 3 是一个布尔数组，True为1，False为0

# 计算x数组中有多少个非0元素
print(np.count_nonzero(x))  # 15

# 判断x数组中是否有任意一个元素满足括号中的条件
print(np.any(x == 0))  # True 如果有任意一个元素为0，则返回True，否则返回False
print(np.any(x < 0))  # False 如果有任意一个元素小于0，则返回True，否则返回False

# 判断x数组中是否所有元素都满足括号中的条件
print(np.all(x >= 0))  # True x中所有元素都满足条件x >= 0，所以返回True
print(np.all(x > 0))  # False x中有元素为0，不都满足条件x > 0，所以返回False

print(X)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
# 求X中有多少个偶数
print(np.sum(X % 2 == 0))  # 8
print(np.sum(X % 2 == 0, axis=1))  # [2 2 2 2]  axis=1,即沿着列方向，看每一行有多少偶数
print(np.sum(X % 2 == 0, axis=0))  # [4 0 4 0]  axis=0,即沿着行方向，看每一列有多少偶数

#
print(np.all(X > 0, axis=1))  # [False  True  True  True]

print(x)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
# 求x中大于3小于10的数字的个数
print(np.sum((x > 3) & (x < 10)))  # 6  &是与运算符，&为位运算符，&&为条件运算符
# 数字为偶数或者数字大于10的有多少个
print(np.sum((x % 2 == 0) | (x > 10)))  # 11  |是或运算符
# 不为0的数有多少
print(np.sum(~(x == 0)))  # 15  ~是非运算符
# 查看x中小于5的元素
print(x[x < 5])  # [0 1 2 3 4]
# 查看数组中所有的偶数
print(x[x % 2 == 0])  # [ 0  2  4  6  8 10 12 14]

print(X)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
# 取出X中最后一列能被3整除的行
print(X[X[:, 3] % 3 == 0, :])
# [[ 0  1  2  3]
#  [12 13 14 15]]
