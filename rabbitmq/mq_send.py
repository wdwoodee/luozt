import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host='10.10.7.32'))
channel=connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='hello world!')
print(" [x] sent 'hello world'")
connection.close()