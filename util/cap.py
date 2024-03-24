import cv2
import numpy as np
import urllib.request

# Function to read frames from the ESP32-CAM
def read_frame(stream_url = 'http://192.168.31.23/mjpeg/1'):
    stream = urllib.request.urlopen(stream_url)
    bytes = b''
    while True:
        bytes += stream.read(1024)
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            # bytes = bytes[b+2:]
            frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            if frame is not None:
                return frame
            else:
                raise Exception('Failed to decode frame')