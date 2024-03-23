import cv2

def capture_frame(video_url):
    # 使用OpenCV捕获视频流
    cap = cv2.VideoCapture(video_url)

    if not cap.isOpened():
        print("无法打开视频流")
        return

    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        cv2.imwrite('captured_frame.jpg', frame)
        cv2.waitKey(0)
    else:
        print("无法读取视频流")

    cap.release()
    cv2.destroyAllWindows()

# 视频流的URL
video_url = 'http://192.168.134.14/mjpeg/1'
capture_frame(video_url)