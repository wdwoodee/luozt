import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host='10.10.7.32'))
channel=connection.channel()
channel.queue_declare(queue='hello')

def callback(ch,method,properties,body):
    print("[x] received %r" % body)


channel.basic_consume(callback,queue='hello',no_ack=True)
print('[*]waiting for message to exit press CRTL+C')
channel.start_consuming()