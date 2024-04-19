# import multiprocessing
#
# def task():
#     pass
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=task)
#     p1.start()
#
#
# #  进程启动代码需要写在name=main下面，关于底层操作系统，spawn必须如此，fork则无所谓
# #  windows只支持spawn，mac都支持，fork会复制主进程的全部资源，spawn则不会
# #  如果spawn中想要复制可以通过传参的方法,args
#

# import multiprocessing
# count = multiprocessing.cpu_count()
# print(count) #  输出16  实际是8核

import time
import multiprocessing


def task(lock):
    print("开始")
    lock.acquire()
    #假设文件只保存了一个值10
    with open('fl.txt',mode='r',encoding='utf-8') as f:
        current_num = int(f.read())

    print('排队抢票中。。')
    time.sleep(0.5)
    current_num-=1

    with open('fl.txt',mode='w',encoding='utf-8') as f:
        f.write(str(current_num))
    lock.release()

if __name__ == '__main__':
    lock = multiprocessing.RLock()

    for i in range(10):
        p = multiprocessing.Process(target=task,args=(lock,))
        p.start()
    #线程锁不能当参数传，但是进程锁可以

    time.sleep(7)

####协程比线程更节省资源，但是开发难度大，可以用来增加并发量，协程只有一个进程
#一般用协程发请求，不处理数据；放到队列或数据库会用其他方式处理

