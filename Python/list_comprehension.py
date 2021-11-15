# c_l = [0, 1, 2, 3, ......, 100]

c_l = []
for i in range(100):
    c_l.append(i)
# print(f'list defined by for loop:{c_l}')

# exercise
# [1, 2, 3, 4, 5, 6, ......, 97, 98, 99, 100]
# [100,99,98,97]
# [[1, 2, 3], [4, 5, 6], ......, [97, 98, 99], [100]]
a = [x for x in zip(range(1,100),range(101, 1,-1))]
b = [a[x: x + 3] for x in range(0, len(a), 3)]
print('\nExercise results:')
print(f'a = {a}\n')
print(f'b = {b}\n')
