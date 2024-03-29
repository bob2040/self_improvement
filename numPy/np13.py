import time
import numpy as np

# 数组中的运算
# 在数学中：
# a = (0,1,2)
# a * 2 = (0,2,4)
# 但在python中：
n = 10
L = [i for i in range(n)]
print(L)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L * 2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  得到的是两个列表的合并
# 所以要：
A = []
for e in L:
    A.append(e * 2)
print(A)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 如果n很大，那么这个方法的效率会很低
n = 100000
L = [i for i in range(n)]
start = time.time()
A = []
for e in L:
    A.append(e * 2)
print(time.time() - start)  # 0.031249523162841797

# 采用生成表达式的方式
start = time.time()
A = [i * 2 for i in L]
print(time.time() - start)  # 0.014883756637573242 快1倍时间
# print(A)

# 使用numpy，运行速度非常快
L = np.arange(n)
start = time.time()
A = np.array(i * 2 for i in L)
print(time.time() - start)  # 0.0

start = time.time()
A = 2 * L
print(time.time() - start)  # 0.0

# Universal Functions
x = np.arange(1, 16).reshape(3, 5)
print(x)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]]
# 加法
print(x + 1)
# [[ 2  3  4  5  6]
#  [ 7  8  9 10 11]
#  [12 13 14 15 16]]
# 减法
print(x - 1)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
# 乘法
print(x * 2)
# [[ 2  4  6  8 10]
#  [12 14 16 18 20]
#  [22 24 26 28 30]]
# 除法
print(x / 2)
# [[0.5 1.  1.5 2.  2.5]
#  [3.  3.5 4.  4.5 5. ]
#  [5.5 6.  6.5 7.  7.5]]
# 整除法
print(x // 2)
# [[0 1 1 2 2]
#  [3 3 4 4 5]
#  [5 6 6 7 7]]
# 乘方
print(x ** 2)
# [[  1   4   9  16  25]
#  [ 36  49  64  81 100]
#  [121 144 169 196 225]]
# 求余
print(x % 2)
# [[1 0 1 0 1]
#  [0 1 0 1 0]
#  [1 0 1 0 1]]
# 取倒数
print(1 / x)
# [[1.         0.5        0.33333333 0.25       0.2       ]
#  [0.16666667 0.14285714 0.125      0.11111111 0.1       ]
#  [0.09090909 0.08333333 0.07692308 0.07142857 0.06666667]]
# 求绝对值
print(np.abs(x))
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]]
# 求正弦
print(np.sin(x))
# [[ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]
#  [-0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]
#  [-0.99999021 -0.53657292  0.42016704  0.99060736  0.65028784]]
# 求余弦
print(np.cos(x))
# [[ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219]
#  [ 0.96017029  0.75390225 -0.14550003 -0.91113026 -0.83907153]
#  [ 0.0044257   0.84385396  0.90744678  0.13673722 -0.75968791]]
# 求正切
print(np.tan(x))
# [[ 1.55740772e+00 -2.18503986e+00 -1.42546543e-01  1.15782128e+00
#   -3.38051501e+00]
#  [-2.91006191e-01  8.71447983e-01 -6.79971146e+00 -4.52315659e-01
#    6.48360827e-01]
#  [-2.25950846e+02 -6.35859929e-01  4.63021133e-01  7.24460662e+00
#   -8.55993401e-01]]

# np.arcsin(), np.arccos(), np.arctan(),...

# 求e的x次方
print(np.exp(x))
# [[2.71828183e+00 7.38905610e+00 2.00855369e+01 5.45981500e+01
#   1.48413159e+02]
#  [4.03428793e+02 1.09663316e+03 2.98095799e+03 8.10308393e+03
#   2.20264658e+04]
#  [5.98741417e+04 1.62754791e+05 4.42413392e+05 1.20260428e+06
#   3.26901737e+06]]
# 求n的x次方
print(np.power(3, x))  # n为3
# print(3 ** x)  # 效果与上面相同
# [[       3        9       27       81      243]
#  [     729     2187     6561    19683    59049]
#  [  177147   531441  1594323  4782969 14348907]]
# 取log值，即以e为底的自然对数
print(np.log(x))
# [[0.         0.69314718 1.09861229 1.38629436 1.60943791]
#  [1.79175947 1.94591015 2.07944154 2.19722458 2.30258509]
#  [2.39789527 2.48490665 2.56494936 2.63905733 2.7080502 ]]
# 取以2为底的log值
print(np.log2(x))
# [[0.         1.         1.5849625  2.         2.32192809]
#  [2.5849625  2.80735492 3.         3.169925   3.32192809]
#  [3.45943162 3.5849625  3.70043972 3.80735492 3.9068906 ]]
# 取以10为底的log值
print(np.log10(x))
# [[0.         0.30103    0.47712125 0.60205999 0.69897   ]
#  [0.77815125 0.84509804 0.90308999 0.95424251 1.        ]
#  [1.04139269 1.07918125 1.11394335 1.14612804 1.17609126]]

# 矩阵运算
A = np.arange(4).reshape(2, 2)
print(A)
# [[0 1]
#  [2 3]]
B = np.full((2, 2), 10)
print(B)
# [[10 10]
#  [10 10]]
# 加法
print(A+B)
# [[10 11]
#  [12 13]]
# 减法
print(A-B)
# [[-10  -9]
#  [ -8  -7]]
# 乘法
print(A*B)
# [[ 0 10]
#  [20 30]]
# 除法
print(A/B)
# [[0.  0.1]
#  [0.2 0.3]]

