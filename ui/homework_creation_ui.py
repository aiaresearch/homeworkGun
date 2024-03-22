import sys
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from qfluentwidgets import PushButton, ComboBox, SubtitleLabel, CalendarPicker, Dialog
from qfluentwidgets import FluentIcon as FIF
from . import center


class CreationView(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("CreationView{background: rgb(255, 255, 255)}")


class HomeworkCreationWindow(CreationView):
    submitSignal = Signal(int, str, str)
    def __init__(self):
        super().__init__()

        center(self)
        self.setWindowTitle("作业创建")
        
        self.vBox = QVBoxLayout(self)
        self.vBox.setContentsMargins(30, 30, 30, 30)
        self.vBox.setSpacing(20)

        self.subjectBox = QHBoxLayout()
        self.subjectBox.addWidget(SubtitleLabel("作业科目:"))
        self.subjectComboBox = ComboBox(self)
        self.subjectComboBox.setPlaceholderText("请选择作业科目")
        subjects = ["语文", "数学", "英语", "物理", "化学", "生物"]
        self.subjectComboBox.addItems(subjects)
        self.subjectComboBox.setCurrentIndex(-1)
        self.subjectBox.addWidget(self.subjectComboBox)
        self.vBox.addLayout(self.subjectBox)
        
        self.startBox = QHBoxLayout()
        self.startBox.addWidget(SubtitleLabel("开始时间："))
        self.startCalendar = CalendarPicker(self)
        self.startCalendar.setDateFormat('yyyy-M-d')
        self.startBox.addWidget(self.startCalendar)
        self.vBox.addLayout(self.startBox)

        self.endBox = QHBoxLayout()
        self.endBox.addWidget(SubtitleLabel("结束时间："))
        self.endCalendar = CalendarPicker(self)
        self.endCalendar.setDateFormat('yyyy-M-d')
        self.endBox.addWidget(self.endCalendar)
        self.vBox.addLayout(self.endBox)

        self.submitButton = PushButton("提交", self, FIF.CHECKBOX)
        self.submitButton.clicked.connect(self.submit)
        self.vBox.addWidget(self.submitButton)

    def submit(self):
        subject = self.subjectComboBox.currentIndex()
        start_time = self.startCalendar.date.toString('yyyy-MM-dd')
        end_time = self.endCalendar.date.toString('yyyy-MM-dd')
        if subject == -1 or not start_time or not end_time:
            w = Dialog("失败", "请填写完整信息")
            w.exec()
        else:
            self.submitSignal.emit(subject+1, start_time, end_time)
            w = Dialog("成功", "作业创建成功")
            w.exec()
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomeworkCreationWindow()
    w.show()
    sys.exit(app.exec())
    