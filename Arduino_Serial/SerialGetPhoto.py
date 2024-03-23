import serial
import io
from PIL import Image

# 配置串口连接
ser = serial.Serial('COM12', 115200)  # 修改'COM端口号'为实际的串口号

try:
    while True:
        # 读取串口数据（这里假设JPEG数据已经完整接收，你可能需要根据实际情况处理数据流）
        imageData = ser.read(10)  # '大小'是预期读取的字节数，可能需要调整

        # 使用BytesIO从接收的数据中创建一个流
        imageStream = io.BytesIO(imageData)

        # 使用Pillow加载这个流作为图像
        image = Image.open(imageStream)

        # 显示图像
        image.show()

        # 可选：等待或者在这里加入逻辑以控制何时读取下一帧图像
        # 例如，使用input("Press Enter to continue...")等待用户交互

except KeyboardInterrupt:
    # 处理Ctrl+C，优雅地关闭串口连接
    print("程序被用户中断，正在退出...")
    ser.close()