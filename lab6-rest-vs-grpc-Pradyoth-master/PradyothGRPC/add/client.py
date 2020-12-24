import grpc
import sys
import add_pb2 as add__pb2
import add_pb2_grpc
address = sys.argv[1] + ":50051"
f = open("TIME.md", "w")
start_time = perf_counter()
count = int(sys.argv[3])
channel = grpc.insecure_channel(address)
stub = add_pb2_grpc.AddStub(channel)
args = add__pb2.Args(a=1, b=2)
for i in range(0,count):
	response = stub.Sum(args)
	print(response.c)
end_time = perf_counter()
print("Time in milli seconds:",(start_time - end_time)*1000)
f.write("Program execution time: {}\n".format((end_time - start_time)))
f.close()
