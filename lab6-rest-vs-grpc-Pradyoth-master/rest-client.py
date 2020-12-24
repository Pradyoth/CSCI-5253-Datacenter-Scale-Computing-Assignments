from __future__ import print_function
import requests
import json
import sys
# prepare headers for http request
#headers = {'content-type': 'image/png'}
# send http request with image and receive response
def add(arg):
        url = 'http://' + sys.argv[1] + ':5000/' +arg
        params = {'x':1, 'y':2}
        for i in range(0,1000):
                response = requests.get(url=url,params=params)
                print("Response is", response)
                print(response.text)
                print(sys.argv[0])
def image(arg):
# prepare headers for http request
        headers = {'content-type': 'image/png'}
        img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
# send http request with image and receive response
        image_url = 'http://' + sys.argv[1] + ':5000/api/' +arg
        for i in range(0,1000):
                response = requests.post(image_url, data=img, headers=headers)
                print("Response is", response)
                print(json.loads(response.text))
def main():
	file_output = open("TIMING.md","w")
	start_time = perf_counter()
        if sys.argv[2] == 'add':
                add(sys.argv[2])
        else:
                image(sys.argv[2])
	end_time = perf_counter()
	file_output.write("Elapsed time is {}\n".format(end_time - start_time))
if __name__ == "__main__":
	main()


