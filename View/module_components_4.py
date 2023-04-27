import sys
from datetime import datetime
from datetime import time 
sys.path.append(".")
import serial, threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QPushButton
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal, QRectF
from PyQt5.QtGui import QPixmap, QPen, QBrush, QColor, QIntValidator
from PyQt5.QtCore import QTimer

from Controller.modules_control import TurnOnOffModule

from View.module_pictogram_view import Ui_Form_modulo_pictograma

class ModulePictogram(QWidget):
    def __init__(self, sesion, com_port):
        super().__init__()
        self.ui_pic = Ui_Form_modulo_pictograma()
        self.ui_pic.setupUi(self)
        self.sesion = sesion
        self.port = com_port
        self.set_module_images()
        self.ui_pic.label_text_status.setHidden(True)
        self.ui_pic.label_conn_status.setHidden(True)
        
    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_4_pictogramas.jpg")
        self.ui_pic.label_module_image.setPixmap(
            pixmap1.scaled(
            self.ui_pic.label_module_image.width(),
            self.ui_pic.label_module_image.height(),
            aspectRatioMode=False
            )
        )
    