# 两个矩阵的乘法
print(A.dot(B))  # A矩阵的每一行和B矩阵中的每一列相乘再相加，
# 0*10 + 1*10，0*10 + 1*10    即：10 10
# 2*10 + 3*10，2*10 + 3*10       50 50
# [[10 10]
#  [50 50]]

# 矩阵的转置
print(A.T)
# [[0 2]
#  [1 3]]

C = np.full((3, 3), 666)
print(C)
# [[666 666 666]
#  [666 666 666]
#  [666 666 666]]
# print(A + C)  # 报错，因为A是2行2列的，而C是3行3列的，它俩维度不同，不能运算

# 向量和矩阵的运算
v = np.array([1, 2])
print(v)  # [1 2]  是向量
print(A)  # 是矩阵
# [[0 1]
#  [2 3]]
# 加法
print(v + A)  # 向量与矩阵的每一行进行相加
# [[1 3]
#  [3 5]]
print(np.vstack([v] * A.shape[0]))  # 将向量叠两次
# [[1 2]
#  [1 2]]
print(np.vstack([v] * A.shape[0]) + A)  # 将向量叠两次，然后再与A相加
# [[1 3]
#  [3 5]]

# 堆叠
print(np.tile(v, (2, 1)))  # v是要堆叠的向量，(2, 1)元组表示在行上堆叠2次，在列上堆叠1次
# [[1 2]
#  [1 2]]
print(np.tile(v, (2, 1)) + A)
# [[1 3]
#  [3 5]]

# 乘法
print(v * A)
# [[0 2]
#  [2 6]]
# 矩阵乘法
print(v.dot(A))  # [4 7]  [1*0+2*2 1*1+2*3]  这里v是行向量
print(A.dot(v))  # [2 8]  [0*1+1*2 2*1+3*2]  这里把v当成一个列向量，numpy自动把v转换成了一个2乘1的矩阵，然后再运算

# 矩阵的逆
print(A)
# [[0 1]
#  [2 3]]
# 求A的逆矩阵
print(np.linalg.inv(A))
# [[-1.5  0.5]
#  [ 1.   0. ]]
invA = np.linalg.inv(A)
# 原矩阵乘以其逆矩阵得到的是单位矩阵，要求矩阵是一个方阵，否则无法求其逆矩阵，会报错
print(A.dot(invA))
# [[1. 0.]
#  [0. 1.]]
# 逆矩阵乘以原矩阵得到的也是单位矩阵
print(invA.dot(A))
# [[1. 0.]
#  [0. 1.]]

# 对于非方阵，求其伪逆矩阵
x = np.arange(16).reshape(2, 8)
pinvX = np.linalg.pinv(x)
print(pinvX)
# [[-1.35416667e-01  5.20833333e-02]
#  [-1.01190476e-01  4.16666667e-02]
#  [-6.69642857e-02  3.12500000e-02]
#  [-3.27380952e-02  2.08333333e-02]
#  [ 1.48809524e-03  1.04166667e-02]
#  [ 3.57142857e-02 -6.93889390e-18]
#  [ 6.99404762e-02 -1.04166667e-02]
#  [ 1.04166667e-01 -2.08333333e-02]]
print(pinvX.shape)  # (8, 2)

# 原矩阵乘以其伪逆矩阵得到的是单位矩阵
print(x.dot(pinvX))
# [[ 1.00000000e+00 -2.91433544e-16]
#  [ 1.33226763e-15  1.00000000e+00]]
print(pinvX.dot(x))
# [[ 4.16666667e-01  3.33333333e-01  2.50000000e-01  1.66666667e-01
#    8.33333333e-02  3.33066907e-16 -8.33333333e-02 -1.66666667e-01]
#  [ 3.33333333e-01  2.73809524e-01  2.14285714e-01  1.54761905e-01
#    9.52380952e-02  3.57142857e-02 -2.38095238e-02 -8.33333333e-02]
#  [ 2.50000000e-01  2.14285714e-01  1.78571429e-01  1.42857143e-01
#    1.07142857e-01  7.14285714e-02  3.57142857e-02  2.22044605e-16]
#  [ 1.66666667e-01  1.54761905e-01  1.42857143e-01  1.30952381e-01
#    1.19047619e-01  1.07142857e-01  9.52380952e-02  8.33333333e-02]
#  [ 8.33333333e-02  9.52380952e-02  1.07142857e-01  1.19047619e-01
#    1.30952381e-01  1.42857143e-01  1.54761905e-01  1.66666667e-01]
#  [-5.55111512e-17  3.57142857e-02  7.14285714e-02  1.07142857e-01
#    1.42857143e-01  1.78571429e-01  2.14285714e-01  2.50000000e-01]
#  [-8.33333333e-02 -2.38095238e-02  3.57142857e-02  9.52380952e-02
#    1.54761905e-01  2.14285714e-01  2.73809524e-01  3.33333333e-01]
#  [-1.66666667e-01 -8.33333333e-02 -2.22044605e-16  8.33333333e-02
#    1.66666667e-01  2.50000000e-01  3.33333333e-01  4.16666667e-01]]
