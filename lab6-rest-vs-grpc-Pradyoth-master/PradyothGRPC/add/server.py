import grpc
from concurrent import futures
import time
import add_pb2
import add_pb2_grpc
from add import add

class AddServicer(add_pb2_grpc.AddServicer):

  def Sum(self, request, context):
    response = add_pb2.Output()
    response.c = add(request.a, request.b)
    return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_pb2_grpc.add_AddServicer_to_server(AddServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(80000)
    except KeyboardInterrupt:
        server.stop(0)

serve()
