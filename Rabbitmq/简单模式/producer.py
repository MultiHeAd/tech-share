#producer

import pika


# chanel是控制对象
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# # 创造对象然后申明名称叫hello
# channel.queue_declare(queue='hello2')


#  持久化需要加上durable=true，并且名字不能用已经创建了的队列
channel.queue_declare(queue='hello3',durable=True)

# 插入，交换机不存在因为是简单模式，指定队列hello，数据是hello world
# properties=pika.BasicProperties(delivery_mode=2)赋予属性存到硬盘
channel.basic_publish(exchange='',
                      routing_key='hello3',
                      body='Hihihihi!',properties=pika.BasicProperties(delivery_mode=2))

print(" [x] Sent 'Hihihihi!'")
