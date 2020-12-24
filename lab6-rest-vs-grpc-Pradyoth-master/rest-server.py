from flask import Flask, request, Response
import jsonpickle
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
@app.route('/add', methods=['GET'])
def test1():
     a = int(request.args.get('x'))
     b = int(request.args.get('y'))
     return str(a+b)
# route http posts to this method
@app.route('/api/image', methods=['POST'])
def test():
    r = request
    # convert the data to a PIL image type so we can extract dimensions
    try:
        ioBuffer = io.BytesIO(r.data)
        img = Image.open(ioBuffer)
    # build a response dict to send back to client
        response = {
            'width' : img.size[0],
            'height' : img.size[1]
            }
    except:
        response = { 'width' : 0, 'height' : 0}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")
# start flask app
app.run(host="0.0.0.0", port=5000)
