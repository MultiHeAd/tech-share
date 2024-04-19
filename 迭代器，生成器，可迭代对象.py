"""
迭代器需要定义__iter__和__next__两种方法
__iter__方法需要返回self，函数本身
__next__方法返回下一个数据，如果没有数据了，则抛出StopIteration的异常
"""

class IT(object):
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        print(0)
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration
        return self.counter

# next()是迭代器和生成器对象共有的方法，每次执行可以执行下一步操作

obj1 = IT()
v1 = next(obj1)
print(v1)

v2 = next(obj1)
print(v2)

# v3 = next(obj1)
# print(v3)


obj2 = IT()
for item in obj2:
    print(item)

#  obj1和obj2的区别在于obj1是直接调用next方法而obj2则是会先调用iter方法

#  生成器是特殊的迭代器



#  如果一个类中有__iter__方法且返回一个迭代器对象，则我们称这个类创造的对象为可迭代对象
