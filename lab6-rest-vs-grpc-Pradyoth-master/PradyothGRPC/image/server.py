import grpc
from concurrent import futures
import time
import image_pb2
import image_pb2_grpc
from image import process

class ImageProcessServicer(image_pb2_grpc.ImageProcessServicer):

  def GetHeightAndWidth(self, request, context):
    response = image_pb2.OutParams()
    out = process(request.img)
    response.width = out['width']
    response.height = out['height']
    return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_ImageProcessServicer_to_server(ImageProcessServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

serve()
