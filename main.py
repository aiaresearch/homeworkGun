import cap
import recognize
import insert
import keyboard


if __name__ == '__main__':
    
    # TODO: 当扳机按键被按下时，调用cap.capImage()函数
    def on_key_press(event):
        if event.name == 'c':
            print("Capturing image...")
            # 接收识别结果
            results = list(set(recognize.recognize_image(cap.capImage())))
            print('Read:',results)
            # 插入数据库
            insert.insert_submit(results)
            print(f"Successfully inserted {len(results)} submitted records.")

        elif event.name == 'q':
            print("Quitting...")
            exit()
            

    keyboard.on_press(on_key_press)
    keyboard.wait('esc')
    exit()