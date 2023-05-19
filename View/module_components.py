# En este modulo esta la clase que controla ventana de seleccion de modulo
# y la ventana del modulo de grafomotricidad
# tambien estas las clases QThread para el envio y recepcion de datos arduino

import sys
import serial, threading, bluetooth

sys.path.append(".")
from datetime import datetime
from datetime import time 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QRadioButton
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from View.module_selection_view import Ui_Form_seleccion_modulos
from View.module_grafomotricidad_view import Ui_Form_modulo_grafomotricidad
from View.module_components_2 import ModuleVumeter
from View.module_components_3 import ModuleIlumination
from View.module_components_4 import ModulePictogram
from Controller.session_control import add_sesion_module, get_sesion_by_id, add_module_grafomotricidad, set_final_time
from Model.model import Sesion, ModuloGrafomotricidad
from View.components import MessageDialog

from Controller.module_codes import path_figuras, codigo_figuras, module_mac_address
from Controller.modules_control import TurnOnOffModule



class ModuleSelection(QWidget):
    def __init__(self, student):
        super().__init__()
        self.ui_modules = Ui_Form_seleccion_modulos()
        self.ui_modules.setupUi(self)
        self.student = student
        self.load_info_student()
        
        # eliminar label, line edit del puerto COM
        self.ui_modules.label_bluetooth_status.setHidden(True)
        self.ui_modules.lineEdit_com_port.setHidden(True)
        self.ui_modules.label_3.setHidden(True)
        self.ui_modules.label_5.setHidden(True)
        # ya no se usa el puerto COM
        
        
        # comentar para que no se cree sesione innecesarias
        self.create_sesion()
        
        self.ui_modules.pushButton_module_grafomotricidad.clicked.connect(self.open_module_grafomotricidad)
        self.ui_modules.pushButton_module_vumetro.clicked.connect(self.open_module_vumeter)
        self.ui_modules.pushButton_module_iluminacion.clicked.connect(self.open_module_ilumination)
        self.ui_modules.pushButton_module_pictograma.clicked.connect(self.open_module_pictogram)
        
    def create_sesion(self):
        
        new_sesion = Sesion(
            fecha= datetime.now().date(), 
            hora_inicio = datetime.now().time(), 
            hora_fin = None, 
            id_estudiante=self.student.id
        )
        ## add_session_module retorna el id de la sesion
        # self.sesion es un (int)
        # se pasa como parametro para las ventanas de los modulos
        self.sesion = add_sesion_module(new_sesion)
        
        print('sesion #'+str(self.sesion)+' creada')
        
        
        
    def open_module_grafomotricidad(self):
        # cambiar None por self.sesion 2
        self.grafomotricidad = ModuleGrafomotricidad(self.sesion)
        self.grafomotricidad.show()
    
    def open_module_vumeter(self):
        
        self.vumeter = ModuleVumeter(self.sesion)
        self.vumeter.show()
        
    def open_module_ilumination(self):
        self.ilumination = ModuleIlumination(self.sesion)
        self.ilumination.show()
        
    def open_module_pictogram(self):
        self.pictogram = ModulePictogram(None)
        self.pictogram.show()

    def load_info_student(self):
        self.ui_modules.label_cedula.setText(self.student.cedula)
        self.ui_modules.label_apellidos.setText(self.student.apellidos)
        self.ui_modules.label_nombres.setText(self.student.nombres)

    def closeEvent(self, event):
        
        print("finalizo la sesion")
        set_final_time(self.sesion, datetime.now().time())
        print("se agrego la hora fin a la sesion "+str(self.sesion))
        event.accept()

# En el texrfield lineEdit_time_taken se coloca el tiempo tomado hasta que se 
# se presiono el boton de detener

