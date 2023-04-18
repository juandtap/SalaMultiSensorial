import sys
import serial, time, threading

sys.path.append(".")
from datetime import datetime
from datetime import time as time2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from View.module_selection_view import Ui_Form_seleccion_modulos
from View.module_grafomotricidad_view import Ui_Form_modulo_grafomotricidad
from View.module_components_2 import ModuleVumeter
from Controller.session_control import add_sesion_module, get_sesion_by_id
from Model.model import Sesion, ModuloGrafomotricidad
from View.components import MessageDialog

from Controller.module_grafomotricidad_figures import path_figuras



class ModuleSelection(QWidget):
    def __init__(self, student):
        super().__init__()
        self.ui_modules = Ui_Form_seleccion_modulos()
        self.ui_modules.setupUi(self)
        self.student = student
        self.load_info_student()
        
        self.ui_modules.pushButton_module_grafomotricidad.clicked.connect(self.open_module_grafomotricidad)
        self.ui_modules.pushButton_module_vumetro.clicked.connect(self.open_module_vumeter)
    
    def open_module_grafomotricidad(self):
        sesion = Sesion(
            fecha= datetime.now().date(), 
            hora_inicio = datetime.now().time(), 
            hora_fin = None, 
            id_estudiante=self.student.id
        )
        self.grafomotricidad = ModuleGrafomotricidad(sesion, self.ui_modules.lineEdit_com_port.text().strip())
        self.grafomotricidad.show()
    
    def open_module_vumeter(self):
        # sesion = Sesion(
        #     fecha= datetime.now().date(), 
        #     hora_inicio = datetime.now().time(), 
        #     hora_fin = None, 
        #     id_estudiante=self.student.id
        # )
        self.vumeter = ModuleVumeter(None, self.ui_modules.lineEdit_com_port.text().strip())
        self.vumeter.show()

    def load_info_student(self):
        self.ui_modules.label_cedula.setText(self.student.cedula)
        self.ui_modules.label_apellidos.setText(self.student.apellidos)
        self.ui_modules.label_nombres.setText(self.student.nombres)


# En el texrfield lineEdit_time_taken se coloca el tiempo tomado hasta que se 
# se presiono el boton de detener

