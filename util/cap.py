import cv2

class Camera:
    
    def __init__(self, source=0) -> None:
        self.source = source
        try:
            self.cap = cv2.VideoCapture(source)
            self.capture() # Warm up
        except Exception:
            raise Exception(f"Camera: Failed to open source {source}")

    def capture(self, num_retry=2):
        for _ in range(num_retry):
            _, frame = self.cap.read()
            if frame.shape[0] > 0 and frame.shape[1] > 0:
                return frame

        raise Exception(f"Camera: Failed to read from source {self.source} after retrying {num_retry} times.")
    
    def __del__(self):
        self.cap.release()

if __name__ == '__main__':
    cam = Camera()
    while True:
        img = cam.capture()
        cv2.imshow('Captured Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cv2.destroyAllWindows()