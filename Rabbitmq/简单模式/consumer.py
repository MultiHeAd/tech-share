import pika

"""
链接mq，监听队列，回调函数callback
"""

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello3',durable=True)

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

    #添加下面一句可以确保程序在运行的时候无错才删除
    ch.basic_ack(delivery_tag=method.delivery_tag)


#  确定监听数列，基本的消费，数列是hello，一旦能有数据立刻执行callback函数,auto_ack=True是默认参数简单模式无需修改
channel.basic_consume(queue='hello3',
                      auto_ack=False,
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')

#  开始执行
channel.start_consuming()