class ModuleGrafomotricidad(QWidget):
    def __init__(self, sesion, com_port):
        super().__init__()
        self.ui_mod_grafo = Ui_Form_modulo_grafomotricidad()
        self.ui_mod_grafo.setupUi(self)
        self.sesion = sesion
        self.com_port = com_port
        self.ui_mod_grafo.textEdit_instructions.setReadOnly(True)
        
        
        self.set_module_images()
        
        self.ui_mod_grafo.label_conn_status.setHidden(True)
        self.ui_mod_grafo.label_9.setHidden(True)
        self.ui_mod_grafo.label_3.setText("   Tiempo")
        
        self.ui_mod_grafo.timeEdit_limit_time.setReadOnly(True)
        
        self.ui_mod_grafo.pushButton_stop.setEnabled(False)
        self.ui_mod_grafo.pushButton_save.setEnabled(False)
        
        self.ui_mod_grafo.pushButton_start.clicked.connect(self.start_listening_data)
        self.ui_mod_grafo.pushButton_stop.clicked.connect(self.stop_listening_data)
        self.ui_mod_grafo.pushButton_save.clicked.connect(self.save_module_data)
        
       

    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_1_grafomotricidad.jpg")
        self.ui_mod_grafo.label_module_image.setPixmap(
            pixmap1.scaled(
            self.ui_mod_grafo.label_module_image.width(),
            self.ui_mod_grafo.label_module_image.height(),
            aspectRatioMode=False
            )
        )
        
        # carga las figuras en los labels, 
        # el path de las figuras esta en 'path_figuras' del archivo module_grafomotricidad_figures
        for i in range(len(path_figuras)):
            pixmap = QPixmap(path_figuras[i])
            if i+1 < 10:
                label = getattr(self.ui_mod_grafo, "label_figure_0" + str(i+1))
            else:
                label = getattr(self.ui_mod_grafo, "label_figure_" + str(i+1))
            label.setPixmap(pixmap.scaled(100, 100, aspectRatioMode=True))

           
    def start_listening_data(self):
        
        # recibir datos por bluetooth-serial
        # puerto com, parametro junto con la sesion
        self.ui_mod_grafo.timeEdit_limit_time.setStyleSheet("color: black;")
        self.ui_mod_grafo.pushButton_stop.setEnabled(True)
        self.ui_mod_grafo.pushButton_save.setEnabled(False)
        # limpia los campos
        self.clear_fields()

        port = self.com_port
        print("puerto com :"+port)

       
        # Inicio Thread timer 
        
        self.timer_thread = TimerThread()
        self.timer_thread.timeChanged.connect(self.update_time)
        self.timer_thread.finished_signal.connect(self.timer_stopped)
        
        self.timer_thread.start()
        self.ui_mod_grafo.pushButton_stop.setEnabled(True)
        
        ## Inicio Thread lectura de datos serial_bluetooth desde arduino

        time_in_seconds = self.ui_mod_grafo.timeEdit_limit_time.time().second()
        time_in_minutes = self.ui_mod_grafo.timeEdit_limit_time.time().minute()
        self.limit_time_in_seconds = time_in_seconds + \
            (time_in_minutes * 60)
        self.limit_time = self.ui_mod_grafo.timeEdit_limit_time.time()
        print("tiempo total en segundos: ")
        print(self.limit_time_in_seconds)
        print("tiempo total: ")
        print(self.limit_time.toString("mm:ss"))

        self.ui_mod_grafo.lineEdit_limit_time.setText(
            self.limit_time.toString("mm:ss"))

        self.serial_thread = ArduinoSerialThread(
            port=self.com_port, baudrate=9600, timeout=1, duration=self.limit_time_in_seconds)
        self.serial_thread.data_received.connect(self.show_received_data)
        self.serial_thread.start()
        print("mando a iniciar hilo serial")
            
    
        
        
        
    def stop_timer(self):
        self.timer_thread.stop()
        

    def update_time(self, module_time):
        #time_str = module_time.toString('mm:ss')
       
        self.ui_mod_grafo.timeEdit_limit_time.setTime(module_time)
             
    def show_received_data(self, data):
        
        print("Dato recibido : "+data)
        
        
          
    def clear_fields(self):
        self.ui_mod_grafo.lineEdit_figure.setText("")
        self.ui_mod_grafo.lineEdit_result.setText("")
        self.ui_mod_grafo.lineEdit_time_taken.setText("")
        
    
    
    def stop_listening_data(self):
        
        self.timer_thread.stop()
        
        self.time_taken = self.ui_mod_grafo.timeEdit_limit_time.time()
        print("contador detenido por el usuario")
        self.ui_mod_grafo.lineEdit_time_taken.setText(
            self.time_taken.toString("mm:ss")
        )
        self.ui_mod_grafo.pushButton_stop.setEnabled(False)
        self.ui_mod_grafo.pushButton_save.setEnabled(True)
    
    def save_module_data(self):
        pass
        # Despues de que se haga detenido el contador se guarda la informaion 
        #new_module = ModuloGrafomotricidad (
            #tiempo_limite = time2(0,self.limit_time.minute(),self.limit_time.second()),
            #tiempo_tomado = time2(0,self.time_taken.minute(),self.time_taken.second()),
            #aciertos = self.success,
            #fallos = self.fails
        #)
        
        # self.sesion.modulos_grafomotricidad.append(new_module)
        
        # if add_sesion_module(self.sesion, new_module):
        #     self.message_dialog = MessageDialog('Datos Guardados')
        #     self.message_dialog.show()
        #     self.clear_fields()
        # else:
        #     self.message_dialog = MessageDialog('Error!')
        #     self.message_dialog.show()
        
        
    def timer_stopped(self):
        print("se detuvo el contador ")
    
class CountDownThread(QThread):
        
    update_signal = pyqtSignal(QTime)
    finished_signal = pyqtSignal()

    
    def __init__(self, time_edit):
        super().__init__()
        self.time_edit = time_edit
        self.running = True
            
    def run(self):
        time_left = self.time_edit.time()
        while time_left >= QTime(0, 0) and self.running:
            self.update_signal.emit(time_left)
            time_left = time_left.addSecs(-1)
            self.sleep(1)
            
    def stop(self):
        self.running = False
        
class TimerThread(QThread):
    
    timeChanged = pyqtSignal(QTime)
    finished_signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self._is_running = False
        self._elapsed_time = QTime(0, 0, 0)

    def run(self):
        self._is_running = True
        while self._is_running:
            self.sleep(1)
            self._elapsed_time = self._elapsed_time.addSecs(1)
            self.timeChanged.emit(self._elapsed_time)

    def stop(self):
        self._is_running = False


class ArduinoSerialThread(QThread):
    
    data_received = pyqtSignal(str)
    
    
    def __init__(self, port, baudrate, timeout, duration, parent=None):
        super().__init__(parent)
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.duration = duration
        self.stopped = False
        self.stop_event = threading.Event()
        
    def run(self):
        
        print("se ejecuta el hilo serial")
        try:
            bluetooth_serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        except serial.SerialException as e:
            print("Error al intentar conectarse al puerto serial:", e)
            self.finished.emit()
            return
        
        # leer datos durante el tiempo especificado (self.duration)
        
        start_time = time.time()
        while not self.stopped and time.time() - start_time < self.duration:
            if bluetooth_serial.in_waiting:
                data = bluetooth_serial.readline().decode().strip()
                self.data_received.emit(data)
                
            if self.stop_event.is_set():
                self.stopped = True
                self.stop_event.clear()
        
        bluetooth_serial.close()
        self.finished.emit()
        self.quit()
        
    def stop(self):
        self.stopped = True