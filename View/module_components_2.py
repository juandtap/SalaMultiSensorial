import sys
import serial, time, threading, random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

sys.path.append(".")
from datetime import datetime
from datetime import time as time2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QGraphicsScene, QGraphicsRectItem, QGraphicsProxyWidget
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal, QRectF
from PyQt5.QtGui import QPixmap, QPen, QBrush, QColor
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
import random

from View.module_vumeter_view import Ui_Form_modulo_vumetro
from Controller.session_control import add_sesion_module, get_sesion_by_id
from Model.model import Sesion, ModuloGrafomotricidad
from View.components import MessageDialog

class ModuleVumeter(QWidget):
    def __init__(self, sesion, com_port):
        super().__init__()
        self.ui_vum = Ui_Form_modulo_vumetro()
        self.ui_vum.setupUi(self)
        self.sesion = sesion
        self.port = com_port
        self.set_module_images()
        self.ui_vum.label_text_status.setHidden(True)
        self.ui_vum.label_conn_status.setHidden(True)
        
        #self.draw_vumeter_level()
        #self.set_level()
        
        


    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_2_vumetro.png")
        self.ui_vum.label_module_image.setPixmap(
            pixmap1.scaled(
            self.ui_vum.label_module_image.width(),
            self.ui_vum.label_module_image.height(),
            aspectRatioMode=False
            )
        )
        
    
    ## prueba dibujar vumetro
    def draw_vumeter_level(self):
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 400, 400)
        
        # dibuja todos los rectangulos del vumetro
        
        
        rect_size = 20  # Tamaño de los rectángulos
        rect_count = 18  # Cantidad de rectángulos a dibujar
        rect_margin = 2  # Margen entre cada rectángulo
        
        x = (self.scene.width() / 2) - (rect_size / 2)
        y = self.scene.height() - rect_size
        
       
        for i in range(rect_count):
            rect = QRectF(x, y, rect_size, rect_size)
            pen = QPen(Qt.black, 2)
            if i >= 0 and i < 6:
                # Verde del 1 al 6
                brush = QBrush(QColor(0, 255, 0))
            elif i >= 6 and i < 12:
                # Amarillo del 7 al 12
                brush = QBrush(QColor(255, 255, 0))
            else:
                # Rojo del 13 al 18
                brush = QBrush(QColor(255, 0, 0))
                
            self.scene.addRect(rect, pen, brush)
            
            # Ajustamos la posición del siguiente rectángulo
            y -= rect_size + rect_margin
        
        for item in self.scene.items():
            if isinstance(item,QGraphicsRectItem):
                item.setVisible(False)
                


        self.ui_vum.graphicsView.setScene(self.scene)

        
    def set_level(self):
        level = 15
        self.ui_vum.label_level.setText(str(level))
        last_index = len(self.scene.items()) - 1
        
        for i in range(last_index, last_index - level, -1):
            self.scene.items()[i].setVisible(True)
           