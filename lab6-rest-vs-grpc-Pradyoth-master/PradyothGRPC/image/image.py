from PIL import Image
import io

def process(img):
	ioBuffer = io.BytesIO(img)
	img = Image.open(ioBuffer)
	response = {
	    'width' : img.size[0],
	    'height' : img.size[1]
	    }
	return response