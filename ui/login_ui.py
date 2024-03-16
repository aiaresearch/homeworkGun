# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

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

