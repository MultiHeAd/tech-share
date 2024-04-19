#  Publish/Subscribe
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


#  创建交换机，声明一个名为logs的交换机,fanout/direct/topic，发布订阅：fanout
channel.exchange_declare(exchange='logs', exchange_type='fanout')


#  跟简单模式下相比，routing_key为空了，exchange需要取值
#  向log交换机插入字符串"hello world"

message ="info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)


print(f" [x] Sent {message}")
connection.close()