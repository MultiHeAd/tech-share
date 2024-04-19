import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs3', exchange_type='topic')

# 系统会随机给一个唯一名字
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
print(queue_name)


# 和发布订阅模式相比，要补充一个关键词，如果是绑定多个关键词一定要写多次，可以用for循环
channel.queue_bind(exchange='logs3', queue=queue_name, routing_key='usa.#')
# channel.queue_bind(exchange='logs2', queue=queue_name, routing_key='info')
# channel.queue_bind(exchange='logs2', queue=queue_name, routing_key='warning')

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] {body}")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()