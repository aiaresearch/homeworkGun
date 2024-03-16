from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QTimer)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListView,
    QMainWindow, QMenu, QMenuBar, QScrollArea,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget, QPushButton, QMessageBox)


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
        self.lbCam.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbText = QLabel(self.centralwidget)
        self.lbText.setObjectName(u"lbText")
        self.lbText.setGeometry(QRect(370, 20, 320, 16))
        self.lbText.setTextFormat(Qt.TextFormat.PlainText)
        self.lbText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.capButton = QPushButton(self.centralwidget)
        self.capButton.setObjectName(u"capButton")
        self.capButton.setGeometry(QRect(250, 100, 101, 31))
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
        self.capButton.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444", None))
        self.menuExit.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355", None))
    # retranslateUi

class MainWindow(QMainWindow):
    def __init__(self, cam, ocr):
        super().__init__()
        self.cam = cam
        self.ocr = ocr
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("作业提交系统")
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera)
        self.timer.start(1000 // 30)

        self.ui.capButton.clicked.connect(self.scan)
        self.ui.actionExit.triggered.connect(self.close)

    def update_camera(self):
        img = self.cam.capture()
        height, width, _ = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format.Format_BGR888)

        self.ui.lbCam.setPixmap(QPixmap.fromImage(qImg))
        self.ui.lbCam.setScaledContents(True)

    def scan(self):
        img = self.cam.capture()
        ids = self.ocr.ocr(img, det_kwargs={'min_box_size' : 10})
        message = ''
        for id in ids:
            message = message + ' ' + id['text']
        _ = QMessageBox()
        _.setWindowTitle("扫描结果")
        _.setText(f"扫描到 {message}")
        _.addButton(QMessageBox.StandardButton.Ok)
        _.exec()

    def fetch_homework(self):
        ...

    def fetch_submisson(self):
        ...

    def fetch_students(self):
        ...