class ModuleGrafomotricidad(QWidget):
    def __init__(self, sesion):
        super().__init__()
        self.ui_mod_grafo = Ui_Form_modulo_grafomotricidad()
        self.ui_mod_grafo.setupUi(self)
        self.sesion = sesion # id de la sesion (int)
        
        self.ui_mod_grafo.textEdit_instructions.setReadOnly(True)
        self.ui_mod_grafo.label_conn_status.setHidden(True)
        self.ui_mod_grafo.label_9.setText('Conectando, Espere...')
        self.ui_mod_grafo.label_3.setText("   Tiempo")
        
        # envia la senal de inicio 'i' al modulo arduino
        
        self.turn_on_off_thread = TurnOnOffModule('i',1)
        self.turn_on_off_thread.my_signal.connect(self.socket_free)
        self.turn_on_off_thread.start()
        
        self.set_module_images()
        
        
        
        
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
    
        # establece la figura 1 como seleccionada, para evitar que pulsen el boton de inicio
        # sin antes haber seleccionado una figura
        
        self.ui_mod_grafo.radioButton_1.setChecked(True)
        self.ui_mod_grafo.lineEdit_figure.setText(codigo_figuras[1])
        self.figure_code = 1
        print("codigo de la figura seleccionada: ")
        print(self.figure_code)
        
    def closeEvent(self, event):
        # envia la senial de finializacion 'f'
        self.turn_on_off_thread = TurnOnOffModule('f',1)
        self.turn_on_off_thread.start()
       
        event.accept()
        
    def socket_free(self, flag):
        if flag == 'free':
            self.ui_mod_grafo.label_9.setHidden(True)
            self.ui_mod_grafo.label_conn_status.setHidden(False)
        else:
            self.ui_mod_grafo.label_9.setText('!Sin Conexion')

    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_1_grafomotricidad.jpg")
        self.ui_mod_grafo.label_module_image.setPixmap(
            pixmap1.scaled(
            self.ui_mod_grafo.label_module_image.width(),
            self.ui_mod_grafo.label_module_image.height(),
            aspectRatioMode=False
            )
        )
        
        pixmap2 = QPixmap("Assets/logo1.png")
        self.ui_mod_grafo.label_logo1.setPixmap(
            pixmap2.scaled(
            self.ui_mod_grafo.label_logo1.width(),
            self.ui_mod_grafo.label_logo1.height(),
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
        
        # obtengo el nombre del radiobutton 'radioButton_2' por ejemplo
        # y extraigo el numero con split('-')[-1] con ese numero busco el nombre de la figura en el diccionario de figuras
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


       
        # Inicio Thread timer 
        
        self.timer_thread = TimerThread()
        self.timer_thread.timeChanged.connect(self.update_time)
        self.timer_thread.finished_signal.connect(self.timer_stopped)
        
        self.timer_thread.start()
        self.ui_mod_grafo.pushButton_stop.setEnabled(True)
        
        ## Inicio Thread lectura de datos serial_bluetooth desde arduino

        
       
        self.serial_thread = ArduinoSerialThread()
        self.serial_thread.data_received.connect(self.show_received_data)
        self.serial_thread.start()
        print("mando a iniciar hilo serial")
            
  
    def update_time(self, module_time):
        #time_str = module_time.toString('mm:ss')
        # si el thread del contador se detuvo, se pone en 00:00
        if self.timer_thread._is_running:
            self.ui_mod_grafo.timeEdit_limit_time.setTime(module_time)
        else:
            self.ui_mod_grafo.timeEdit_limit_time.setTime(QTime(0,0,0))
             
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
        # acciones a ejecutar cuando el thread del contador de detiene
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
    
    
    def __init__(self,parent=None):
        super().__init__(parent)
        
        
        self.stopped = False
        self.stop_event = threading.Event()
        
    def run(self):
        
        print("se ejecuta el hilo de escucha socket bluetooth")
        try:
            #bluetooth_serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            blue_socket = bluetooth.BluetoothSocket()
            blue_socket.connect((module_mac_address[1],1))
        except Exception as e:
            print("Error al intentar la conexion con HC05:", e)
            self.finished.emit()
            return
        
       
        while not self.stopped:
            data = blue_socket.recv(1024)
            
            data_formated = data.decode('utf-8').strip()
            self.data_received.emit(data_formated)
            # se detiene al recivir un dato
            if data is not None:
                self.stopped = True


            if self.stop_event.is_set():
                self.stopped = True
                self.stop_event.clear()
        
        blue_socket.close()
        self.finished.emit()
        print("Hilo Escucha socket bluetooth terminado")
        self.quit()
        
    def stop(self):
        self.stopped = True
        print("Hilo Escucha socket bluetooth terminado por el usuario")
        
# revisar Qtimer, hacer que se reinicie al presionar el boton de inicio
# revisar figure code linea 227 en la funcion show_data_received
# nivel de instensida 1  2 3 , bajo, medio , alto
# cada 50ms los datos del vumetro 
# se guarda nivel maximo alcanzado, considerar nivel intermedio y bajo, sabiendo que el nivel 1 va a ser siempre el bajo y el tiempo 