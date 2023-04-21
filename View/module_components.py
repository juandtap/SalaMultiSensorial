import sys
import serial, threading

sys.path.append(".")
from datetime import datetime
from datetime import time 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QRadioButton
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from View.module_selection_view import Ui_Form_seleccion_modulos
from View.module_grafomotricidad_view import Ui_Form_modulo_grafomotricidad
from View.module_components_2 import ModuleVumeter
from Controller.session_control import add_sesion_module, get_sesion_by_id, add_module_grafomotricidad, set_final_time
from Model.model import Sesion, ModuloGrafomotricidad
from View.components import MessageDialog

from Controller.module_grafomotricidad_figures import path_figuras, codigo_figuras



class ModuleSelection(QWidget):
    def __init__(self, student):
        super().__init__()
        self.ui_modules = Ui_Form_seleccion_modulos()
        self.ui_modules.setupUi(self)
        self.student = student
        self.load_info_student()
        
        #1self.create_sesion()
        
        self.ui_modules.pushButton_module_grafomotricidad.clicked.connect(self.open_module_grafomotricidad)
        self.ui_modules.pushButton_module_vumetro.clicked.connect(self.open_module_vumeter)
        
    def create_sesion(self):
        
        new_sesion = Sesion(
            fecha= datetime.now().date(), 
            hora_inicio = datetime.now().time(), 
            hora_fin = None, 
            id_estudiante=self.student.id
        )
        
        self.sesion = add_sesion_module(new_sesion)
        
        print('sesion #'+str(self.sesion)+' creada')
        
        
        
    def open_module_grafomotricidad(self):
        # cambiar None por self.sesion 2
        self.grafomotricidad = ModuleGrafomotricidad(None, self.ui_modules.lineEdit_com_port.text().strip())
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

    def closeEvent(self, event):
        #3set_final_time(self.sesion, datetime.now().time())
        #print("se agrego la hora fin a la sesion "+str(self.sesion))
        event.accept()

# En el texrfield lineEdit_time_taken se coloca el tiempo tomado hasta que se 
# se presiono el boton de detener

