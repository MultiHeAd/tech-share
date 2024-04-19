import threading

# loop = 10000000
#
# number = 0
#
# def _add(count):
#     global number
#     for i in range(count):
#         number += 1
#
# t = threading.Thread(target=_add, args=(loop,))
# t.start()
#
# #如果加上 t.join() 就是让主线程等到子线程执行完再继续走，也就是后面print一定会是1加到10000000的和
#
# print(number)

# class MyThread(threading.Thread):
#     def run(self):
#         print('执行此线程',self._args)
#
# t = MyThread(args=(100,))
# t.start()







#
# lock_object = threading.RLock()
#
# loop = 10000000
# number = 0
#
# def _add(count):
#     lock_object.acquire() #申请锁,注意锁必须用的是同一把锁，否则毫无意义
#     global number
#     for i in range(count):
#         number+=1
#     lock_object.release() #释放锁，不释放其他线程没法继续进行
#
# def _sub(count):
#     lock_object.acquire() #申请锁
#     global number
#     for i in range(count):
#         number-=1
#     lock_object.release() #释放锁，不释放其他线程没法继续进行
#
# t1= threading.Thread(target=_add, args=(loop,))
# t2= threading.Thread(target=_sub, args=(loop,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(number)
#
# #死锁就是互相竞争导致程序停止



import time
from concurrent.futures import ThreadPoolExecutor


def task(video_url,num):
    print("开始执行任务",video_url)
    time.sleep(5)

pool = ThreadPoolExecutor(10)

url_list = ["www.xxx-{}.com".format(i) for i in range(300)]


for url in url_list:
    pool.submit(task,url,2)

#可以加上
# pool.shutdown(True)
#表示等当前线程池里所有任务都执行完了再继续执行别的，如果不写则是每当一个线程执行完就替换成别的未执行的线程

print("END")
