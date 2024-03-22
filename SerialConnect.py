import serial
import time
import serial.tools.list_ports

def SelectSerialPort():
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("没有找到任何可用的串口！")
        return None

    sorted_ports = sorted(ports, key=lambda x: x.device)
    selected_port = sorted_ports[-1].device
    
    print(f"自动选择了串口 {selected_port}")
    return selected_port
BAUD_RATE = 9600
serial_port = SelectSerialPort()

if serial_port:
    try:
        ser = serial.Serial(serial_port, BAUD_RATE, timeout=1)
        time.sleep(1)

        print("开始读取数据...")
        try:
            while True:
                # 读取串口数据
                if ser.in_waiting > 0:
                    data = ser.readline().decode().strip()
                    print(data)  # 在控制台上显示接收到的数据
                    # 检查是否接收到特定的字符串
                    if data == "ButtonPressed":
                        print("开始拍摄")
                        ser.write("Received\n".encode())  # 向串口发送确认消息
        except KeyboardInterrupt:
            print("\n程序被用户中断。")
        finally:
            ser.close()
            print("串口已关闭。")
    except serial.SerialException:
        print(f"无法打开串口 {serial_port}，请检查配置。")
else:
    print("未选择任何串口，程序退出。")
