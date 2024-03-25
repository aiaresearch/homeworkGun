import cv2
import numpy as np
import urllib.request

# Function to read frames from the ESP32-CAM
def read_frames(stream_url):
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
                cv2.imshow('Frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break

# URL of the video stream
stream_url = 'YOUR_STREAM_URL_HERE'

# Start reading frames
read_frames(stream_url)

# Clean up
cv2.destroyAllWindows()
