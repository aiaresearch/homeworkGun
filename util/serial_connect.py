import serial
import time
import serial.tools.list_ports


BAUD_RATE = 9600

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
    selected_port = Search_newport(initial_ports)
    return selected_port



def detect_button_press():
    with select_serial_port() as serial_port:
        if not serial_port:
            raise Exception("未检测到串口")
        ser = serial.Serial(serial_port, BAUD_RATE, timeout=1)
        time.sleep(1)
        try:
            while True:
                if ser.in_waiting > 0:
                    data = ser.readline().decode().strip()
                    print(data)  # 显示接收到的数据
                    if data == "ButtonPressed":
                        ser.write("Received\n".encode())  # 向串口发送确认消息
                        return True
        except KeyboardInterrupt:
            raise Exception()
        except serial.SerialException as e:
            raise Exception()
        finally:
            ser.close()
