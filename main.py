import sys
import os
sys.path.append(os.path.dirname(__file__))
import util.cap as cap
from util.fetch import fetch_data
from util.insert import insert_submit
from ui.login_ui import LoginWindow
import numpy as np
import cv2
import requests
from cnocr import CnOcr

from PySide6.QtWidgets import QApplication
import qt_material

           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    qt_material.apply_stylesheet(app, theme='light_blue.xml')
    login_window = LoginWindow(cap.Camera(), CnOcr(rec_model_name='number-densenet_lite_136-fc', det_model_name='en_PP-OCRv3_det', cand_alphabet='0123456789'))
    login_window.show()
    if login_window.detect_cfg_existence():
        login_window.token_check()
    
    sys.exit(app.exec())