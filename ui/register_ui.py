# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.request import request

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget, QMessageBox)
from qfluentwidgets import FluentWindow, PushButton, LineEdit, TitleLabel, SubtitleLabel
from . import center, FrameView

class Ui_registerWindow(object):
    def setupUi(self, registerWindow):
        if not registerWindow.objectName():
            registerWindow.setObjectName(u"registerWindow")
        registerWindow.resize(450, 393)
        self.lbRegister = TitleLabel(registerWindow)
        self.lbRegister.setObjectName(u"lbRegister")
        self.lbRegister.setGeometry(QRect(120, 70, 221, 61))
        font = QFont()
        font.setPointSize(24)
        self.lbRegister.setFont(font)
        self.lbRegister.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(registerWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(110, 140, 241, 181))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.usernameFrame = FrameView(self.widget)
        self.usernameFrame.setObjectName(u"usernameFrame")
        self.widget1 = QWidget(self.usernameFrame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 211, 51))
        self.usernameLayout = QHBoxLayout(self.widget1)
        self.usernameLayout.setObjectName(u"usernameLayout")
        self.usernameLayout.setContentsMargins(0, 0, 0, 0)
        self.lbUsername = SubtitleLabel(self.widget1)
        self.lbUsername.setObjectName(u"lbUsername")

        self.usernameLayout.addWidget(self.lbUsername)

        self.inputUsername = LineEdit(self.widget1)
        self.inputUsername.setObjectName(u"inputUsername")

        self.usernameLayout.addWidget(self.inputUsername)


        self.verticalLayout.addWidget(self.usernameFrame)

        self.passwordFrame = FrameView(self.widget)
        self.passwordFrame.setObjectName(u"passwordFrame")
        self.layoutWidget = QWidget(self.passwordFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 211, 71))
        self.passwordLayout = QHBoxLayout(self.layoutWidget)
        self.passwordLayout.setObjectName(u"passwordLayout")
        self.passwordLayout.setContentsMargins(0, 0, 0, 0)
        self.lbPassword = SubtitleLabel(self.layoutWidget)
        self.lbPassword.setObjectName(u"lbPassword")

        self.passwordLayout.addWidget(self.lbPassword)

        self.inputPassword = LineEdit(self.layoutWidget)
        self.inputPassword.setEchoMode(LineEdit.EchoMode.Password)
        self.inputPassword.setObjectName(u"inputPassword")

        self.passwordLayout.addWidget(self.inputPassword)


        self.verticalLayout.addWidget(self.passwordFrame)

        self.registerButton = PushButton(self.widget)
        self.registerButton.setObjectName(u"registerButton")

        self.verticalLayout.addWidget(self.registerButton)


        self.retranslateUi(registerWindow)

        QMetaObject.connectSlotsByName(registerWindow)
    # setupUi

    def retranslateUi(self, registerWindow):
        registerWindow.setWindowTitle(QCoreApplication.translate("registerWindow", u"\u6ce8\u518c", None))
        self.lbRegister.setText(QCoreApplication.translate("registerWindow", u"\u6ce8\u518c", None))
        self.lbUsername.setText(QCoreApplication.translate("registerWindow", u"\u7528\u6237\u540d\uff1a", None))
        self.inputUsername.setText("")
        self.lbPassword.setText(QCoreApplication.translate("registerWindow", u"\u5bc6\u7801\uff1a", None))
        self.inputPassword.setText("")
        self.registerButton.setText(QCoreApplication.translate("registerWindow", u"\u6ce8\u518c", None))
    # retranslateUi

class RegisterWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_registerWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("RegisterWindow{background: rgb(255, 255, 255)} ")

        self.ui.registerButton.clicked.connect(self.register)
        center(self)


    def register(self):
        username = self.ui.inputUsername.text()
        password = self.ui.inputPassword.text()
        if username == "" or password == "":
            QMessageBox.warning(self, "警告", "用户名或密码不能为空！")
        else:
            request.fetch_register_status(username, password)
            QMessageBox.information(self, "成功", "注册成功！")