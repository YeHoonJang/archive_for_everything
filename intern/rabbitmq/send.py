import pika

#로컬서버에 접속
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#큐 생성
channel.queue_declare(queue='hello')

channel.basic_publish(exchange = '',
                      routing_key = 'hello',
                      body = 'Hello World!')

print("Send Hello World!")

connection.close()