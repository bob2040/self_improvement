import numpy as np

# 索引
x = np.random.normal(0, 1, size=1000000)
print(np.min(x))  # -4.846435456196245
print(np.argmin(x))  # 356694  是x中元素最小值的索引值
print(x[356694])  # -4.846435456196245

print(np.argmax(x))  # 143861
print(x[143861])
print(np.max(x))

# 排序和使用索引
x = np.arange(16)
print(x)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
# 将x进行乱序处理，打乱
np.random.shuffle(x)
print(x)  # [13 11  0  4  7  6  3  5  1 12  9  8 15  2 10 14]
# 排序
print(np.sort(x))  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]  注意，这样排序并没有改变x本身
print(x)  # [13 11  0  4  7  6  3  5  1 12  9  8 15  2 10 14]
# 要想改变x本身的顺序
x.sort()  # 这样就是将x本身进行排序
print(x)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]

np.random.seed(666)
y = np.random.randint(10, size=(4, 4))  # 生成元素为0~10之间随机整数的数组，4行4列
print(y)
# [[2 6 9 4]
#  [3 1 0 8]
#  [7 5 2 5]
#  [5 4 8 4]]
print(np.sort(y))  # 默认将每一行里面的元素进行由小到大排序，即：沿着列的方向
# [[2 4 6 9]
#  [0 1 3 8]
#  [2 5 5 7]
#  [4 4 5 8]]
print(np.sort(y, axis=1))  # axis默认值是1
# [[2 4 6 9]
#  [0 1 3 8]
#  [2 5 5 7]
#  [4 4 5 8]]
print(np.sort(y, axis=0))  # 将每一列里面的元素进行由小到大排序，即：沿着行的方向
# [[2 1 0 4]
#  [3 4 2 4]
#  [5 5 8 5]
#  [7 6 9 8]]

print(x)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
np.random.shuffle(x)
print(x)  # [ 3  6  9  7 11  1  8  2  5 12 13 10 15 14  0  4]  原数组
print(np.argsort(x))  # 按照原数组中元素的索引值进行元素的从小到大排序
# [14  5  7  0 15  8  1  3  6  2 11  4  9 10 13 12] 每一个元素都是索引值，索引14对应的是原数组中的0，索引5对应的是原数组中的1，......

print(np.partition(x, 3))  # [ 1  2  0  3 11  7  8  6  5 12 13 10 15 14  9  4]
# 3是标定点，执行后，3前面的元素都比3小，3后面数都比3大，但3前后的元素都是无序的

print(x)  # 原数组： [ 3  6  9  7 11  1  8  2  5 12 13 10 15 14  0  4]
print(np.argpartition(x, 3))  # [ 5  7 14  0  4  3  6  1  8  9 10 11 12 13  2 15]
# 索引5在原数组中为元素1，索引7在原数组中为元素2，索引14在原数组中为元素0，索引0在原数组中为元素3，......

print(y)
# [[2 6 9 4]
#  [3 1 0 8]
#  [7 5 2 5]
#  [5 4 8 4]]
print(np.argsort(y, axis=1))  # 将每一行按照索引值进行元素的从小到大排序  axis=1，即沿着列方向
# [[0 3 1 2]
#  [2 1 0 3]
#  [2 1 3 0]
#  [1 3 0 2]]
print(np.argsort(y, axis=0))  # 将每一列按照索引值进行元素的从小到大排序  axis=0，即沿着行方向
# [[0 1 1 0]
#  [1 3 2 3]
#  [3 2 3 2]
#  [2 0 0 1]]
print(np.argpartition(y, 2, axis=1))
# [[0 3 1 2]
#  [2 1 0 3]
#  [2 1 3 0]
#  [1 3 0 2]]
print(np.argpartition(y, 2, axis=0))
# [[0 1 1 0]
#  [1 3 2 3]
#  [3 2 3 2]
#  [2 0 0 1]]

aa = np.array([[1, 3, 5], [5, 8, 3], [3, 1, 2]])
# aa = np.array([1, 3, 5])
print(aa)
# [[1 3 5]
#  [5 8 3]
#  [3 1 2]]
bb = np.where(aa == 1)
bb1 = np.argwhere(aa == 1)
print(bb)
print(bb1)
