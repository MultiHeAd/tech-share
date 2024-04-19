# class Person():
#     country = "中国"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print("我是{},今年{}岁".format(self.name, self.age))
#
#     @classmethod
#     def greet(cls):
#         print("定义了一个类方法")
#
#     @staticmethod
#     def f1():
#         print("定义了一个静态方法")
#
#     def __str__(self):
#         return self.name
#
# p1 = Person("张三",12)
# p1.country = "美国"
# print(p1)

#这样写 country是类变量，也就是默认不修改，而如果写到init里则变成了实例化变量，虽然可以设置默认值但是应该是可能需要修改的



# info = dict()
#
# info['key1'] = 123
# info['key2'] = 456
# print(info['key1'])


# with 对象 as f  在内部执行前先执行enter方法,f会赋值return的值； 缩进部分执行后会自动执行exit方法
# with obj as f:
#     print(456)
#     print(f)


# class Foo():
#     def __enter__(self):
#         print(123)
#         return 789
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("结束")
#
# obj = Foo()


"""
特殊方法：
__new__ 在init之前触发，创建空对象；平常写代码，一般会不写，但是实际会从父类执行
__call__ 对象+（）执行call
__str__  可以将对象转换为字符串
__dict__ 自动获取所有的类对象的实例变量，并将他们转换成字典格式
__getitem__ , __setitem__ , __delitem__ 让对象支持字典的三种操作
__enter__ , __exit__ 可以用来写一些在操作前后需要进行的内容
__add__  对象与对象之间进行相加
"""

# class num():
#     def __init__(self,name):
#         self.name = name
#
#     def __add__(self,other):
#         return self.name + " " + other.name
#
# n1 = num('alex')
# n2 = num('sb')
# n3 = n1+n2
# print(n3)

"""
内置函数补充

1.callable用来确认函数是否可以被执行
def func():
    pass
print( callable(func) )

2.super()用来调用继承类里的同名函数，和self正好是一对，self优先自己而super不找自己
class base():
    def msg(self, num):
        print(num + 1)

class func(base):
    def msg(self, num):
        super().msg(num + 2)

obj1 = func()
obj1.msg(1)  返回4
        
3.isinstance()判断对象是否是某个类或者是其子类的实例/issubclass()则是判断是否是继承关系，下面的就是Func和Base，Top的关系也是True
比如下面的用法：
class Top():
    pass
    
class Base(Top):
    pass

class Func(Base):
    pass
    
obj = Func()
print( Func(v1,Func) )  #True
print( Func(v1,Base) )  #True
print( Func(v1,Top) )  #True

"""







