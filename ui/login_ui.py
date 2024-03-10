# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        if not LoginWidget.objectName():
            LoginWidget.setObjectName(u"LoginWidget")
        LoginWidget.resize(664, 539)
        self.layoutWidget = QWidget(LoginWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(220, 170, 231, 171))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        # Username
        self.frameUsername = QFrame(self.layoutWidget)
        self.frameUsername.setStyleSheet("border: none;")
        self.frameUsername.setObjectName(u"frameUsername")
        self.frameUsername.setFrameShape(QFrame.StyledPanel)
        self.frameUsername.setFrameShadow(QFrame.Raised)
        self.layoutWidget2 = QWidget(self.frameUsername)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 198, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbUsername = QLabel(self.layoutWidget2)
        self.lbUsername.setObjectName(u"lbUsername")

        self.horizontalLayout_2.addWidget(self.lbUsername)

        self.lineUsername = QLineEdit(self.layoutWidget2)
        self.lineUsername.setObjectName(u"lineUsername")

        self.horizontalLayout_2.addWidget(self.lineUsername)

        self.gridLayout.addWidget(self.frameUsername, 0, 0, 1, 1)

        # Password
        self.framePassword = QFrame(self.layoutWidget)
        self.framePassword.setStyleSheet("border: none;")
        self.framePassword.setObjectName(u"framePassword")
        self.framePassword.setFrameShape(QFrame.StyledPanel)
        self.framePassword.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.framePassword)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 197, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbPassword = QLabel(self.layoutWidget1)
        self.lbPassword.setObjectName(u"lbPassword")

        self.horizontalLayout.addWidget(self.lbPassword)

        self.linePassword = QLineEdit(self.layoutWidget1)
        self.linePassword.setObjectName(u"linePassword")

        self.horizontalLayout.addWidget(self.linePassword)


        self.gridLayout.addWidget(self.framePassword, 1, 0, 1, 1)

        # Button
        self.frameButton = QFrame(self.layoutWidget)
        # self.frameButton.setStyleSheet("border: none;")
        self.frameButton.setObjectName(u"frameButton")
        self.frameButton.setFrameShape(QFrame.StyledPanel)
        self.frameButton.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameButton)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loginButton = QPushButton(self.frameButton)
        self.loginButton.setObjectName(u"loginButton")

        self.verticalLayout.addWidget(self.loginButton)

        self.gridLayout.addWidget(self.frameButton, 2, 0, 1, 1)


        self.framePassword.raise_()
        self.frameButton.raise_()
        self.frameUsername.raise_()

        # Label
        self.lbWelcome = QLabel(LoginWidget)
        self.lbWelcome.setObjectName(u"lbWelcome")
        self.lbWelcome.setGeometry(QRect(180, 80, 321, 61))
        font = QFont()
        font.setPointSize(52)
        self.lbWelcome.setFont(font)


        self.retranslateUi(LoginWidget)


        QMetaObject.connectSlotsByName(LoginWidget)
    # setupUi

    def retranslateUi(self, LoginWidget):
        LoginWidget.setWindowTitle(QCoreApplication.translate("LoginWidget", u"Form", None))
        self.lbUsername.setText(QCoreApplication.translate("LoginWidget", u"\u7528\u6237\u540d:", None))
        self.lbPassword.setText(QCoreApplication.translate("LoginWidget", u"\u5bc6\u7801:", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWidget", u"\u767b\u5f55", None))
        self.lbWelcome.setText(QCoreApplication.translate("LoginWidget", u"Welcome!", None))
    # retranslateUi

