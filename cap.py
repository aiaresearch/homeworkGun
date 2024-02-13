import cv2
import numpy as np

def capImage():
    cap = cv2.VideoCapture(0)
    _, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()
    return np.array(frame)

if __name__ == '__main__':
    while True:
        img = capImage()
        cv2.imshow('Captured Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cv2.destroyAllWindows()