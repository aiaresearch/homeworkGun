import cap
import recognize
import insert


if __name__ == '__main__':
    
    cap.capture()

    result = recognize.recognize()
    result = list(set(result))

    insert.insert(result)
    print(f"Successfully inserted {len(result)} submitted records.")
    