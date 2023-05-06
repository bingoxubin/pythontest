# 列表
list = [1,2,'abc']
list.append('x') # 常用函数1：append
print(list)
print(len(list)) # 常用函数2：len
del list[0]
print(list)   # 常用函数3：del
list2 = [4,2,6,7,3,2,8,1]
list2 = sorted(list2)  # 常用函数4：sorted或者list2.sort()
print(list2)
a = [1,2,3]             #常用函数5：zip
b = ['a','b','c']
for x,y in zip(a,b):
    print(x,y)
a = a[::-1]   #常用函数6：翻转
print(a)
a.reverse()
print(a)

list1 = [i*i for i in range(10)]
print(list1)

# 元祖
tuple = (1,2,3) # 元祖不能修改
print(tuple)
x,y,z=tuple #分开复制，列表也能用
print(x,y,z)

# 集合
set = set()
set.add(1)
print(set)
set1 = {1,2,3,4,5,5}
print(set1)

# 字典
dict = {'zs':1,'ls':2}
dict['zs']=3
print(dict)

