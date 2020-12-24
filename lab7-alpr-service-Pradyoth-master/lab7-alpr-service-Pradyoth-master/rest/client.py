from __future__ import print_function
from time import perf_counter
import requests
import json
import sys

md5_hash = ['1acb43b6af19e8d90ea94d40f5b8e207', '6e70a8f60d91a2d221a8de81a60168fc', 'de51a09e30c8a617ad963141404d789c', '16316aa0fa2e657a5c5aa8a09b0f612e', '786d4d75e52cde3b292045265aa59a2c']

def image():
    headers = {'content-type': 'image/png'}
    file_names = ["images/beetle.jpg","images/car.jpg","images/geotagged.jpg","images/plate1.png","images/the-meat-car.jpg"]
    for i in range(0,5):
        img = open("images/"+file_names[i], 'rb').read()
        print(sys.argv[1])
        image_url = 'http://' + sys.argv[1] + ':5000/api/image/'+file_names[i]
        response = requests.put(image_url, data=img, headers=headers)
        print("Response is", json.loads(response.text))
        md5_hash.append(json.loads(response.text)['hash'])


def get_license():
    licenses = ['3309DJN', 'GZTHE0A', 'S9SJLYY']
    for i in licenses:
        print(sys.argv[1])
        image_url = 'http://' + sys.argv[1] + ':5000/license/'+ i
        response = requests.get(image_url)
        print(json.loads(response.text))


def get_all_info():
    for value in md5_hash:
        print(value)
        if value is not None:
            print('calling')
            image_url = 'http://' + sys.argv[1] + ':5000/hash/'+ value
            response = requests.get(image_url)
            print(json.loads(response.text))



image()
get_all_info()
get_license()


