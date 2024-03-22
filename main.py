import sys
import os
from PySide6.QtWidgets import QApplication
from cnocr import CnOcr
sys.path.append(os.path.dirname(__file__))
DEBUG = False
if DEBUG is False:
    import util.cap as cap
from ui.login_ui import LoginWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow(cap.Camera() if DEBUG is False else None, CnOcr(
        rec_model_name='number-densenet_lite_136-fc',
        det_model_name='en_PP-OCRv3_det',
        cand_alphabet='0123456789'))
    login_window.show()
    if login_window.detect_cfg_existence():
        login_window.token_check()

    sys.exit(app.exec())
    