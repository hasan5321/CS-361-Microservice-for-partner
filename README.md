# CS-361-Microservice-for-partner

After cloning this repo

We are using the RPC model that is depicted in the rabbit mq docs. This is where the client sends and receives a message to the service so that the service can receive and send a response back to the client. In this case the response will be a fileName for a image containing a motivational quote.

Requesting and receiving Data using RabbitMQ server:

- First install pika using python3 -m install pika --upgrade
- install rabbitmq using methods show here https://www.rabbitmq.com/download.html
- start rabbitmq (commands should be in docs)
- open up cmd line and run RPC.py so it can start receiving messages
- Would recommend following this guide to setup client to send and receive messages https://www.rabbitmq.com/tutorials/tutorial-six-python.html

UML Sequence Diagram:

- C is the client
- S is the server
- C request data from S
- S replies to C

![plot](./UML.png)
