import pika
# 端口：http://localhost:15672/


# 1.应答参数

#  默认应答 auto_ack
#  问题：存在数据丢失的问题，比如callback函数里因为某原因（比如语法错误）报错，数据实际已经取出但是无法打印或进行后续操作，此时重启后数据丢失
#  解决方案：auto_ack=False 改为手动应答,在callback函数里加上下面一行确保运行无错的时候才删除
"""
auto_ack=False
ch.basic_ack(delivery_tag=method.delivery_tag)
"""

#  手动会牺牲效率，但是数据更安全


# 2.持久化参数

#  为了解决的问题：如果生产者将信息存到了rabbit服务器，此时服务器崩了，那么内存里的所有数据都会消失
#  解决方案：存到磁盘

"""
channel.queue_declare(queue='hello2', durable=True)
channel.basic_publish(exchange='',
                      routing_key="hello2",
                      body="hello world",
                      properties=pika.BasicProperties(
                         delivery_mode = 2
                      ))
"""


# 3.交换机模式
# -发布订阅
#  流程是生产者创建交换机，（交换机类似容器），消费者创建队列，（可以有多个消费者），分别用各自创建的队列绑定交换机，从而接受信息
#  生产者产生信息的时候，每个进程每个应用都会拿到一份数据

# 4.分发参数
#  在多个消费者的情况下，默认规则是轮询分发，你一个我一个，依次分发
#  方式不好，用的不多；可能存在的问题：分配不均衡，不公平，运行快的得等运行慢的
#  结局方案：公平分发
"""
Fair dispatch
在消费者端加上：实现公平分发，谁快谁先拿
channel.basic_qos(prefetch_count=1)
"""

# 5.交换机-关键字模式
# 在生产者每次往服务器发送内容的时候多指定一个关键词，消费者获取内容的时候需要先指定关键词，关键词必须完全一致才能成功获取到内容

# 6.交换机-通配符模式
# 跟关键字模式相比就是使用了正则，关键词更模糊一点，只有两类#和*。
# #匹配1个或多个字符，*匹配一个字符