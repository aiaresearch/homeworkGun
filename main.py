import cap
from recognize import recognize
import insert
import cv2


if __name__ == '__main__':
    
    while True:
        if (cv2.waitKey(1) & 0xFF) == ord('c'):
            results = recognize(cap.capImage())
            results = list(set(results))

            insert.insert(results)
            print(f"Successfully inserted {len(results)} submitted records.")
        
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    