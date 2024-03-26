from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt, QTimer, Signal, QThread, QObject)
from PySide6.QtGui import (QImage, QPixmap)
from PySide6.QtWidgets import (QLabel, QMainWindow, QMenu, QMenuBar,
                               QStatusBar, QWidget, QMessageBox, QListWidgetItem, QTableWidgetItem)
from qfluentwidgets import (ListWidget, TableWidget, PushButton, MessageBox, FluentWindow, Action)
import os
import cv2
from threading import Thread
import serial
from .homework_creation_ui import HomeworkCreationWindow
from util.database import init_client_db, insertion, query
from util.request import request
from util.cap import first_frame
import util.serial_connect
from . import subjects, center


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.homeworkList = ListWidget(MainWindow)
        self.homeworkList.setObjectName(u"homeworkList")
        self.homeworkList.setGeometry(QRect(50, 50, 201, 531))
        self.lbCam = QLabel(MainWindow)
        self.lbCam.setObjectName(u"lbCam")
        self.lbCam.setGeometry(QRect(370, 50, 320, 240))
        self.lbCam.setPixmap(QPixmap(u"resources/zh1z.png"))
        self.lbCam.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbText = QLabel(MainWindow)
        self.lbText.setObjectName(u"lbText")
        self.lbText.setGeometry(QRect(370, 20, 320, 16))
        self.lbText.setTextFormat(Qt.TextFormat.PlainText)
        self.lbText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.capButton = PushButton(MainWindow)
        self.capButton.setObjectName(u"capButton")
        self.capButton.setGeometry(QRect(250, 100, 101, 31))
        self.createButton = PushButton(MainWindow)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(250, 140, 101, 31))
        self.submissionTable = TableWidget(MainWindow)
        self.submissionTable.setObjectName(u"submissionTable")
        self.submissionTable.setGeometry(QRect(370, 309, 400, 240))
        self.submissionTable.setColumnCount(3)
        self.submissionTable.setStyleSheet("submisionTable{background: rgb(255, 255, 255)} ")
        self.submissionTable.setHorizontalHeaderLabels([u"学生姓名", u"学生学号", u"提交情况"])
        self.submissionTable.verticalHeader().hide()
        self.submissionTable.setBorderVisible(True)
        self.submissionTable.setBorderRadius(8)
        self.submissionTable.setWordWrap(False)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        self.lbCam.setText("")
        self.lbText.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u753b\u9762", None))
        self.capButton.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
    # retranslateUi


class HomeworkListItem(QListWidgetItem):
    def __init__(self, text, homework_id):
        super().__init__(text)
        self.homework_id = homework_id


class SerialThread(QObject):
    data_received = Signal(bool)

    def __init__(self, port):
        super().__init__()
        self.is_running = True
        self.port = port

    def run(self):
        while self.is_running:
            print(self.port)
            if self.port:
                try:
                    ser = serial.Serial(self.port, 9600, timeout=1, bytesize=8, parity='N', stopbits=1)
                    while self.is_running:
                        if ser.in_waiting > 0:
                            print("按下按钮")
                            data = ser.readline().decode().strip()
                            if isinstance(data, str):
                                self.data_received.emit(True)   
                finally:
                    ser.close()

    def stop(self):
        self.is_running = False


