# Este modulo controla la ventana del modulo Iluminacion

import sys

sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QGraphicsScene, QGraphicsRectItem, QGraphicsProxyWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal, QRectF
from PyQt5.QtGui import QPixmap, QPen, QBrush, QColor
from PyQt5.QtCore import QTimer

from View.module_iluminacion_view import Ui_Form_modulo_iluminacion

class ModuleIlumination(QWidget):
    def __init__(self, sesion, com_port):
        super().__init__()
        self.ui_ilu = Ui_Form_modulo_iluminacion()
        self.ui_ilu.setupUi(self)
        self.sesion = sesion
        self.port = com_port
        self.set_module_images()
        self.ui_ilu.label_text_status.setHidden(True)
        self.ui_ilu.label_conn_status.setHidden(True)
        
    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_3_iluminacion.jpg")
        self.ui_ilu.label_module_image.setPixmap(
            pixmap1.scaled(
            self.ui_ilu.label_module_image.width(),
            self.ui_ilu.label_module_image.height(),
            aspectRatioMode=False
            )
        )