import serial
import time
import serial.tools.list_ports
import cv2

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
    time.sleep(2)
    return selected_port