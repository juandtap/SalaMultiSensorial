# En este modulo esta la clase que controla ventana del modulo vumetro


import sys
import serial, time, threading, random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

sys.path.append(".")
from datetime import datetime
from datetime import time as time2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QGraphicsScene, QGraphicsRectItem, QGraphicsProxyWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal, QRectF
from PyQt5.QtGui import QPixmap, QPen, QBrush, QColor
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

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
        
       
        self.canvas = FigureCanvas(plt.gcf())
        
        
        layout = QVBoxLayout()
       
        
        layout.addWidget(self.canvas)
        self.ui_vum.plot_widget.setLayout(layout)
        
       
        
        # Establecer los parámetros de la gráfica
        self.data = [0,3,6,7,9,2,0,9,7,4,5]  # Lista para almacenar los datos
        self.time = [0,1,2,3,4,5,6,7,8,9,10]  # Lista para almacenar los tiempos
        
        plt.plot(self.time, self.data)
        
        plt.xlabel('Tiempo ms')
        plt.ylabel('Nivel')
        plt.grid(True)
        
        plt.subplots_adjust(top=1)
        plt.subplots_adjust(bottom=0.12)
        self.canvas.draw()
        
        
    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_2_vumetro.png")
        self.ui_vum.label_module_image.setPixmap(
            pixmap1.scaled(
            self.ui_vum.label_module_image.width(),
            self.ui_vum.label_module_image.height(),
            aspectRatioMode=False
            )
        )
