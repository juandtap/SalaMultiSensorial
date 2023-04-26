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
        
        #self.draw_vumeter_level()
        #self.set_level()
        layout = QVBoxLayout()
        self.plot_vum = PlotWidget()
        layout.addWidget(self.plot_vum)
        self.ui_vum.plot_widget.setLayout(layout)
        
        self.ui_vum.pushButton_start.clicked.connect(self.agregar_datos)
        
         # Establecer los parámetros de la gráfica
        self.data = []  # Lista para almacenar los datos
        self.time = []  # Lista para almacenar los tiempos
        
         # Crear un QTimer que actualice la gráfica cada 100 ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_grafica)
        self.timer.start(100)

        # Crear una variable para el tiempo
        self.tiempo = 0
        
    def agregar_datos(self):
        dato = random.randint(0,100)
        self.tiempo =+ 1
        self.plot_vum.update_plot(dato, self.tiempo)
        
    def actualizar_grafica(self):
        self.plot_vum.canvas.draw()

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

class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)

        # Crear una figura de Matplotlib y un objeto de plot
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)

        # Crear un objeto de canvas de Matplotlib
        self.canvas = FigureCanvas(self.figure)

        # Agregar el canvas a este widget
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Crear una lista para almacenar los datos que se graficarán
        self.data = []
        self.time = []

    def update_plot(self, new_data, new_time):
        # Agregar los nuevos datos y el nuevo tiempo a las listas de datos y tiempo
        #self.data.append(new_data)
        #self.time.append(new_time)
        self.data = [0,3, 6, 7, 10, 20, 30, 59, 70, 40, 50]
        self.time = [0,1,2,3,4,5,6,7,8,9,10]

        # Limitar la cantidad de puntos mostrados en la gráfica a 100
        if len(self.data) > 100:
            self.data.pop(0)
            self.time.pop(0)

        # Limpiar el plot y graficar los datos
        self.axes.clear()
        self.axes.plot(self.time, self.data)

        # Actualizar el canvas
        self.canvas.draw()