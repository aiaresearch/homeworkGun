# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListView,
    QMainWindow, QMenu, QMenuBar, QScrollArea,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.homeworkList = QListView(self.centralwidget)
        self.homeworkList.setObjectName(u"homeworkList")
        self.homeworkList.setGeometry(QRect(10, 20, 201, 531))
        self.lbCam = QLabel(self.centralwidget)
        self.lbCam.setObjectName(u"lbCam")
        self.lbCam.setGeometry(QRect(370, 50, 320, 240))
        self.lbCam.setPixmap(QPixmap(u"resources/zh1z.png"))
        self.lbCam.setAlignment(Qt.AlignCenter)
        self.lbText = QLabel(self.centralwidget)
        self.lbText.setObjectName(u"lbText")
        self.lbText.setGeometry(QRect(370, 20, 320, 16))
        self.lbText.setTextFormat(Qt.PlainText)
        self.lbText.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(370, 309, 320, 240))
        self.scrollArea.setWidgetResizable(True)
        self.SubmissionScroll = QWidget()
        self.SubmissionScroll.setObjectName(u"SubmissionScroll")
        self.SubmissionScroll.setGeometry(QRect(0, 0, 318, 238))
        self.submissionTable = QTableWidget(self.SubmissionScroll)
        self.submissionTable.setObjectName(u"submissionTable")
        self.submissionTable.setGeometry(QRect(0, 0, 320, 240))
        self.scrollArea.setWidget(self.SubmissionScroll)
        MainWindow.setCentralWidget(self.centralwidget)
        self.exitBar = QMenuBar(MainWindow)
        self.exitBar.setObjectName(u"exitBar")
        self.exitBar.setGeometry(QRect(0, 0, 800, 24))
        self.menuExit = QMenu(self.exitBar)
        self.menuExit.setObjectName(u"menuExit")
        MainWindow.setMenuBar(self.exitBar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.exitBar.addAction(self.menuExit.menuAction())
        self.menuExit.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.lbCam.setText("")
        self.lbText.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u753b\u9762", None))
        self.menuExit.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355", None))
    # retranslateUi

