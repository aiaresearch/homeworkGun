import util.cap as cap
import util.recognize as recognize
import util.insert as insert
import keyboard


if __name__ == '__main__':
    cam = cap.Camera()
    
    # TODO: Implement physical trigger driver
    def on_key_press(event):
        if event.name == 'c':
            print("Capturing image...")
            results = recognize(cam.capture())
            print(results)
            results = list(set(results))
            insert(results)
            print(f"Successfully inserted {len(results)} submitted records.")

        elif event.name == 'q':
            print("Quitting...")
            exit()
            

    keyboard.on_press(on_key_press)
    keyboard.wait('esc')
