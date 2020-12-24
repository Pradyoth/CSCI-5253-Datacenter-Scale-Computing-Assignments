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

redis_md5_to_license = redis.Redis(host='10.128.0.63', port=6379, db=1)
redis_filename_to_hash = redis.Redis(host='10.128.0.63', port=6379, db=2)
redis_license_to_md5 = redis.Redis(host='10.128.0.63', port=6379, db=3)

# md5 -> license:confidence:lat:lon
# filename -> md5
# license -> md5

@app.route('/api/image/<file_name>', methods=['PUT'])
def test(file_name):
    # f = open("../images/"+file_name,"rb")
    # i = f.read()
    logging.basicConfig()


    try:
        data = request.data
        md5checksum = hashlib.md5(data)
        md5_hex = md5checksum.hexdigest()
        print(file_name, md5_hex)
        redis_filename_to_hash.set(file_name, md5_hex)
        print(redis_filename_to_hash.get(file_name))
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='10.128.0.59'))
        channel = connection.channel()
        channel.queue_declare(queue='toWorker', durable=True)
        channel.basic_publish(
            exchange='',
            routing_key='toWorker',
            body=data,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
                headers = {'filename':file_name, 'md5': md5_hex}
            ))
        print(" [x] Sent %r" % md5_hex)
        connection.close()
        response = {
            'hash' : md5_hex
            }
    except:
        response = { 'hash': None}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/license/<license>', methods=['GET'])
def get_license(license):
    try:
        info = redis_license_to_md5.get(license)
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
        info = redis_md5_to_license.get(check_sum)
        info = info.decode('utf-8') if info else None
        print(info)
        response = {
            'information' : info
            }
    except:
        response = {'information': None}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")


app.run(host="0.0.0.0", port=5000)

