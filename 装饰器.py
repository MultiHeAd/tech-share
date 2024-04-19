# def func():
#     print("func函数")
#     value = [1,2,3,4]
#     return value
#
# def outer(orign):
#     def inner():
#         print('before')
#         res=orign()
#         print('after')
#         return res
#     return inner()
#
#
# func=outer(func)
# result = func
# print(result)

#  @函数
"""

def func1():
    xxxx

@func1
def func2():
    xxx


会先执行func2，然后把func2返回的值作为参数传给func1然后执行func1最后再将func1的值赋回给func2

"""
import functools


# def outer(orign):
#     def inner():
#         print('before')
#         res=orign()
#         print('after')
#         return res
#     return inner()
#
# @outer
# def func():
#     print("func函数")
#     value = [1,2,3,4]
#     return value
#
#
# result = func
# print(result)
#


# """如果函数有参数"""
# def outer(origin):
#     def inner(*args, **kwargs):
#         print("装饰开始")
#         res = origin(*args, **kwargs)
#         print("装饰结束")
#         return res
#     return inner
#
#
# @outer
# def func(*args, **kwargs):
#     print(args,kwargs)
#
# func(1,2,3, a1=3,a2=4,)
# func(ac=14)
# func(5,6,7)






# from flask import Flask
#
# app = Flask(__name__)
#
# def outer(origin):
#     def inner(*args, **kwargs):
#         # 先判断用户是否已经登录，如果未登录，则返回登录页面
#         res = origin(*args, **kwargs)
#         return res
#     return inner
#
# def index():
#     return "首页"
#
# @outer
# def info():
#     return "用户信息"
# @outer
# def order():
#     return ("订单信息")
#
# app.add_url_rule('/', view_func=index)
# app.add_url_rule('/info/', view_func=info)
# app.add_url_rule('/order/', view_func=order)
#
# app.run()

#  装饰器的本质是运行里边的内容，就是inner

# import functools
# def outer(origin):
#     #  只要加上 @functools.wraps(origin) 可以获取原来函数的名字和注释
#     @functools.wraps(origin)
#     def inner(*args, **kwargs):
#         #打印装饰器参数
#         print("装饰开始")
#         res = origin(*args, **kwargs)
#         print("装饰结束")
#         return res
#     return inner
#
#
# @outer
# def func(*args, **kwargs):
#     """打印动态参数"""
#     print(args,kwargs)
#
# func(1,2,3, a1=3,a2=4,)
# func(ac=14)
# func(5,6,7)
#
# print(func.__name__,func.__doc__)


import os
import time
import functools

def gard(function):
    @functools.wraps(function)
    def inner(path):
        folder_path = path.rsplit('/',1)[0]
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        res = function(path)
        return res
    return inner

def timer(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        message = "运行时间：{}".format(end_time - start_time)
        print(message)
        return result
    return inner




@timer
def write_user_info(path):
    file_obj = open(path, mode='a',encoding='utf-8')
    file_obj.write('？？？')
    file_obj.close()



write_user_info('E:/python/基础练习/test.txt')

