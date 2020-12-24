from time import perf_counter
import requests
import json
import sys

md5_hash = ['1acb43b6af19e8d90ea94d40f5b8e207', '6e70a8f60d91a2d221a8de81a60168fc', 'de51a09e30c8a617ad963141404d789c', '16316aa0fa2e657a5c5aa8a09b0f612e', '786d4d75e52cde3b292045265aa59a2c']



ip = sys.argv[1]
api = sys.argv[2]
image_file = sys.argv[3]

def image():
    headers = {'content-type': 'image/png'}
    # file_names = ["beetle.jpg","car.jpg","geotagged.jpg","plate1.png","the-meat-car.jpg"]
    img = open(image_file, 'rb').read()
    _, image_file_name = image_file.split("/")
    image_url = 'http://' + ip + ':5000/api/image/'+ image_file_name
    response = requests.put(image_url, data=img, headers=headers)
    print(response.text)
    print("Response of image api is ", json.loads(response.text))
    md5_hash.append(json.loads(response.text)['hash'])


def get_license():
    licenses = ['3309DJN', 'GZTHE0A', 'S9SJLYY']
    for i in licenses:
        image_url = 'http://' + sys.argv[1] + ':5000/license/'+ i
        response = requests.get(image_url)
        print("Response of license api is",json.loads(response.text))


def get_all_info():
    for value in md5_hash:
        if value is not None:
            image_url = 'http://' + sys.argv[1] + ':5000/hash/'+ value
            response = requests.get(image_url)
            print("Response of all info api is",json.loads(response.text))



if api == 'image':
    image()


