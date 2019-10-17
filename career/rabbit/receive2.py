import time
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = conn.channel()

channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep( body.count('.') )
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
