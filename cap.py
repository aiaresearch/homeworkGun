import cv2

def capImage():
    cap = cv2.VideoCapture(0)
    _, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()
    return frame

if __name__ == '__main__':
    capImage()