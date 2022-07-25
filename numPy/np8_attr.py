"""
数组属性
"""
import numpy as np

# 复数数组
a = np.array([
    [1+1j, 2+4j, 3+7j],
    [4+2j, 5+5j, 6+8j],
    [7+3j, 8+6j, 9+9j]])
# dtype 元素类型属性
print(a.dtype)  # complex128，128位，16个字节，实部占8个字节，虚部占8个字节
# dtype属性本身的属性str，编码
print(a.dtype.str)  # <c16
# dtype属性本身的属性char，助记符
print(a.dtype.char)  # D

# shape 维度属性
print(a.shape)  # (3, 3) 维度是二维3行3列

# T 转置视图属性
print(a.T)
# [[1.+1.j 4.+2.j 7.+3.j]
#  [2.+4.j 5.+5.j 8.+6.j]
#  [3.+7.j 6.+8.j 9.+9.j]]

# ndim 维数属性
print(a.ndim)  # 2 2维

# size 元素个数
print(a.size)  # 9 共9个元素
print(len(a))  # 3 与size不同，len()返回的是shape属性维度元组的第0号元素，即3

# itemsize 每个元素的字节数
print(a.itemsize)  # 16
# 求数组的总字节数 a.size * a.itemsize
print(a.size * a.itemsize)  # 144

# nbytes 数组的总字节数
print(a.nbytes)  # 144 等价于a.size * a.itemsize

# real 实部数组，imag 虚部数组
print(a.real)
# [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]
print(a.imag)
# [[1. 4. 7.]
#  [2. 5. 8.]
#  [3. 6. 9.]]

# flat 扁平迭代器，只需一重循环，遍历整个数组，比ravel()和flatten()方法更节省内存空间和时间
for elem in a.flat:
    print(elem)
# (1+1j)
# (2+4j)
# (3+7j)
# (4+2j)
# (5+5j)
# (6+8j)
# (7+3j)
# (8+6j)
# (9+9j)
# flat迭代器也是可读可写的，支持下标运算
# 可读取特定的元素
print(a.flat[[1, 3, 5]])  # [2.+4.j 4.+2.j 6.+8.j] 分别是扁平迭代器里面的第1、3、5号元素
# 可写入修改
a.flat[[2, 4, 6]] = 0  # 将扁平迭代器里面的第2、4、6号元素赋值为0
print(a)  # 0.+0.j
# [[1.+1.j 2.+4.j 0.+0.j]
#  [4.+2.j 0.+0.j 6.+8.j]
#  [0.+0.j 8.+6.j 9.+9.j]]


# 数组.tolist()
def fun(a, b):
    a.append(b)
    return a


x = np.array([10, 20, 30])
y = 40
# 把y追加到x中
x = np.array(fun(x.tolist(), y))
print(x)  # [10 20 30 40]

# numpy里面的追加方法 np.append(数组,追加的元素)
np.append(x, 50)
print(x)  # [10 20 30 40] 注意，追加后并不改变原来的x，它是返回值里面多了一个50
# 所以，要接收一下
x = np.append(x, 50)
print(x)  # [10 20 30 40 50]
