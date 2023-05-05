# En este modulo esta la clase que controla ventana del modulo vumetro
# para que el Thread de escucha se detenga tiene que estar reciviendo datos, de lo contrario 
# se queda en un estado de espera bloqueando el socket bluetooth

import sys
from PyQt5 import QtGui
import serial, time, threading, random, bluetooth


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
from Controller.module_codes import module_mac_address
from Model.model import Sesion, ModuloGrafomotricidad
from View.components import MessageDialog
from Controller.modules_control import TurnOnOffModule

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
        
        # envia la senal de inicio 'i' al modulo arduino
        
        self.turn_on_off_thread = TurnOnOffModule('i')
        self.turn_on_off_thread.start()
        
        
        self.canvas = FigureCanvas(plt.gcf())
        
        
        layout = QVBoxLayout()
       
        
        layout.addWidget(self.canvas)
        self.ui_vum.plot_widget.setLayout(layout)
        
       
        
        # Establecer los parámetros de la gráfica
        #self.data = [0,3,6,7,9,2,0,9,7,4,5]  
        #self.time = [0,1,2,3,4,5,6,7,8,9,10]
        
        self.data = [0,]  
        self.timedata = [0,]  
        
        self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_data)
        self.timer.start(500)
        
        plt.plot(self.timedata , self.data)
        
        plt.xlabel('Tiempo ms')
        plt.ylabel('Nivel')
        plt.grid(True)
        
        
        plt.subplots_adjust(top=1)
        plt.subplots_adjust(bottom=0.12)
        self.canvas.draw()
        
        self.ui_vum.pushButton_start.clicked.connect(self.start_listening_data)
        self.ui_vum.pushButton_stop.clicked.connect(self.stop_listening_data)
        
    def closeEvent(self, event):
        # envia la senial de finializacion 'f'
        self.turn_on_off_thread = TurnOnOffModule('f')
        self.turn_on_off_thread.start()
       
        event.accept()
        
    
    
    def start_listening_data(self):
        self.serial_thread = VumeterDataThread()
        self.serial_thread.data_received.connect(self.updata_data_2)
        # self.serial_thread.finished.connect(self.serial_thread.quit)
        # self.serial_thread.finished.connect(self.serial_thread.deleteLater)
        self.serial_thread.start()
        
    
    def updata_data_2(self, level):
        plt.clf()
        self.data.append(level)
        self.timedata.append(len(self.timedata)*100) 
        plt.plot(self.timedata , self.data)
        
        #print("listas nivel actual: ")
        # for level in self.data:
        #     print(str(level))
        # print('lista de timpo: ')
        # for tm in self.timedata :
        #     print(str(tm))
        
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
        self.timedata.append(len(self.timedata)*100) 
        
        
        # actualiza la grafica
        
        #limpia la grafica (clear)
        plt.clf()
        
        plt.plot(self.timedata, self.data)
        
        plt.xlabel('Tiempo ms')
        plt.ylabel('Nivel')
        plt.grid(True)
        
        plt.subplots_adjust(top=1)
        plt.subplots_adjust(bottom=0.12)
        self.canvas.draw()
        

# Thread para escuchar datos del vumetro
class VumeterDataThread(QThread):
    
    data_received = pyqtSignal(int)

    def __init__(self,parent=None):
        super().__init__(parent)
        # self.port = port
        # self.baudrate = baudrate
        self.running = False

    def run(self):
        
        try:
            blue_socket = bluetooth.BluetoothSocket()
            blue_socket.connect((module_mac_address[0],1)) 
            
            self.running = True
            
            print("inicia thread de escucha")
            
            while self.running:
                self.msleep(100)
                print("leyendo datos...")
                data = blue_socket.recv(1024)
                
                line = data.decode('utf-8').strip()
                try:
                    val = int(line)
                    print("dato recibido: "+line)
                        
                        
                    self.data_received.emit(val)
                except ValueError:
                    print("Error en datos recibidos: ",line)
                
                if not self.running:
                    break
            
            
        except Exception as e:
            print("Error al conectarse al modulo  ",e)
        
        finally:
            blue_socket.close()
            print('Conexion con el modulo cerrada')
 
    def stop(self):
        self.running = False
        print("pongo en false el flag")
        self.wait(100) 