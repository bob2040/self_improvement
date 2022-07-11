"""
索引
"""
import numpy as np

a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 创建2页，2行，2列的数组
print(a)  # 整个数组
print(a[0])  # 第0页
print(a[0][0])  # 第0页中的第0行  [1 2]
print(a[0][0][0])  # 第0页中的第0行中的第0列  1

# 遍历
for i in range(a.shape[0]):  # a.shape[0]是数组维度元组中的0号元素，表示页数
    for j in range(a.shape[1]):  # a.shape[1]是数组维度元组中的1号元素，表示行数
        for k in range(a.shape[2]):  # a.shape[2]是数组维度元组中的2号元素，表示列数
            print(a[i][j][k], a[i, j, k])  # a[i][j][k]也可以写成a[i, j, k]这样，两者相同

# numpy的内置类型和自定义类型
b = np.array([1, 2, 3], dtype=int)  # int是python中的数据类型，numpy会自动将其映射为numpy中的np.int32，
                                    # 但是这种映射与系统有关，与解释器的字长有关(字长是32位的或64位的)，
                                    # 若是64位系统，可能映射成np.int64
print(b.dtype)  # int32
c = b.astype(float)  # float -> np.float64
print(c.dtype)  # float64
d = c.astype(str)  # str -> np.str_
print(d.dtype)  # <U32 表示小端字节序，unicode编码，32位字长
