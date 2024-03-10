import sys
import os
sys.path.append(os.path.dirname(__file__))
import util.cap as cap
from util.fetch import fetch_data
from util.insert import insert_submit
import numpy as np
import cv2
import requests
from cnocr import CnOcr
from ui.login_ui import Ui_LoginWidget

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QGuiApplication, QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QScreen)
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget, )

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWidget()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")
        self.center()


        self.lbBackground = QLabel(self)
        self.lbBackground.setPixmap(QPixmap("./ui/resources/zh1z.png"))
        self.lbBackground.setScaledContents(True)
        self.lbBackground.show()
        self.lbBackground.lower()

        self.ui.loginButton.clicked.connect(self.login_check)

    def login_check(self):
        username = self.ui.lineUsername.text()
        password = self.ui.linePassword.text()
        if fetch_data.fetch_login_status(username, password):
            self.close()
            self.main_window = MainWindow()
            self.main_window.show()
        else:
            ... # TODO: Show error message

    def center(self):
        # 获取主屏幕对象
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()

        # 获取窗口的尺寸
        window_geometry = self.frameGeometry()

        # 计算窗口居中时的左上角坐标
        x = screen_geometry.center().x() - window_geometry.width() / 2
        y = screen_geometry.center().y() - window_geometry.height() / 2

        # 移动窗口到居中位置
        self.move(x, y)
            
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gun Detection")
        self.setFixedSize(1280, 720)
        self.label = QLabel(self)
        self.label.setFixedSize(1280, 720)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Press space to capture image")
        self.label.show()


           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec()

# if __name__ == '__main__':
#     cam = cap.Camera()
#     ocr = CnOcr(rec_model_name='number-densenet_lite_136-fc', det_model_name='en_PP-OCRv3_det', cand_alphabet='0123456789')

    
#     # TODO: Implement physical trigger driver
#     def on_key_press(event):
#         if event == Key.space:
#             print("Capturing image...")
#             img = cam.capture()
#             print(img.shape)
#             cv2.imshow("Image", img)
#             ret = ocr.ocr(img, det_kwargs={'min_box_thresh' : 0.5})
#             results = [d['text'] for d in ret if 'text' in d]
#             results = list(set(results))
#             insert_submit(results)
#             # print(f"Successfully inserted {len(results)} submitted records.")

#         elif event == Key.esc:
#             print("Quitting...")
#             exit()
            

#     with Listener(on_press=on_key_press) as listener:
#         listener.join()
