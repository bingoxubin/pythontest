# from com.bingoabin._03processcontrol import _01processcontrol
from com.bingoabin._03processcontrol._01processcontrol import add

# from 包 import 文件
# 或者
# from 文件 import 函数  注意也可以起别名，用as方式
# 都可以
print("==========================")
# _01processcontrol.add(1,2,3)
add(1,2,3)

# python自带了很多模块
from random import randint
print(randint(1,10))  # 返回【1-10】之间的一个随机数