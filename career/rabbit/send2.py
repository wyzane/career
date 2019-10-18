import sys
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = conn.channel()

channel.queue_declare(queue='task_queue',
                      durable=True)  # 消息持久化，重启rabbitmq消息不会丢失

message = ' '.join(sys.argv[1:]) or "hello world"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # 使消息持久化
                      ))
print("send message: ", message)
conn.close()
