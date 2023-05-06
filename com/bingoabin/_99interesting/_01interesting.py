a = [i for i in range(10)]
print(a)
a = [0] * 10
b = [0 for i in range(10)]
print(a)
print(b)
#注意特殊问题,牵一发而动全身
c = [0]
a = [c for i in range(10)]
print(a)
a[0][0] = 1
print(a)