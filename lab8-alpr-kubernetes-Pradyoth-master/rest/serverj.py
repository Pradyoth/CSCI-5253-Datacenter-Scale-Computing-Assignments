from flask import Flask, request, Response
import jsonpickle
import numpy as np
import io
from PIL import Image
import hashlib
import pika
import logging
import sys
import redis


app = Flask(__name__)

redis_all_info = redis.Redis(host='10.128.0.63', port=6379, db=1)
redis_filename = redis.Redis(host='10.128.0.63', port=6379, db=2)
redis_license = redis.Redis(host='10.128.0.63', port=6379, db=3)

# md5 -> license:confidence:lat:lon
# filename -> md5
# license -> md5

@app.route('/api/image/<file_names>', methods=['PUT'])
def test(file_names):
    # f = open("../images/"+file_names,"rb")
    # i = f.read()
    logging.basicConfig()


    try:
        data = request.data
        print(type(data))
        md5hash = hashlib.md5(data)
        md5_message = md5hash.hexdigest()
        print(file_names, md5_message)
        redis_filename.set(file_names, md5_message)
        print(redis_filename.get(file_names))
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='10.128.0.59'))
        channel = connection.channel()
        channel.queue_declare(queue='task_queue', durable=True)
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=data,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
                headers = {'filename':file_names, 'md5': md5_message}
            ))
        print(" [x] Sent %r" % md5_message)
        connection.close()
        response = {
            'hash' : md5_message
            }
    except:
        response = { 'hash': None}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/license/<license>', methods=['GET'])
def get_license(license):
    try:
        info = redis_license.get(license)
        info = info.decode('utf-8') if info else None
        response = {
            'images' : info
            }
    except:
        response = {'images': None}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/hash/<check_sum>', methods=['GET'])
def get_all_info(check_sum):
    try:
        info = redis_all_info.get(check_sum)
        info = info.decode('utf-8') if info else None
        print(info)
        response = {
            'info' : info
            }
    except:
        response = {'info': None}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")


app.run(host="0.0.0.0", port=5000)