class ModuleGrafomotricidad(QWidget):
    def __init__(self, sesion, com_port):
        super().__init__()
        self.ui_mod_grafo = Ui_Form_modulo_grafomotricidad()
        self.ui_mod_grafo.setupUi(self)
        self.sesion = sesion # id de la sesion (int)
        self.com_port = com_port
        self.ui_mod_grafo.textEdit_instructions.setReadOnly(True)
        
        # envia la senal de inicio 'i' al modulo arduino
        self.turn_on_module()
        
        
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
        
        
        # asignar evento a cada uno de los radiobuttons (18)
        radio_buttons_list = [self.findChild(QRadioButton, f"radioButton_{i}") for i in range(1, 19)]
        
        for radio_button in radio_buttons_list:
            radio_button.clicked.connect(self.get_selected_figure_name)

    
    def turn_on_module(self):
        # este metodo se inicia al abrir la ventana del modulo
        # enviar caracter 'i' al modulo rduino
        
        try:
            serial_port = serial.Serial(self.com_port, 9600)
            serial_port.write(b'i')
            serial_port.close()
            print("caracter de inicio 'i' enviado por el puerto: "+self.com_port)
        except serial.SerialException as ex:
            print("Error en la conexion serial: ", ex)
        except Exception as ex:
            print("Error al enviar el caracter 'i'", ex)
        
        
        
        
    def turn_off_module(self):
        #este metodo se ejecuta al cerrar la ventana
        #enviar caracter 'f' al modulo arduino
        try:
            serial_port = serial.Serial(self.com_port, 9600)
            serial_port.write(b'f')
            serial_port.close()
            print("caracter de finalizacion 'f' enviado por el puerto: "+self.com_port)
        except serial.SerialException as ex:
            print("Error en la conexion serial: ", ex)
        except Exception as ex:
            print("Error al enviar el caracter 'i'", ex)
            
        
       
    
    def closeEvent(self, event):
        # envia la senial de finializacion 'f'
        self.turn_off_module()
        event.accept()
        

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

    
    def get_selected_figure_name(self):
        radio_button = self.sender()
        rb = '0'
        if radio_button.isChecked():
            rb = radio_button.objectName()
        
        # obtengo el nombre del radiobutton (radioButton_2) por ejemplp
        # y extraigo el numero con split('-')[-] con ese numero busco el nombre de la figura en el diccionario de figuras
        # Otra forma de hacerlo seria directamente obtener el texto del radioButton pero igual se 
        # se necesitaria su codigo para saber si se selecciono la figura correcta
        
        self.figure_code = int(rb.split('_')[-1])
        print("codigo de la figura seleccionada: ")
        print(self.figure_code)
        
        self.ui_mod_grafo.lineEdit_figure.setText(codigo_figuras[self.figure_code])
           
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

        
       
        self.serial_thread = ArduinoSerialThread(
            port=self.com_port, baudrate=9600, timeout=1)
        self.serial_thread.data_received.connect(self.show_received_data)
        self.serial_thread.start()
        print("mando a iniciar hilo serial")
            
  
    def update_time(self, module_time):
        #time_str = module_time.toString('mm:ss')
       
        self.ui_mod_grafo.timeEdit_limit_time.setTime(module_time)
             
    def show_received_data(self, data):
        
        print("Dato recibido : "+data)
        if data == str(self.figure_code):
            self.ui_mod_grafo.lineEdit_result.setText('Correcto')
        else:
            self.ui_mod_grafo.lineEdit_result.setText('Incorrecto')
        
        
        self.stop_listening_data()
          
    def clear_fields(self):
        #self.ui_mod_grafo.lineEdit_figure.setText("")
        self.ui_mod_grafo.lineEdit_result.setText("")
        self.ui_mod_grafo.lineEdit_time_taken.setText("")
        
    
    
    def stop_listening_data(self):
        
        self.timer_thread.stop()
        self.serial_thread.stop()
        self.time_taken = self.ui_mod_grafo.timeEdit_limit_time.time()
        print("contador detenido por el usuario")
        self.ui_mod_grafo.lineEdit_time_taken.setText(
            self.time_taken.toString("mm:ss")
        )
        
        self.ui_mod_grafo.timeEdit_limit_time.setTime(QTime(0,0,0))
        
        self.ui_mod_grafo.pushButton_stop.setEnabled(False)
        self.ui_mod_grafo.pushButton_save.setEnabled(True)
    
    def save_module_data(self):
        # Se guarda la informacion al presionar el boton de 'Guardar'
        new_module = ModuloGrafomotricidad (
            id_sesion = self.sesion,
            figura = codigo_figuras[self.figure_code],
            tiempo_tomado = time(0,self.time_taken.minute(),self.time_taken.second()),
            resultado = self.ui_mod_grafo.lineEdit_result.text()
        )
        
        
        
        if add_module_grafomotricidad(new_module):
            self.message_dialog = MessageDialog('Datos Guardados')
            self.message_dialog.show()
            self.clear_fields()
        else:
            self.message_dialog = MessageDialog('Error!')
            self.message_dialog.show()
        
        
    def timer_stopped(self):
        print("se detuvo el contador ")
    
        
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
    
    
    def __init__(self, port, baudrate, timeout, parent=None):
        super().__init__(parent)
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        
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
        
       
        while not self.stopped:
            if bluetooth_serial.in_waiting:
                data = bluetooth_serial.readline().decode().strip()
                self.data_received.emit(data)
                # se detiene al recivir un dato
                if data is not None:
                    self.stopped = True


            if self.stop_event.is_set():
                self.stopped = True
                self.stop_event.clear()
        
        bluetooth_serial.close()
        self.finished.emit()
        print("Hilo Escucha serial terminado")
        self.quit()
        
    def stop(self):
        self.stopped = True
        print("Hilo Escucha serial terminado por el usuario")
        