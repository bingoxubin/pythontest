class Car:
    static_a = []   # 静态属性，所有对象共用一个

    def __init__(self):
        print("created")
        self.a = []    # 类似与构造方法，方法里面的表示成员变量  self有点类似与java的this

    def update(self):
        for i in range(len(self.a)):
            self.a[i] *= 2



a = Car()
b = Car()

a.static_a.append(1)
b.static_a.append(1)
print(a.static_a)
print(b.static_a)

a.a.append(1)
b.a.append(2)
print(a.a)
print(b.a)

a.update()
print(a.a)


# 继承
class Tool(Car):
    def __init__(self):
        print("Create Tool")
        super().__init__()   #调用父类的构造函数

t = Tool()
print(t.a)