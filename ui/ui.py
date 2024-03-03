from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QLabel, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QInputDialog, QMessageBox
from PySide6.QtCore import Qt
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util.connect import get_connection, DatabaseType

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("未提交学生")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.label = QLabel("表格示例")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.table_widget = QTableWidget()
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
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["学号", "姓名", "提交情况"])

        for i, row in enumerate(unsubmits):
            id_item = QTableWidgetItem(str(row[0]))
            name_item = QTableWidgetItem(row[1])
            self.table_widget.setItem(i, 0, id_item)
            self.table_widget.setItem(i, 1, name_item)
            self.table_widget.setItem(i, 2, QTableWidgetItem("未提交"))
        
        for i, row in enumerate(submits):
            print(row)
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
    window = MainWindow()
    window.show()
    sys.exit(app.exec())