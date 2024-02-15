import cap
from recognize import recognize
from insert import insert
import cv2
import keyboard


if __name__ == '__main__':
    
    # TODO: 当扳机按键被按下时，调用cap.capImage()函数
    def on_key_press(event):
        if event.name == 'c':
            print("Capturing image...")
            results = recognize(cap.capImage())
            print(results)
            results = list(set(results))
            insert(results)
            print(f"Successfully inserted {len(results)} submitted records.")
            

    keyboard.on_press(on_key_press)
    keyboard.wait('esc')
    exit()