# En este modulo esta la clase que controla ventana del modulo vumetro


import sys
import serial, time, threading, random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

sys.path.append(".")
from datetime import datetime
from datetime import time as time2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QGraphicsScene, QGraphicsRectItem, QGraphicsProxyWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal, QRectF, QDateTime
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
        #self.data = [0,3,6,7,9,2,0,9,7,4,5]  
        #self.time = [0,1,2,3,4,5,6,7,8,9,10]
        
        self.data = [0,]  
        self.time = [0,]  
        
        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.update_data)
        #self.timer.start(500)
        
        plt.plot(self.time, self.data)
        
        plt.xlabel('Tiempo ms')
        plt.ylabel('Nivel')
        plt.grid(True)
        
        
        plt.subplots_adjust(top=1)
        plt.subplots_adjust(bottom=0.12)
        self.canvas.draw()
        
        self.ui_vum.pushButton_start.clicked.connect(self.start_listening_data)
        self.ui_vum.pushButton_stop.clicked.connect(self.stop_listening_data)
        
    
    def start_listening_data(self):
        self.serial_thread = VumeterDataThread(self.port, 9600)
        self.serial_thread.data_received.connect(self.updata_data_2)
        self.serial_thread.start()
        
    
    def updata_data_2(self, data, time):
        plt.clf()
        self.data.extend(data)
        self.time.extend(time)
        plt.plot(self.time, self.data)
        
        print("listas nivel actual: ")
        for level in self.data:
            print(str(level))
        print('lista de timpo: ')
        for tm in self.time:
            print(str(tm))
        
        plt.xlabel('Tiempo ms')
        plt.ylabel('Nivel')
        plt.grid(True)
        
        plt.autoscale(True)
        
        plt.subplots_adjust(top=1)
        plt.subplots_adjust(bottom=0.12)
        self.canvas.draw()

    def stop_listening_data(self):
        self.serial_thread.stop()
        print('Hilo de escucha detenido')
        print('estado del thread de escucha: '+str(self.serial_thread.isRunning()))
    
    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_2_vumetro.png")
        self.ui_vum.label_module_image.setPixmap(
            pixmap1.scaled(
            self.ui_vum.label_module_image.width(),
            self.ui_vum.label_module_image.height(),
            aspectRatioMode=False
            )
        )

    def update_data(self):
        value = random.randint(0,9)
        self.data.append(value)
        # cada 100ms
        self.time.append(len(self.time)*100) 
        
        # actualiza la grafica
        
        #limpia la grafica (clear)
        plt.clf()
        
        plt.plot(self.time, self.data)
        
        plt.xlabel('Tiempo ms')
        plt.ylabel('Nivel')
        plt.grid(True)
        
        plt.subplots_adjust(top=1)
        plt.subplots_adjust(bottom=0.12)
        self.canvas.draw()
        

# Thread para escuchar datos del vumetro
class VumeterDataThread(QThread):
    
    data_received = pyqtSignal(list, list)

    def __init__(self, port, baudrate, parent=None):
        super().__init__(parent)
        self.port = port
        self.baudrate = baudrate
        self.running = False

    def run(self):
        try: 
            ser = serial.Serial(self.port, self.baudrate)
            self.running = True
        except serial.SerialException as e:
            print("Error al conectarse al modulo por el puerto com "+self.port+" : "+str(e))
            return
        data = []
        timedata = []
        while self.running:
            if ser.in_waiting:
                line = ser.readline().decode('utf-8').strip()
                try:
                    val = float(line)
                    print("dato recibido: "+line)
                    data.append(val)
                    timedata.append(time.monotonic()/ 1000)
                    self.data_received.emit(data, timedata)
                except ValueError:
                    print("Error en datos recibidos: ",line)
                self.msleep(10)
        ser.close()
        print('Conexion con el modulo cerrada')

        
    def stop(self):
        self.running = False
        self.wait(100) 