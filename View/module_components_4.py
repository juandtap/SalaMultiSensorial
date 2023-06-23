import sys
from datetime import datetime
from datetime import time 
sys.path.append(".")
import bluetooth, threading
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from Controller.module_codes import module_mac_address
# Este modulo controla la ventana del modulo pictogramas

from PyQt5.QtGui import QPixmap


from Controller.modules_control import TurnOnOffModule

from View.module_pictogram_view import Ui_Form_modulo_pictograma

class ModulePictogram(QWidget):
    def __init__(self, sesion):
        super().__init__()
        self.ui_pic = Ui_Form_modulo_pictograma()
        self.ui_pic.setupUi(self)
        self.sesion = sesion
        self.ui_pic.label_text_status.setText("Conectando...")
        # self.turn_on_off_thread = TurnOnOffModule('i',4)
        # self.turn_on_off_thread.my_signal.connect(self.socket_free)
        # self.turn_on_off_thread.start()
        self.set_module_images()
        self.ui_pic.label_text_status.setHidden(True)
        self.ui_pic.label_conn_status.setHidden(True)
        
        self.ui_pic.pushButton_start.clicked.connect(self.start_listening_data)
        self.ui_pic.pushButton_stop.clicked.connect(self.stop_listening_data)
        
    def socket_free(self, flag):
        if flag == "free":
            self.ui_pic.label_conn_status.setHidden(False)
            self.ui_pic.label_text_status.setHidden(True)
        else:
            self.ui_pic.label_text_status.setText("!Sin Conexion")
            
        
    
    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_4_pictogramas.jpg")
        self.ui_pic.label_module_image.setPixmap(
            pixmap1.scaled(
            self.ui_pic.label_module_image.width(),
            self.ui_pic.label_module_image.height(),
            aspectRatioMode=False
            )
        )
        
        pixmap2 = QPixmap("Assets/logo1.png")
        self.ui_pic.label_logo1.setPixmap(
            pixmap2.scaled(
            self.ui_pic.label_logo1.width(),
            self.ui_pic.label_logo1.height(),
            aspectRatioMode=False
            )
        )
        
        pixmap3 = QPixmap("Assets/logo2.png")
        self.ui_pic.label_logo2.setPixmap(
            pixmap3.scaled(
            self.ui_pic.label_logo2.width(),
            self.ui_pic.label_logo2.height(),
            aspectRatioMode=False
            )
        )
        
    def start_listening_data(self):
        print("Escuchando datos modulo pictogramas")
        self.thread_pictogram = PictogramDataThread()
        self.thread_pictogram.data_received.connect(self.show_received_data)
        self.thread_pictogram.start()
        
        
    def show_received_data(self, data):
        print("Datos recibidos: ")
        print(data)
        self.ui_pic.lineEdit_list_images.setText(data)
    
    def stop_listening_data(self):
        self.thread_pictogram.stop()
               
class PictogramDataThread(QThread):
    
    data_received = pyqtSignal(str)
    
    
    def __init__(self,parent=None):
        super().__init__(parent)
        
        
        self.stopped = False
        self.stop_event = threading.Event()
        
    def run(self):
        
        print("se ejecuta el hilo de escucha socket bluetooth")
        try:
           
            blue_socket = bluetooth.BluetoothSocket()
            blue_socket.connect((module_mac_address[4],1))
        except Exception as e:
            print("Error al intentar la conexion con Raspberry:", e)
            self.finished.emit()
            return
        
        print("Leyendo datos...")
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
        print("Socket bluetooth liberado")
        self.quit()
        
    def stop(self):
        self.stopped = True
        print("Hilo Escucha socket bluetooth terminado por el usuario")
        
## datos a recibir
# MAC del raspberry: B8:27:EB:94:95:C8

# {Numero de pictogramas, correctos, incorrectos, categoriaseleccionada}
# 