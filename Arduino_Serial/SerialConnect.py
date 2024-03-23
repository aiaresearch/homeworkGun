import serial
import time
import serial.tools.list_ports

def PortList():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

def Search_newport(initial_ports):
    while True:
        current_ports = PortList()
        new_ports = list(set(current_ports) - set(initial_ports))
        if new_ports:
            return new_ports[0]  # 返回找到的第一个新串口
        time.sleep(1)  # 短暂等待后再次检查

def select_serial_port():
    initial_ports = PortList()
    print("等待扫描枪插入...")
    selected_port = Search_newport(initial_ports)
    print(f"检测到新串口，已选择 {selected_port}")
    return selected_port

BAUD_RATE = 9600
serial_port = select_serial_port()

if serial_port:
    try:
        ser = serial.Serial(serial_port, BAUD_RATE, timeout=1)
        time.sleep(1)
        print("开始读取数据...")
        try:
            while True:
                if ser.in_waiting > 0:
                    data = ser.readline().decode().strip()
                    print(data)  # 显示接收到的数据
                    if data == "ButtonPressed":
                        print("开始拍摄,请持稳设备。")
                        ser.write("Received\n".encode())  # 向串口发送确认消息
        except KeyboardInterrupt:
            print("\n程序被用户中断。")
        finally:
            ser.close()
            print("串口已关闭。")
    except serial.SerialException:
        print(f"无法打开串口 {serial_port}，请检查配置。")
else:
    print("未检测到新串口，程序退出。")