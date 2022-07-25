"""
使用numpy创建数组的方法
"""
import numpy as np

# arange()
a = np.arange(10)
print(a)  # [0 1 2 3 4 5 6 7 8 9]
b = np.arange(1, 10)
print(b)  # [1 2 3 4 5 6 7 8 9]
c = np.arange(1, 10, 2)
print(c)  # [1 3 5 7 9]

# array()
d = np.array([])
print(d)  # []
e = np.array([10, 20, 30, 40, 50])
print(e)  # [10 20 30 40 50]
f = np.array([[1, 2, 3], [4, 5, 6]])
print(f)  # [[1 2 3]
           # [4 5 6]]

# 查看f对象的数据类型
print(type(f))  # <class 'numpy.ndarray'>
print(type(f[0][0]))  # <class 'numpy.int32'> 32位整型
print(type(f.dtype))  # <class 'numpy.dtype[int32]'> 32位整型 4个字节

g = np.array(['1', '2', '3'])
print(type(g[0]))  # <class 'numpy.str_'>  字符串类型，下划线是与python中的字符串区分
print(g.dtype)  # <U1  <表示小端字节序，U表示字符串采用的unicode编码，unicode编码里面每个字符占4个字节，1表示每个字符串的长度为1
# 创建的时候人为指定数据类型 dtype属性
h = np.array(['1', '2', '3'], dtype=np.int32)
# print(h)
print(type(h[0]))  # <class 'numpy.int32'>  已经不是字符串了
print(h.dtype)  # int32
# print(h)
# 将其再变回字符串 astype()方法
k = h.astype(np.str_)
print(type(k[0]))  # <class 'numpy.str_'>
print(k.dtype)  # <U11

# 数组的维度 ndarray.shape
print(e.shape)  # (5,) 表示1维的，5个元素
print(f.shape)  # (2, 3) 表示2行3列，二维数组
l = np.array([
    [np.arange(1, 5), np.arange(5, 9), np.arange(9, 13)],
    [np.arange(13, 17), np.arange(17, 21), np.arange(21, 25)]
    ])
print(l.shape)  # (2, 3, 4) 2页，3行，4列，三维数组
print(l)
'''
[[[ 1  2  3  4]
  [ 5  6  7  8]
  [ 9 10 11 12]]
 [[13 14 15 16]
  [17 18 19 20]
  [21 22 23 24]]]
'''