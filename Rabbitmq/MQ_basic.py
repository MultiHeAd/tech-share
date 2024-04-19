#  队列 特点：先进先出
import queue

# 创造一个最大存储十个元素的队列
q = queue.Queue(maxsize=10)

# 填数据
q.put(111)
q.put(222)
q.put(333)


print(q.get())  # 取到111因为111先进，如果重复到第四次，看block参数，如果该参数为true则是停住，只要加入新的参数则会打印；block为False则报empty错
#   print(q.get(block=False))
print(q.get())
print(q.get())
print(q.get())

#  MQ的三大好处：解耦，异步，流量削峰。常见的消息队列有ActiveMQ,RabbitMQ,Kafka,RocketMQ
#  外卖系统：
#  链式操作不可取，同步不可取，效率极低，并且如果出现错误，整个系统全部崩溃
#  并发操作的问题：1.没有做到"高内聚，低耦合"，开发的时候功能应该相对独立，不要受到影响
#  采用消息队列可以避免上面的问题，本质类似数据库；订单系统为生产者，生产出内容以后放到消息队列，骑士系统，商家系统，后台为消费者，监听队列中的内容，人手一份，取走后处理后续内容
#  消息队列打破了高耦合，其余系统不需要和订单系统联系，方便后续模块修改调用，这就是解耦




"""启动队列，插件，https://developer.aliyun.com/article/1134566"""