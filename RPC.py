import pika
import random
import os

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

class Image(object):
    __slots__ = ["filename"]
    def __init__(self, filename):
        self.filename = filename

    @property
    def get(self):
        with open(self.filename, "rb") as f:
            data = f.read()
        return data

def on_request(ch, method, props, body):
    randomNumber = random.randint(0,100)
    dir_list = os.listdir('images')
    index = randomNumber % len(dir_list)
    file_name = dir_list[index]
    print(" [.] file_name: " + file_name)
    path = "/Users/hasansyed/Documents/CS-361-Microservice-for-partner/images/" + file_name
    image = Image(filename=path)
    data = image.get
    response = data

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()