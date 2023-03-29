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
        # recibir datos por bluetooth-serial
        # puero com, parametro junto con la sesion
        port = self.com_port
        print("puerto com :"+port)
        
        time_in_seconds = self.ui_mod_grafo.timeEdit_limit_time.time().second()
        time_in_minutes = self.ui_mod_grafo.timeEdit_limit_time.time().minute()
        limit_time = time_in_seconds + (time_in_minutes * 60)
        print("tiempo total en segundos")
        print(limit_time)
        
        # Buscar como manejar esta excepcion cuando no se conecta con arduino
        
        serial_bluetooth = serial.Serial('COM6',9600)
        if serial_bluetooth is not None:
            print("Conexion establecida")
        else:
            print("Sin conexion")
        init_time = time.time()
        
        self.timer.start(1000)
        while (time.time() - init_time) < limit_time:
            data_in = serial_bluetooth.readline().decode().rstrip()
            if data_in:
                print("Dato recibido: " + data_in)
            
        print("Detenida la lectura de datos del arduino")
                    
    def stop_listening_data(self):
        pass
    
    
        
    def update_timer(self):
        remain_time = self.ui_mod_grafo.timeEdit_limit_time.time()
        if remain_time.second() != 0 and remain_time.minute() != 0:
            self.timer.stop()
        else:
            remain_time = remain_time.addSecs(-1)
            self.ui_mod_grafo.timeEdit_limit_time.setTime(remain_time)