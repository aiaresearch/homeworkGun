from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QGuiApplication, QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget, QMessageBox)
import os
import json
from ui.register_ui import RegisterWindow
from ui.main_window_ui import MainWindow
from util.request import request

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        if not LoginWidget.objectName():
            LoginWidget.setObjectName(u"LoginWidget")
        LoginWidget.resize(664, 539)
        self.lbWelcome = QLabel(LoginWidget)
        self.lbWelcome.setObjectName(u"lbWelcome")
        self.lbWelcome.setGeometry(QRect(180, 80, 321, 61))
        font = QFont()
        font.setPointSize(52)
        self.lbWelcome.setFont(font)
        self.widget = QWidget(LoginWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(222, 172, 251, 181))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameUsername = QFrame(self.widget)
        self.frameUsername.setObjectName(u"frameUsername")
        self.frameUsername.setFrameShape(QFrame.StyledPanel)
        self.frameUsername.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frameUsername)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 198, 35))
        self.usernameLayout = QHBoxLayout(self.layoutWidget)
        self.usernameLayout.setObjectName(u"usernameLayout")
        self.usernameLayout.setContentsMargins(0, 0, 0, 0)
        self.lbUsername = QLabel(self.layoutWidget)
        self.lbUsername.setObjectName(u"lbUsername")

        self.usernameLayout.addWidget(self.lbUsername)

        self.lineUsername = QLineEdit(self.layoutWidget)
        self.lineUsername.setObjectName(u"lineUsername")

        self.usernameLayout.addWidget(self.lineUsername)


        self.verticalLayout.addWidget(self.frameUsername)

        self.framePassword = QFrame(self.widget)
        self.framePassword.setObjectName(u"framePassword")
        self.framePassword.setFrameShape(QFrame.StyledPanel)
        self.framePassword.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.framePassword)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 197, 35))
        self.passwordLayout = QHBoxLayout(self.layoutWidget1)
        self.passwordLayout.setObjectName(u"passwordLayout")
        self.passwordLayout.setContentsMargins(0, 0, 0, 0)
        self.lbPassword = QLabel(self.layoutWidget1)
        self.lbPassword.setObjectName(u"lbPassword")

        self.passwordLayout.addWidget(self.lbPassword)

        self.linePassword = QLineEdit(self.layoutWidget1)
        self.linePassword.setObjectName(u"linePassword")

        self.passwordLayout.addWidget(self.linePassword)


        self.verticalLayout.addWidget(self.framePassword)

        self.frameButton = QFrame(self.widget)
        self.frameButton.setObjectName(u"frameButton")
        self.frameButton.setFrameShape(QFrame.StyledPanel)
        self.frameButton.setFrameShadow(QFrame.Raised)
        self.widget1 = QWidget(self.frameButton)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 10, 176, 37))
        self.buttonLayout = QHBoxLayout(self.widget1)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.loginButton = QPushButton(self.widget1)
        self.loginButton.setObjectName(u"loginButton")

        self.buttonLayout.addWidget(self.loginButton)

        self.registerButton = QPushButton(self.widget1)
        self.registerButton.setObjectName(u"registerButton")

        self.buttonLayout.addWidget(self.registerButton)


        self.verticalLayout.addWidget(self.frameButton)


        self.retranslateUi(LoginWidget)

        QMetaObject.connectSlotsByName(LoginWidget)
    # setupUi

    def retranslateUi(self, LoginWidget):
        LoginWidget.setWindowTitle(QCoreApplication.translate("LoginWidget", u"Form", None))
        self.lbWelcome.setText(QCoreApplication.translate("LoginWidget", u"Welcome!", None))
        self.lbUsername.setText(QCoreApplication.translate("LoginWidget", u"\u7528\u6237\u540d:", None))
        self.lbPassword.setText(QCoreApplication.translate("LoginWidget", u"\u5bc6\u7801:", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWidget", u"\u767b\u5f55", None))
        self.registerButton.setText(QCoreApplication.translate("LoginWidget", u"\u6ce8\u518c", None))
    # retranslateUi


class LoginWindow(QWidget):
    def __init__(self, cam, ocr):
        super().__init__()
        self.ui = Ui_LoginWidget()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")
        self.cam = cam
        self.ocr = ocr
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
        self.main_window = MainWindow(self.cam, self.ocr)
        self.main_window.show()

    def token_check(self):
        with open("cache.json", "r") as file:
            token = json.load(file)['token']
            response = request.fetch_token_status(token)
            if type(response) == dict:
                if response['message'].endswith('successfully'):
                    self.redirect_to_main_window()
            elif self.EXPIRE == False:
                self.EXPIRE = True
                expireMessage = QMessageBox()
                expireMessage.setWindowTitle("登录失败")
                expireMessage.setText("登录过期，请重新登录！")
                expireMessage.addButton(QMessageBox.StandardButton.Ok)
                expireMessage.exec()


    def login_check(self):
        username = self.ui.lineUsername.text()
        password = self.ui.linePassword.text()
        response = request.fetch_login_status(username, password)
        if type(response) == dict:
            token = response['token']
            with open("cache.json", "w") as file:
                json.dump({'token': token}, file)
            self.redirect_to_main_window()
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