class MainWindow(FluentWindow):
    def __init__(self, ocr):
        super().__init__()
        self.ocr = ocr
        self.students = []
        self.homeworks = []
        self.last_homework_id = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_window()
        self.setStyleSheet("MainWindow{background: rgb(255, 255, 255)}")
        center(self)
        self.setWindowTitle("作业提交系统")

        self.fill_homework_list()

        self.ui.homeworkList.itemClicked.connect(self.show_submission)
        self.ui.capButton.clicked.connect(self.scan)
        self.ui.createButton.clicked.connect(self.create_homework)


    def init_window(self):
        
        if not os.path.exists(os.path.join(os.path.dirname(__file__), os.pardir, 'homework.db')):
            init_client_db.database_init()
            self.fetch_students()
        
        init_client_db.database_init()
        self.fetch_homework()
        self.load_students()
        selected_port = util.serial_connect.select_serial_port()
        self.serial_thread = QThread()
        self.serial_worker = SerialThread(selected_port)
        self.serial_worker.moveToThread(self.serial_thread)
        self.serial_worker.data_received.connect(self.button_presssed)
        self.serial_thread.started.connect(self.serial_worker.run)
        self.serial_thread.start()

    
    def button_presssed(self, data):
        if data:
            self.scan()
        

    def update_camera(self):
            img = first_frame()
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            height, width, _ = img.shape
            bytesPerLine = 3 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format.Format_BGR888)

            self.ui.lbCam.setPixmap(QPixmap.fromImage(qImg))
            self.ui.lbCam.setScaledContents(True)


    def scan(self):
        img = first_frame()
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        height, width, _ = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format.Format_BGR888)
        self.ui.lbCam.setPixmap(QPixmap.fromImage(qImg))
        self.ui.lbCam.setScaledContents(True)

        scanned_ids = self.ocr.ocr(img, det_kwargs={'min_box_size': 10})
        message = ''
        for scanned_id in scanned_ids:
            message = message + ' ' + scanned_id['text']
        self.ui.lbText.setText(f"识别结果：{message}")
        for student_id in scanned_ids:
            for student in self.students:
                if str(student[0]) == student_id['text']:
                    self.ui.lbText.setText(f"识别结果：{message} 提交成功")
                    self.submit_homework(self.ui.homeworkList.currentItem().homework_id, student_id['text'])
                    self.show_submission()
                    break
                    
                self.ui.lbText.setText(f"识别结果：{message} 未找到该学生")

        
        QTimer.singleShot(2000, lambda: self.ui.lbCam.setPixmap(QPixmap()))


    def create_homework(self):
        self.create = HomeworkCreationWindow()
        self.create.submitSignal.connect(self.handle_creation)
        self.create.show()


    def handle_creation(self, subject, start_time, end_time):
        self.last_homework_id += 1
        homework_id = self.last_homework_id
        insertion.insert_homework(homework_id, subject, start_time, end_time)
        self.homeworks.append((homework_id, subject, start_time, end_time))
        self.fill_homework_list()
        request.create_homework(homework_id, str(subject), start_time, end_time)


    def fetch_homework(self):
        self.homeworks, self.last_homework_id = request.fetch_homeworks()
        for homework in self.homeworks:
            insertion.insert_homework(homework[0], homework[1], homework[2], homework[3])
        self.fill_homework_list()


    def fetch_students(self):
        self.students = request.fetch_student(class_id=12)
        insertion.insert_students(self.students)


    def load_students(self):
        self.students = query.get_students()


    
    def fill_homework_list(self):
        self.ui.homeworkList.clear()
        for homework in self.homeworks:
            item = HomeworkListItem(f"{subjects[homework[1]]} 作业 {homework[3][5:]} 截止", homework[0])
            self.ui.homeworkList.addItem(item)
            
    
    def show_submission(self):
        self.ui.submissionTable.clear()
        item = self.ui.homeworkList.currentItem()
        homework_id = item.homework_id
        self.ui.submissionTable.setRowCount(len(self.students))
        submissions = query.get_submission(homework_id)
        
        for i, submission in enumerate(submissions):
            submission[2] = '已提交' if submission[2]=="True" else '未提交'
            for j, content in enumerate(submission):
                self.ui.submissionTable.setItem(i, j, QTableWidgetItem(content))
        self.ui.submissionTable.resizeColumnsToContents()


    def submit_homework(self, homework_id, school_id):
        subject = insertion.insert_submission(homework_id, school_id)
        request.submit_homework(school_id, subject, homework_id)
