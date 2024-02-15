import cap
from recognize import recognize
from insert import insert
import cv2
import keyboard


if __name__ == '__main__':
    
    while True:
        # TODO: 当扳机and按键被按下时，调用cap.capImage()函数
        if cv2.waitKey(1) & 0xFF == ord('c'):
            print("Capturing image...")
            results = recognize(cap.capImage())
            print(results)
        #     results = list(set(results))

        #     insert(results)
        #     print(f"Successfully inserted {len(results)} submitted records.")
        
        # if (cv2.waitKey(1) & 0xFF) == ord('q'):
        #     break
    