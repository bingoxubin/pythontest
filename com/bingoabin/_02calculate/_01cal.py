import copy

# 计算符
print(2 + 2)
print(8 / 5)  # 除法1.6
print(1 / 3)  # 0.3333333333333333
print(8 // 5)  # 整除 1  注意：是向下取整，c++中是向0取整
print(8 % 5)  # 取余数 3
print(2 ** 3)  # 2的3次方 8
print(round(2.123123123, 2))  # 保留2位小数

# 字符串
print('fdsf sdfsdf')
print('doesn\'t')  # 中间需要转义
print('"yes," i am ok')  # "yes," i am ok
print("\"yes,\" i am ok")  # "yes," i am ok
print('"Isn\'t," they said')  # "Isn't," they said
print('c:\some\name')  # 其中进行了转义，如果不想转义 前面加上r
print(r'c:\some\name')  # 其中进行了转义，如果不想转义 前面加上r
print("""\              
      My Name
        is 
    Bingo
      """)  # 原样输出,其中第一个\ 表示去掉回车
print("abc" * 3)  # abcabcabc

a = "abcdefg"
print(a[1])  # b
print(a[-1])  # g
print(a[0:2])  # ab 切片 左闭右开   注意：前后可以省略，前面省略默认是0，后面省略默认是-1
# 注意：字符串中的元素不能进行修改
print(len(a))  # 字符串的长度

# 列表
# python中常用的数据结构 list set dist
squarts = [1, 2, 3, 4, 5, 6]
print(squarts)
print(len(squarts))
print(squarts[1])  # 2
arr = [1, 2, "abc", [3, 4]]  # 列表中可以包含任意元素
print(squarts[:])  # 复制一个数组
# 浅拷贝
x = [1, 2]
y = [3, 4]
m = [x, y]
n = m
n[0] = "abc"  # n 是 ['abc', [3, 4]]
print(m)  # m 是 ['abc', [3, 4]]
# 拷贝第一层
p = [x, y]
q = p[:]
q[0] = "abc"  # q 是 ['abc', [3, 4]]
print(p)  # p 是 [[1, 2], [3, 4]]
# 深拷贝 递归拷贝
r = [x, y]
s = copy.deepcopy(r)
s[0] = "abc";
print(r)  # [[1, 2], [3, 4]]

print(x + y)  # 列表可以进行相加 [1, 2, 3, 4]
x.append(6)  # 列表中添加一个元素
print(x)

x = [1, 2, 3, 4, 5]
x[1:2] = "abc"  # 切片进行替换 注意加[]和不加的区别 加的话变成[1, 'abc', 3, 4, 5] 不加变成[1, 'a', 'b', 'c', 3, 4, 5]
print(x)

a, b = 0, 1  # 符合赋值
print(a, b)  # 0 1
a, b = b, a  # 交换变量
print(a, b)  # 1 0

# 求斐波那契额数列
print(40 * "=")
a,b=0,1
while a < 10:
    print(a,end=', ')
    a, b = b, a + b
