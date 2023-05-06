# if判断
# 读入一个整数
# x = int(input("please enter an integer:"))
x = 1
print(x)
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print("single")
else:
    print("more")
# 注意类似三目运算符
y = "one" if x == 1 else "not one"
print(y)

# for 循环
words = ['cat', 'window', 'flower']
for word in words:
    print(word)

users = {'bingo': '1', 'abin': '2', 'liling': '3'}
# 遍历方式一：
for idx in users:
    print(idx, users[idx])
# 遍历方式二：
for key, value in users.items():
    print(key, value)

# range函数
print(list(range(0, 10)))
for i in range(0, 10):
    print(i)
# 指定公差
for i in range(9, -1, -1):
    print(i)

# break  求质数
# 方式一：传统写法
for i in range(2, 10):
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = True
    if not flag:
        print(i)
# 方式二：break写法
for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

# continue
for i in range(2, 10):
    if i % 2 == 0:
        continue
    print(i)

# pass
# 类似 java中的todo，比如python中定义了一个方法，
# 暂时不想实现，可以先用pass表示，因为python中不是用括号划分区间的，
# 所以方法下面必须得有一行是函数的实现

# 定义函数
def add(a,b):
    print(a + b)
add(3,4)
#定义函数可以不用管参数类型,可以给定默认值（只能从最后往前连续个参数设置默认值）
def f(a,b,c,d='bingo'):
    print(a,b,c,d)
def add(a,b,c):
    print(a + b + c)

# 解包 将数组中的数，解包，作为函数的参数
arr = [1,2,3,4]
f(*arr)
# dict字典解包，用**

# lambda表达式
g = lambda x, y: x + y
print(g(3, 4))
