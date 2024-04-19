# def add(a: int, b: int) -> int:
#     return a + b
# 声明不是强制执行
# result = add(1,1.5)
# print(result)

# def squared_numbers(nums):
#     for i in nums:
#         yield i**2
#
# nums = [1,2,3,4,5]
# squared_numbers = (i*i for i in nums)
# print(squared_numbers)


def foo():
    yield 2
    yield 2

def func():
    yield 1
    yield from foo()
    yield 1

# gen = func()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for item in func():
    print(item)


