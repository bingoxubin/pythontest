s = "%04d %.2lf %s" % (2,3.4,"abc") # 格式化输出
print(s)

fout = open('test.txt','w')  # 写文件 这种方式如果异常退出，会导致文件没有关闭
for i in range(1,10):
    fout.write(str(i) + '\n')
fout.close()

# 采用下面这种方式,不需要进行关闭
with open('test1.txt','w') as fout:
    for i in range(1,10):
        fout.write(str(i) + '\n')

# 读文件
with open('test1.txt','r') as fin:
    # print(fin.read())
    print(fin.readlines())  # 读取所有行，返回一个列表
with open('test1.txt','r') as fin:
    for line in fin:
        print(line,end='')    #按行读