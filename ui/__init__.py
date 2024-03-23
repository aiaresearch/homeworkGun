from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QWidget, QFrame
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


subjects = {1 : '语文', 2 : '数学', 3 : '英语', 4 : '物理', 5 : '化学', 6 : '生物'}


def center(w : QWidget | QMainWindow):
    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.geometry()
    window_geometry = w.frameGeometry()
    x = screen_geometry.center().x() - window_geometry.width() / 2
    y = screen_geometry.center().y()- window_geometry.height() / 2
    w.move(x, y)


class FrameView(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Plain)
