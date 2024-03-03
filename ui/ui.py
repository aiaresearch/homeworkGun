from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util.connect import get_connection, DatabaseType

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("未提交学生")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        # 创建数据库连接
        self.connection = get_connection(DatabaseType.SQLITE)
        self.cursor = self.connection.cursor()

        # 检索数据并将其填充到表格中
        self.fill_table()

    def fill_table(self):
        # 检索数据
        self.cursor.execute(f"SELECT id FROM submit WHERE time = date();")
        rows = self.cursor.fetchall()
        submits = []
        for row in rows:
            id = row[0]
            self.cursor.execute(f"SELECT * FROM students WHERE id != {id};")
            submits.append(self.cursor.fetchone())

        
        # 排序数据
        submits.sort(key=lambda x: x[1])

        # 填充表格
        header_item = QTableWidgetItem("未提交学生")
        header_item.setTextAlignment(Qt.AlignCenter)
        self.table_widget.setHorizontalHeaderItem(0, header_item)
        self.table_widget.setRowCount(len(submits))
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["学号", "姓名"])

        for i, row in enumerate(submits):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(i, j, item)

    def closeEvent(self, event):
        # 关闭数据库连接
        self.connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
