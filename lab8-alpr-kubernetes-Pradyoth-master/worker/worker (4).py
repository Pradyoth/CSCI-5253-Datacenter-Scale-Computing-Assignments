from openalpr import Alpr
import sys
import pika
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import redis

alpr = Alpr('us', "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("md")


connection = pika.BlockingConnection(
    pika.ConnectionParameters("rabbitmq-deployment"))
channel = connection.channel()

redis_all_info = redis.Redis("redis-deployment",db=1)
redis_filename = redis.Redis("redis-deployment",db=2)
redis_license = redis.Redis("redis-deployment",db=3)

def get_exif_data(image):
    """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for gps_tag in value:
                    sub_decoded = GPSTAGS.get(gps_tag, gps_tag)
                    gps_data[sub_decoded] = value[gps_tag]

                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
    return exif_data


def _convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    deg_num, deg_denom = value[0]
    d = float(deg_num) / float(deg_denom)

    min_num, min_denom = value[1]
    m = float(min_num) / float(min_denom)

    sec_num, sec_denom = value[2]
    s = float(sec_num) / float(sec_denom)
    return d + (m / 60.0) + (s / 3600.0)


def get_lat_lon(exif_data, debug=False):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    lat = None
    lon = None

    if "GPSInfo" in exif_data:
        gps_info = exif_data["GPSInfo"]

        gps_latitude = gps_info.get("GPSLatitude")
        gps_latitude_ref = gps_info.get('GPSLatitudeRef')
        gps_longitude = gps_info.get('GPSLongitude')
        gps_longitude_ref = gps_info.get('GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":
                lat *= -1

            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon *= -1
    else:
        if debug:
            print("No EXIF data")
    print("Lat & Lon is %s, %s" %(lat, lon))
    return lat, lon

def getLatLon(image, debug=False):
    try:
        exif_data = get_exif_data(image)
        return get_lat_lon(exif_data, debug)
    except:
        print("Exception")
        return None, None

def callback(ch, method, properties, body):
    filename = properties.headers['filename']
    if 'md5' in properties.headers:
    	md5 = properties.headers['md5']
    else:
        md5 = '123465789'
    print(md5)
    f = open("output/" + filename ,"wb")
    f.write(body)
    lat, lon = getLatLon(body)
    results = alpr.recognize_file("output/" + filename)
    i = 0
    for plate in results['results']:
        i += 1
        print("Plate for %s" %(filename) )
        print("   %12s %12s" % ("Plate", "Confidence"))
        for candidate in plate['candidates']:
            prefix = "-"
            if candidate['matches_template']:
                prefix = "*"

            print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
            str1 = str(candidate['plate']) + ':' + str(candidate['confidence']) + ':' + str(lat) +':'+ str(lon)
            print(str1)
            str2 = str(candidate['plate'])
            redis_all_info.set(md5,str1)
            redis_license.set(str2,md5)
    f.close()
    ch.basic_ack(delivery_tag=method.delivery_tag)



channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
alpr.unload()




