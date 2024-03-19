import serial

# 打开 COM3，将波特率配置为9600, 读超时时间为1秒
ser = serial.Serial(port="COM3", baudrate=9600, timeout=1)
if ser.isOpen():
    print("Serial port opened successfully:"+ser.name)

# 读取串口输入信息并输出。
while True:
    com_input = ser.read(1)
    if len(com_input) == 1 and com_input[0] == 16:   # 如果读取结果非空，则输出
        print("Button pressed")
        