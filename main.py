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
from ui.register_ui import RegisterWindow

from cnocr import CnOcr
import json

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
import qt_material

cam = cap.Camera()
ocr = CnOcr(rec_model_name='number-densenet_lite_136-fc', det_model_name='en_PP-OCRv3_det', cand_alphabet='0123456789')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("作业提交系统")
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera)
        self.timer.start(1000 // 30)

        self.ui.triggerButton.clicked.connect(self.scan)
        self.ui.actionExit.triggered.connect(self.close)

    def update_camera(self):
        img = cam.capture()
        height, width, _ = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format.Format_BGR888)

        self.ui.lbCam.setPixmap(QPixmap.fromImage(qImg))
        self.ui.lbCam.setScaledContents(True)

    def update_homework(self):
        ...

    def scan(self):
        img = cam.capture()
        ids = ocr.ocr(img, det_kwargs={'min_box_size' : 10})
        message = ''
        for id in ids:
            message = message + ' ' + id['text']
        _ = QMessageBox()
        _.setWindowTitle("扫描结果")
        _.setText(f"扫描到 {message}")
        _.addButton(QMessageBox.StandardButton.Ok)
        _.exec()

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
        self.EXPIRE = False

        if self.detect_cfg_existence():
            self.token_check()
        
        self.ui.loginButton.clicked.connect(self.login_check)
        self.ui.registerButton.clicked.connect(self.redirect_to_register_window)
    
    def detect_cfg_existence(self):
        return os.path.exists("cache.json")

    def redirect_to_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()

    def redirect_to_main_window(self):
        self.close()
        self.main_window = MainWindow()
        self.main_window.show()

    def token_check(self):
        with open("cache.json", "r") as file:
            token = json.load(file)['token']
            with fetch_data.fetch_token_status(token) as response:
                if response.status_code == 200:
                    if response.json()['message'].endswith('successfully'):
                        self.redirect_to_main_window()
                elif response.status_code == 401 and self.EXPIRE == False:
                    self.EXPIRE = True
                    expireMessage = QMessageBox()
                    expireMessage.setWindowTitle("登录失败")
                    expireMessage.setText("登录过期，请重新登录！")
                    expireMessage.addButton(QMessageBox.StandardButton.Ok)
                    expireMessage.exec()


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
    qt_material.apply_stylesheet(app, theme='light_blue.xml')
    login_window = LoginWindow()
    login_window.show()
    if login_window.detect_cfg_existence():
        login_window.token_check()
    
    sys.exit(app.exec())

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
