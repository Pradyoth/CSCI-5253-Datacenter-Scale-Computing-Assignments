import grpc
import sys
import image_pb2 as image__pb2
import image_pb2_grpc
from time import perf_counter

address = sys.argv[1] + ":50052"
f = open("TIME.md", "w")
start_time = perf_counter()
count = int(sys.argv[3])
channel = grpc.insecure_channel(address)
stub = image_pb2_grpc.ImageProcessStub(channel)
img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
args = image__pb2.ImageMsg(img=img)
for i in range(0,count):
	response = stub.GetHeightAndWidth(args)
	print(response.width, " & ", response.height)
end_time = perf_counter()
print("Time in milli seconds:",(start_time - end_time)*1000)
f.write("Program execution time: {}\n".format((end_time - start_time)))
f.close()

