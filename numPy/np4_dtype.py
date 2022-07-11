import numpy as np
# 第一种自定义数据类型，数组元素中包含多种数据类型
# a = np.array([('ABC', [1, 2, 3])])  # 直接这样创建报错，数据类型不一致
a = np.array([('ABC', [1, 2, 3])], dtype='U3, 3i4')
# 'U3, 3i4'是个自定义数据类型
# U3是元组中第0个元素的数据类型，U3中的U表示numpy.str_，即字符串，U3中的3表示3个字符。
# 3i4是元组中第1个元素的数据类型，3i4中的3表示列表中有3个元素，3i4中的i4表示numpy.int32。
print(a)  # [('ABC', [1, 2, 3])]
# 获取数组元素元组中的元素，元组中的每一个字段用f表示，f0表示数组中的第0号元素，即'ABC'，f1表示数组中的第1号元素，即[1 2 3]，以此类推。
print(a[0]['f0'])  # ABC
print(a[0]['f1'])  # [1 2 3]
print(a[0]['f1'][0])  # 1
print(a[0]['f1'][1])  # 2
print(a[0]['f1'][2])  # 3

b = np.array([('ABC', [1, 2, 3])], dtype=[('name', np.str_, 3), ('scores', np.int32, 3)])
# [('name', np.str_, 3), ('scores', np.int32, 3)] 也是自定义数据类型
# 列表中第1个元组用于描述数组元素元组中的第0号元素'ABC'，
# 'name'表示该元素(字符串)的字段名是name，np.str_表示的是numpy中的字符串类型，此时不能再像上面a中那样简写，3表示3个字符，字符串长度为3
# 列表中第2个元组用于描述数组元素元组中的第1号元素[1, 2, 3]，
# 'scores'表示该元素(列表)的字段名是scores，np.int32表示的是numpy中的int32数据类型，此时不能再像上面a中那样简写，3表示3个元素，列表长度为3
print(b)  # [('ABC', [1, 2, 3])]
# 用字段名访问元素
print(b[0]['name'])  # ABC
print(b[0]['scores'])  # [1 2 3]
print(b[0]['scores'][0])  # 1
print(b[0]['scores'][1])  # 2
print(b[0]['scores'][2])  # 3

# 进一步简化写法，老师推荐的写法
c = np.array([('ABC', [1, 2, 3])], dtype={'names': ['name', 'scores'], 'formats': ['U3', '3i4']})
# 'names'和'formats'两个键的书写是固定不变的，'names'表示字段名，'formats'表示每个字段中元素的格式，可简写
print(c)  # [('ABC', [1, 2, 3])]
# 用字段名访问元素
print(c[0]['name'])  # ABC
print(c[0]['scores'])  # [1 2 3]
print(c[0]['scores'][0])  # 1
print(c[0]['scores'][1])  # 2
print(c[0]['scores'][2])  # 3

# 再进一步简化的写法
d = np.array([('ABCD', [1, 2, 3])], dtype={'name': ('U4', 0), 'scores': ('3i4', 16)})
# 'name': ('U3', 0) 键'name'是对应元素的字段名为'name'，值是一个元组，'U3'是元素类型，0是指定的偏移量，第0个元素，偏移量就是0
# 'scores': ('3i4', 0) 键'scores'是对应元素的字段名为'scores'，值是一个元组，'3i4'是元素类型，16是指定的偏移量，
# 第0个元素4个字符占16个字节(unicode编码每个字符占4个字节)，那么第1个元素指定的偏移量就是16，起始位置为16
print(d)  # [('ABC', [1, 2, 3])]
# 用字段名访问元素
print(d[0]['name'])  # ABC
print(d[0]['scores'])  # [1 2 3]
print(d[0]['scores'][0])  # 1
print(d[0]['scores'][1])  # 2
print(d[0]['scores'][2])  # 3

# 第二种自定义数据类型，把一个数看成几种不同的数据类型。对一个元素做不同类型的访问
e = np.array([0x1234], dtype=('>u2', {'lo': ('u1', 0), 'hi': ('u1', 1)}))
print('{:x}'.format(e[0]))  # 以十六进制形式输出  1234 是十六进制的
print('{:x} {:x}'.format(e['lo'][0], e['hi'][0]))  # 12 34  大端字节序，低数位高地址，高数位低地址

f = np.array([0x1234], dtype=('<u2', {'lo': ('u1', 0), 'hi': ('u1', 1)}))
print('{:x}'.format(f[0]))  # 以十六进制形式输出  1234 是十六进制的
print('{:x} {:x}'.format(f['lo'][0], f['hi'][0]))  # 34 12  小端字节序，低数位低地址，高数位高地址

g = np.array([0x1234], dtype=('=u2', {'lo': ('u1', 0), 'hi': ('u1', 1)}))
print('{:x}'.format(g[0]))  # 以十六进制形式输出  1234 是十六进制的
print('{:x} {:x}'.format(g['lo'][0], g['hi'][0]))  # 34 12  处理器系统默认字节序为：低数位低地址，高数位高地址