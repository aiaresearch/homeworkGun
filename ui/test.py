from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtSql import QSqlDatabase, QSqlQuery
import os
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建数据库连接
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + 'homework.db')  # 指定数据库文件路径

        if not self.db.open():
            print("无法连接到数据库")
            sys.exit(1)

        # 设置界面布局
        self.tableWidget = QTableWidgetItem()
        self.setCentralWidget(self.tableWidget)

        # 执行查询
        self.query = QSqlQuery()
        self.query.exec("SELECT * FROM students;")

        # 加载数据到界面
        self.load_data()

    def load_data(self):
        row = 0
        self.tableWidget.setColumnCount(self.query.record().count())
        self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])  # 更换为你的实际列名

        while self.query.next():
            column = 0
            for field in range(self.query.record().count()):
                item = QTableWidgetItem(str(self.query.value(field)))
                self.tableWidget.setItem(row, column, item)
                column += 1
            row += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
