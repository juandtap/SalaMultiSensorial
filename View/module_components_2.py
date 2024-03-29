# En este archivo esta la clase que controla ventana del modulo vumetro
# Para que el Thread de escucha se detenga tiene que estar recibiendo datos, de lo contrario 
# se queda en un estado de espera bloqueando el socket bluetooth, algo que no es problema ya que 
# el vumetro siempre esta enviando datos, asi que si el vumetro llega a fallar el Thread no se detiene
# guardara los datos pero no liberara el socket bluetooth por el que es necesario cerrar la ventana y volver 
# a abrir, tener en cuenta esto si se quiere establecer algun criterio de parada

import sys
from PyQt5 import QtGui
import bluetooth, json


import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

sys.path.append(".")
from datetime import datetime, time, timedelta

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QGraphicsScene, QGraphicsRectItem, QGraphicsProxyWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal, QRectF, QDateTime
from PyQt5.QtGui import QPixmap, QPen, QBrush, QColor
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from numpy import mean

from View.module_vumeter_view import Ui_Form_modulo_vumetro
from Controller.session_control import add_module_vumetro
from Controller.module_codes import module_mac_address
from Model.model import Sesion, ModuloVumetro
from View.components import MessageDialog
from View.instructions import instrucciones_vumetro
from Controller.modules_control import TurnOnOffModule

class ModuleVumeter(QWidget):
    def __init__(self, sesion):
        super().__init__()
        self.ui_vum = Ui_Form_modulo_vumetro()
        self.ui_vum.setupUi(self)
        self.sesion = sesion
        
        # instrucciones
        self.ui_vum.textEdit_instructions.setText(instrucciones_vumetro)
        
        self.set_module_images()
        self.ui_vum.label_text_status.setText('Conectado, Espere...')
        self.ui_vum.label_conn_status.setHidden(True)
        self.ui_vum.label_reading_data.setHidden(True)

        # desactivo el boton de guardar y detener
        self.ui_vum.pushButton_save.setDisabled(True)
        self.ui_vum.pushButton_stop.setDisabled(True)
        
        
        # envia la senal de inicio 'i' al modulo arduino
        
        self.turn_on_off_thread = TurnOnOffModule('i',2)
        self.turn_on_off_thread.my_signal.connect(self.socket_free)
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
        self.ui_vum.pushButton_save.clicked.connect(self.save_module_data)
        
        # variables para calcular el tiempo de uso del modulo desde que presiona iniciar hasta detener
        self.init_time = None
        self.end_time = None
        self.total_time = None
        
        
    def closeEvent(self, event):
        # envia la senial de finializacion 'f'
        self.turn_on_off_thread = TurnOnOffModule('f',2)
        self.turn_on_off_thread.start()
       
        event.accept()
    
    def socket_free(self, flag):
        if flag == 'free':
            self.ui_vum.label_text_status.setHidden(True)
            self.ui_vum.label_conn_status.setHidden(False)
        else:
            self.ui_vum.label_text_status.setText('!Sin Conexion') 
    
    
    def start_listening_data(self):
        
        plt.clf()
        self.data = [0,]
        self.timedata = [0,]
        self.ui_vum.label_level.setText("")
        self.ui_vum.label_reading_data.setHidden(False)
        self.ui_vum.pushButton_start.setDisabled(True)
        self.ui_vum.pushButton_stop.setDisabled(False)
        self.serial_thread = VumeterDataThread()
        self.serial_thread.data_received.connect(self.updata_data_2)
        
        
        
        self.init_time = datetime.now()
        self.serial_thread.start()
        
        
    
    def updata_data_2(self, level):
        plt.clf()
        self.data.append(level)
        self.timedata.append(len(self.timedata)*50) 
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
        self.ui_vum.pushButton_start.setDisabled(False)
        self.ui_vum.pushButton_stop.setDisabled(True)
        self.ui_vum.pushButton_save.setDisabled(False)
        
        self.serial_thread.stop()
        print('Hilo de escucha detenido')
        print('estado del thread de escucha: '+str(self.serial_thread.isRunning()))
        self.end_time = datetime.now()
        
        self.ui_vum.label_reading_data.setHidden(True)
        self.ui_vum.label_textlevel.setText('Nivel maximo: ')
        self.ui_vum.label_level.setText(str(max(self.data)))
        
        
    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_2_vumetro.png")
        self.ui_vum.label_module_image.setPixmap(
            pixmap1.scaled(
            self.ui_vum.label_module_image.width(),
            self.ui_vum.label_module_image.height(),
            aspectRatioMode=False
            )
        )
        
        pixmap2 = QPixmap("Assets/logo1.png")
        self.ui_vum.label_logo1.setPixmap(
            pixmap2.scaled(
            self.ui_vum.label_logo1.width(),
            self.ui_vum.label_logo1.height(),
            aspectRatioMode=False
            )
        )
        
        pixmap3 = QPixmap("Assets/logo2.png")
        self.ui_vum.label_logo2.setPixmap(
            pixmap3.scaled(
            self.ui_vum.label_logo2.width(),
            self.ui_vum.label_logo2.height(),
            aspectRatioMode=False
            )
        )

    def save_module_data(self):
        print('Guardando datos...')
        self.ui_vum.pushButton_save.setDisabled(True)
        # se guarda la lista[] 'data' en un archivo de texto
        # 
        # directorio para guardar los datos del vumetro
        path = "ModuleData/DatosVumetro/"
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H-%M-%S")
        # este valor es de self.sesion.id
        current_sesion = self.sesion
        filename = path+f"{current_sesion}_{current_date}_{current_time}_datavum.json"
        print('archivo de datos del vumetro guardado en : ')
        print(filename)
        
        ## prueba de datos
        ##self.data.extend([1,2,3,4,4])
        try:
            json_data = json.dumps(self.data)
            with open(filename, "w") as file:
                file.write(json_data)
        except Exception as ex:
            print("error al guardar datos en archivo "+str(ex))

        
        # calcular tiempo de escucha
        
        self.total_time = self.end_time - self.init_time
        
        # guardar en base de datos
        
        new_vum = ModuloVumetro(
            id_sesion = self.sesion,
            nivel_maximo = max(self.data),
            nivel_promedio = int(np.mean(self.data)),
            tiempo = str(self.total_time).split('.')[0],
            datos = filename
        )
        
        if add_module_vumetro(new_vum):
            self.message_dialog = MessageDialog("!Datos Vumetro Guardados")
            self.message_dialog.show()
        else:
            self.message_dialog = MessageDialog("Error!")
            self.message_dialog.show()
            
        
        
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
            blue_socket.connect((module_mac_address[2],1)) 
            
            self.running = True
            
            print("inicia thread de escucha")
            
            while self.running:
                self.msleep(50)
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