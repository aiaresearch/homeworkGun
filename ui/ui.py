from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QLabel, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QInputDialog, QMessageBox, QLineEdit
from PySide6.QtCore import Qt
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util.connect import get_connection, DatabaseType

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("登录页面")
        self.resize(250, 100)
        self.center()

        layout = QVBoxLayout(self)

        self.classname = ''
        self.label = QLabel("请输入班级：", self)
        layout.addWidget(self.label)

        self.class_edit = QLineEdit(self)
        layout.addWidget(self.class_edit)

        self.login_button = QPushButton("登录", self)
        self.login_button.clicked.connect(self.login_clicked)
        layout.addWidget(self.login_button)

    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def login_clicked(self):
        while not self.classname:
            self.classname = self.class_edit.text()
            if not self.classname:
                QMessageBox.warning(self, "Warning", "班级不能为空！")


class MainWindow(QMainWindow):
    def __init__(self, classname = '高一23'):
        super().__init__()

        self.classname = classname

        self.setWindowTitle("学生作业提交情况页面")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.label = QLabel(f" {self.classname} 班学生作业提交情况")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["学号", "姓名", "提交情况"])
        layout.addWidget(self.table_widget)

        # 创建数据库连接
        self.connection = get_connection(DatabaseType.SQLITE)
        self.cursor = self.connection.cursor()

        # 检索数据并将其填充到表格中

        self.fill_table()

        self.button = QPushButton("手动添加提交记录")
        self.button.clicked.connect(self.open_text_input_dialog)
        layout.addWidget(self.button)





    def check_input_legal(self, input_str) -> bool:
        if input_str.isdigit():
            self.cursor.execute(f"SELECT * FROM students WHERE id = {input_str}")
        else:
            self.cursor.execute(f"SELECT * FROM students WHERE name = '{input_str}'")
        
        return self.cursor.fetchone() is not None
            

    def open_text_input_dialog(self):
        text, ok = QInputDialog.getText(self, '添加提交记录', '学生姓名或学号:')
        if ok:
            if not self.check_input_legal(text):
                QMessageBox.warning(self, "Warning", f"学生不存在！")
            else:
                if text.isdigit():
                # 学号
                    self.cursor.execute(f"INSERT INTO submit VALUES ({text}, date());")            
                else:
                    self.cursor.execute(f"""INSERT INTO submit (id, time)
                                        SELECT id, date('now')
                                        FROM students
                                       WHERE name = '{text}';""")
                    
                self.fill_table()


    def fill_table(self):
        # 检索数据
        self.cursor.execute("""SELECT students.*
                            FROM students
                            LEFT JOIN submit ON students.id = submit.id
                            WHERE submit.id IS NULL;
                            """)
        unsubmits = self.cursor.fetchall()

        self.cursor.execute("""SELECT students.*
                            FROM students
                            LEFT JOIN submit ON students.id = submit.id
                            WHERE submit.id IS NOT NULL;
                            """)
        submits = self.cursor.fetchall()

        # 排序数据
        unsubmits.sort(key=lambda x: x[1])
        submits.sort(key=lambda x: x[1])

        # 填充表格
        self.table_widget.setRowCount(len(unsubmits)+len(submits))

        for i, row in enumerate(unsubmits):
            id_item = QTableWidgetItem(str(row[0]))
            name_item = QTableWidgetItem(row[1])
            self.table_widget.setItem(i, 0, id_item)
            self.table_widget.setItem(i, 1, name_item)
            self.table_widget.setItem(i, 2, QTableWidgetItem("未提交"))
        
        for i, row in enumerate(submits):
            id_item = QTableWidgetItem(str(row[0]))
            name_item = QTableWidgetItem(row[1])
            self.table_widget.setItem(i+len(unsubmits), 0, id_item)
            self.table_widget.setItem(i+len(unsubmits), 1, name_item)
            self.table_widget.setItem(i+len(unsubmits), 2, QTableWidgetItem("已提交"))


    def closeEvent(self, event):
        # 关闭数据库连接
        self.cursor.close()
        self.connection.commit()
        self.connection.close()
        event.accept()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())