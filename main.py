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
from ui.main_window_ui import Ui_MainWindow

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot, QTimer)
from PySide6.QtGui import (QGuiApplication, QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QScreen)
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget, QMessageBox)

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
        with fetch_data.fetch_login_status(username, password) as response:
            print(response.status_code)
            if response.status_code == 200:
                token = response.json()['token']
                self.close()
                self.main_window = MainWindow(token)
                self.main_window.show()
            else:
                errorMessage = QMessageBox()
                errorMessage.setWindowTitle("登录失败")
                errorMessage.setText("用户名或密码错误！")
                errorMessage.addButton(QMessageBox.StandardButton.Ok)
                errorMessage.exec()

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
    def __init__(self, token):
        super().__init__()
        self.token = token
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("作业提交系统")
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera)
        self.timer.start(1000 // 30)


        self.ui.actionExit.triggered.connect(self.close)
    
    def update_camera(self):
        img = cam.capture()
        height, width, _ = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format.Format_BGR888)

        self.ui.lbCam.setPixmap(QPixmap.fromImage(qImg))
        self.ui.lbCam.setScaledContents(True)


           
if __name__ == '__main__':
    cam = cap.Camera(source=1)
    ocr = CnOcr(rec_model_name='number-densenet_lite_136-fc', det_model_name='en_PP-OCRv3_det', cand_alphabet='0123456789')
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
