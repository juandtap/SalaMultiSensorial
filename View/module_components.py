import sys
import serial, time
sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox
from PyQt5.QtCore import Qt, QDate, QTimer, QTime
from PyQt5.QtGui import QPixmap
from View.module_selection_view import Ui_Form_seleccion_modulos
from View.module_grafomotricidad_beta_view import Ui_Form_modulo_grafomotricidad

class ModuleSelection(QWidget):
    def __init__(self, student):
        super().__init__()
        self.ui_modules = Ui_Form_seleccion_modulos()
        self.ui_modules.setupUi(self)
        self.student = student
        self.load_info_student()
        
        self.ui_modules.pushButton_module_grafomotricidad.clicked.connect(self.open_module_grafomotricidad)
        
    
    def open_module_grafomotricidad(self):
        self.grafomotricidad = ModuleGrafomotricidad(None, self.ui_modules.lineEdit_com_port.text().strip())
        self.grafomotricidad.show()
        
        
    def load_info_student(self):
        self.ui_modules.label_cedula.setText(self.student.cedula)
        self.ui_modules.label_apellidos.setText(self.student.apellidos)
        self.ui_modules.label_nombres.setText(self.student.nombres)


# En el texrfield lineEdit_remainingtime se coloca el tiempo tomado hasta que se 
# se presiono el boton de detener

class ModuleGrafomotricidad(QWidget):
    def __init__(self, sesion, com_port):
        super().__init__()
        self.ui_mod_grafo = Ui_Form_modulo_grafomotricidad()
        self.ui_mod_grafo.setupUi(self)
        self.sesion = sesion
        self.com_port = com_port
        self.ui_mod_grafo.textEdit_instructions.setReadOnly(True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.set_module_images()
        
        self.ui_mod_grafo.pushButton_stop.setEnabled(False)
        
        self.ui_mod_grafo.pushButton_start.clicked.connect(self.start_listening_data)
        self.ui_mod_grafo.pushButton_stop.clicked.connect(self.stop_listening_data)

    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_1_grafomotricidad.jpg")
        self.ui_mod_grafo.label_module_image.setPixmap(
            pixmap1.scaled(
            self.ui_mod_grafo.label_module_image.width(),
            self.ui_mod_grafo.label_module_image.height(),
            aspectRatioMode=False
            )
        )
        
    def start_listening_data(self):
        
        if ((self.ui_mod_grafo.timeEdit_limit_time.time().minute() != 0) or (self.ui_mod_grafo.timeEdit_limit_time.time().second())) != 0 :
        # recibir datos por bluetooth-serial
        # puerto com, parametro junto con la sesion
            self.ui_mod_grafo.timeEdit_limit_time.setStyleSheet("color: black;")
            self.ui_mod_grafo.pushButton_stop.setEnabled(True)
            # limpia los campos
            self.clear_fields()
            
            port = self.com_port
            print("puerto com :"+port)
            
            time_in_seconds = self.ui_mod_grafo.timeEdit_limit_time.time().second()
            time_in_minutes = self.ui_mod_grafo.timeEdit_limit_time.time().minute()
            self.limit_time_in_seconds = time_in_seconds + (time_in_minutes * 60)
            self.limit_time = self.ui_mod_grafo.timeEdit_limit_time.time()
            print("tiempo total en segundos: ")
            print(self.limit_time_in_seconds)
            print("tiempo total: ")
            print(self.limit_time.toString("mm:ss"))
            
            serial_bluetooth = None
            try:
                serial_bluetooth = serial.Serial('COM6',9600)
                print("Conexion establecida")
            except serial.SerialException as ex:
                print("Sin conexion : "+str(ex))
            
            
            
            init_time = time.time()
            
            self.timer.start(1000)
            
            if serial_bluetooth is not None:
            
                while (time.time() - init_time) < self.limit_time_in_seconds:
                    data_in = serial_bluetooth.readline().decode().rstrip()
                    if data_in:
                        print("Dato recibido: " + data_in)
                
            print("Detenida la lectura de datos del arduino")
        else:
            print("Tiempo ingresado es cero")
            self.ui_mod_grafo.timeEdit_limit_time.setStyleSheet("color: red;")
        
                   
    def clear_fields(self):
        self.ui_mod_grafo.lineEdit_fails.setText("")
        self.ui_mod_grafo.lineEdit_success.setText("")
        self.ui_mod_grafo.lineEdit_remaining_time.setText("")
        
    
    
    def stop_listening_data(self):
        self.timer.stop()
        time_taken = self.limit_time.addSecs(-self.ui_mod_grafo.timeEdit_limit_time.time().second())
        self.ui_mod_grafo.lineEdit_remaining_time.setText(
            time_taken.toString("mm:ss")
        )
        print("contador detenido por el usuario")
        self.ui_mod_grafo.pushButton_stop.setEnabled(False)
    
        
    def update_timer(self):
        remain_time = self.ui_mod_grafo.timeEdit_limit_time.time()
        remain_time = remain_time.addSecs(-1)
        self.ui_mod_grafo.timeEdit_limit_time.setTime(remain_time)
        if remain_time.second() == 0 and remain_time.minute() == 0:
            self.timer.stop()
            print("se detuvo el contador")
            self.ui_mod_grafo.lineEdit_remaining_time.setText(self.limit_time.toString('mm:ss'))
            self.ui_mod_grafo.pushButton_stop.setEnabled(False)