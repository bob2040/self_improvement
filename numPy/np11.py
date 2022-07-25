import numpy as np

a = np.zeros(10)
print(a)  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(a.dtype)  # float64

b = np.zeros((3, 5))
print(b)
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
print(b.dtype)  # float64

c = np.ones((3, 5))
print(c)
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

d = np.ones(shape=(3, 5), dtype=int)
print(d)
# [[1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]
print(d.dtype)  # int32

e = np.full((3, 5), 666)
print(e)
# [[666 666 666 666 666]
#  [666 666 666 666 666]
#  [666 666 666 666 666]]
print(e.dtype)  # int32

# f = np.full((3, 5), 666.0)
f = np.full(shape=(3, 5), fill_value=666.0)
print(f)
# [[666. 666. 666. 666. 666.]
#  [666. 666. 666. 666. 666.]
#  [666. 666. 666. 666. 666.]]
print(f.dtype)  # float64

# np.arange步长可为浮点型，这在python的range中是不允许的
g = np.arange(0, 1, 0.2)
print(g)  # [0.  0.2 0.4 0.6 0.8]

h = np.linspace(0, 20, 10)
print(h)
# [ 0.          2.22222222  4.44444444  6.66666667  8.88888889 11.11111111
#  13.33333333 15.55555556 17.77777778 20.        ]

i = np.linspace(0, 20, 11)
print(i)  # [ 0.  2.  4.  6.  8. 10. 12. 14. 16. 18. 20.]

# 随机数 random
j = np.random.randint(0, 10)  # 生成一个随机整数，包含0，不包含10
print(j)  # 3

# k = np.random.randint(0, 10, 10)  # 生成一个10个元素的数组，每个元素是0到10之间的随机数，包含0，不包含10
k = np.random.randint(0, 10, size=10)  # 生成一个10个元素的数组，每个元素是0到10之间的随机数，包含0，不包含10
print(k)  # [2 4 0 0 7 6 9 5 1 4]

l = np.random.randint(4, 8, size=(3, 5))
print(l)
# [[5 4 7 4 7]
#  [5 7 7 6 5]
#  [6 5 4 5 6]]

# 随机种子 np.random.seed()
np.random.seed(666)
m = np.random.randint(4, 8, size=(3, 5))
print(m)
# [[4 6 5 6 6]
#  [6 5 6 4 5]
#  [7 6 7 4 7]]
np.random.seed(666)
n = np.random.randint(4, 8, size=(3, 5))
print(n)  # 随机种子使得第二次得到的随机矩阵与第一次得到的相同
# [[4 6 5 6 6]
#  [6 5 6 4 5]
#  [7 6 7 4 7]]

# 随机浮点数 np.random.random()
o = np.random.random()
print(o)  # 0.2811684913927954

p = np.random.random(10)
print(p)
# [0.46284169 0.23340091 0.76706421 0.81995656 0.39747625 0.31644109
#  0.15551206 0.73460987 0.73159555 0.8578588 ]

q = np.random.random((3, 5))
print(q)
# [[0.76741234 0.95323137 0.29097383 0.84778197 0.3497619 ]
#  [0.92389692 0.29489453 0.52438061 0.94253896 0.07473949]
#  [0.27646251 0.4675855  0.31581532 0.39016259 0.26832981]]

# 生成符合正态分布的随机浮点数
u = np.random.normal()  # 默认生成符合均值为0方差为1，这样分布的里面的一个随机浮点数
print(u)  # 0.7760516793129695

v = np.random.normal(10, 100)  # 生成符合均值为10方差为100，这样分布里的一个随机浮点数
print(v)  # 128.06359754812632

w = np.random.normal(0, 1, (3, 5))  # 生成符合均值为0方差为1，这样分布里的一个3行5列的随机浮点数组
print(w)
# [[ 0.06102404  1.07856138 -0.79783572  1.1701326   0.1121217 ]
#  [ 0.03185388 -0.19206285  0.78611284 -1.69046314 -0.98873907]
#  [ 0.31398563  0.39638567  0.57656584 -0.07019407  0.91250436]]

x = np.random.rand(10)
print(x)
# [0.2427146  0.57043673 0.57773404 0.89274848 0.12138544 0.66083873
#  0.16459271 0.09435837 0.5876144  0.86014445]

