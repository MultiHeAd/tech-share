import asyncio
"""
asyncio遇到IO阻塞自动切换，不用等着，自动切换别的部分，协程。
"""

"""协程开发"""


# async def fetch(session,url):
#     print("发送请求",url)
#     async with session.get(url, verify_ssl=False) as response:
#         content = await response.content.read()
#         file_name = url.split("_")[-1]
#         with open(file_name, 'wb') as f:
#             f.write(content)
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         url_list = [
#             'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohome_car_ChsEe12AXQ6AOOH_AAFocMS8nzu621.jpg' ,
#             'https://www3.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohome_car_ChcCSV2BBICAUntfAADjJFd6800429.jpg' ,
#             'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohome_car_ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
#         ]
#
#         tasks =[asyncio.create_task(fetch(session,url) for url in url_list)]
#         await asyncio.wait(tasks)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


"""异步编程"""
"""
事件循环：死循环
检测并执行某些代码

"""



# #  去生成或获取一个事件循环
# loop = asyncio.get_event_loop()
#
# #  将任务放到“任务列表”
# loop.run_until_complete()

"""快速上手"""
"""
协程函数
在函数前面加上async def的函数名
协程对象
执行协程函数（）实例化得到的就是协程对象
"""
# async def func():
#     print("协程运行")
#
# result = func()

#  注意创建协程对象，内部代码不会执行，有点像类

# loop = asyncio.get_event_loop()
# loop.run_until_complete(result)
# asyncio.run(result)
#这个是python3.7以上才有的特殊方法本质上执行上面两行


# await 后面需要跟可以等待的对象(协程对象，Future,Task对象

# async def func():
#     print("协程运行")
#
#     #  等待两秒后拿到结果
#     response = await asyncio.sleep(2)
#     print("运行结束")
#
#
# asyncio.run( func() )






# import asyncio
#
# async def func1():
#     print("start")
#     await asyncio.sleep(2)
#     print("stop")
#     return ("结束")
#
# async def func2():
#     print("执行中")
#     response = await func1()
#     print("IO请求结束，结果为",response)
#
# obj = func2()
# asyncio.run(obj)



"""Future对象"""
# async def main():
#     loop = asyncio.get_running_loop()
#
#     fut = loop.create_future()
#
#     await fut
#
# asyncio.run(main())

"""操作redis"""








