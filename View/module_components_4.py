import sys
from datetime import datetime
from datetime import time 
sys.path.append(".")
import bluetooth, threading
from datetime import datetime
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from Controller.module_codes import module_mac_address
from View.instructions import instrucciones_pictogramas
from View.components import MessageDialog
from Controller.session_control import add_module_pictograma
from Model.model import ModuloPictogramas
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
        
        # instrucciones
        self.ui_pic.textEdit_instructions.setText(instrucciones_pictogramas)
        
        
        self.ui_pic.label_text_status.setHidden(True)
        self.ui_pic.label_conn_status.setHidden(True)
        self.ui_pic.label_reading_status.setHidden(True)
        
        self.ui_pic.pushButton_start.clicked.connect(self.start_listening_data)
        self.ui_pic.pushButton_stop.clicked.connect(self.stop_listening_data)
        self.ui_pic.pushButton_save.clicked.connect(self.save_data)
        
        self.ui_pic.pushButton_start.setEnabled(True)
        self.ui_pic.pushButton_save.setEnabled(False)
        self.ui_pic.pushButton_stop.setEnabled(False)
        
         # variables para tomar el tiempo desde que presiona el boton iniciar hasta que recibe los datos
        self.start_time = None
        self.end_time = None
        self.total_time = None
        
    def socket_free(self, flag):
        if flag == "free":
            self.ui_pic.label_conn_status.setHidden(False)
            self.ui_pic.label_text_status.setHidden(True)
        else:
            self.ui_pic.label_text_status.setText("!Sin Conexion")
            
        
    
    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_4_pictogramas.png")
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
        self.clear_data()
        print("Escuchando datos modulo pictogramas")
        self.thread_pictogram = PictogramDataThread()
        self.thread_pictogram.data_received.connect(self.show_received_data)
        self.thread_pictogram.start()
        self.ui_pic.label_reading_status.setHidden(False)
        self.ui_pic.label_reading_status.setText("Esperando Datos ...")
        self.ui_pic.pushButton_start.setEnabled(False)
        self.ui_pic.pushButton_save.setEnabled(False)
        self.ui_pic.pushButton_stop.setEnabled(True)
        
        self.start_time = datetime.now()
        
    def show_received_data(self, data):
        print("Datos recibidos: ")
        self.ui_pic.label_reading_status.setText("Datos recibidos")
        print(data)
        if data:
            data_values = data.split(";")
        else:
            data_values = []
        print("datos separados:")
        for value in data_values:
            print(value)
        
        try:
            self.ui_pic.lineEdit_categoria_seleccionada.setText(data_values[0])
        except IndexError:
            self.ui_pic.lineEdit_categoria_seleccionada.setText("Valor no disponible")

        try:
            self.ui_pic.lineEdit_num_pictogramas_disponibles.setText(data_values[1])
        except IndexError:
            self.ui_pic.lineEdit_num_pictogramas_disponibles.setText("Valor no disponible")
            
        try:
            self.ui_pic.lineEdit_pictogramas.setText(data_values[2])
        except IndexError:
            self.ui_pic.lineEdit_pictogramas.setText("Valor no disponible")   

        try:
            self.ui_pic.lineEdit_num_pictogramas_seleccionados.setText(data_values[3])
        except IndexError:
            self.ui_pic.lineEdit_num_pictogramas_seleccionados.setText("Valor no disponible")

        try:
            self.ui_pic.lineEdit_tamanio_tablero.setText(data_values[4]+"x"+data_values[4])
        except IndexError:
            self.ui_pic.lineEdit_tamanio_tablero.setText("Valor no disponible")

        try:
            self.ui_pic.lineEdit_categorias_mostradas.setText(data_values[5])
        except IndexError:
            self.ui_pic.lineEdit_categorias_mostradas.setText("Valor no disponible")

        try:
            self.ui_pic.lineEdit_num_correctos.setText(data_values[6])
        except IndexError:
            self.ui_pic.lineEdit_num_correctos.setText("Valor no disponible")
            
        try:
            self.ui_pic.lineEdit_list_correctos.setText(data_values[7])
        except IndexError:
            self.ui_pic.lineEdit_list_correctos.setText("Valor no disponible")    

        try:
            self.ui_pic.lineEdit_num_incorrectos.setText(data_values[8])
        except IndexError:
            self.ui_pic.lineEdit_num_incorrectos.setText("Valor no disponible")
            
        try:
            self.ui_pic.lineEdit_list_incorrectos.setText(data_values[9])
        except IndexError:
            self.ui_pic.lineEdit_list_incorrectos.setText("Valor no disponible")
            
        try:
            self.ui_pic.lineEdit_tiempo.setText(data_values[10])
        except IndexError:
            self.ui_pic.lineEdit_tiempo.setText("Valor no disponible")
        
        self.ui_pic.pushButton_start.setEnabled(True)
        self.ui_pic.pushButton_save.setEnabled(True)
        self.ui_pic.pushButton_stop.setEnabled(False)
        
        self.end_time = datetime.now()
        
    def save_data(self):
        # guarda en la base de datos
        print("guardando en DB")
        
        # ya no se calcula el tiempo
        # el tiempo es enviado en segundos desde el modulo de pictigrama
        # self.total_time = self.end_time - self.start_time
        # total_time_str = str(self.total_time).split('.')[0]
        # print("Tiempo : "+total_time_str)
        
        new_picto = ModuloPictogramas(
            id_sesion = self.sesion,
            categoria_seleccionada = self.ui_pic.lineEdit_categoria_seleccionada.text(),
            numero_pictogramas_disponibles = self.ui_pic.lineEdit_num_pictogramas_disponibles.text(),
            nombres_pictogramas = self.ui_pic.lineEdit_pictogramas.text(),
            numero_pictogramas_seleccionados = self.ui_pic.lineEdit_num_pictogramas_seleccionados.text(),
            tamanio_tablero = self.ui_pic.lineEdit_tamanio_tablero.text(),
            categorias_mostradas = self.ui_pic.lineEdit_categorias_mostradas.text(),
            numero_selecciones_correctas = self.ui_pic.lineEdit_num_correctos.text(),
            selecciones_correctas = self.ui_pic.lineEdit_list_correctos.text(),
            numero_selecciones_incorrectas = self.ui_pic.lineEdit_num_incorrectos.text(),
            selecciones_incorrectas = self.ui_pic.lineEdit_list_incorrectos.text(),
            tiempo = self.ui_pic.lineEdit_tiempo.text()
            
        )

        if add_module_pictograma(new_picto):
            print("Datos guardados")
            self.message_dialog = MessageDialog("!Datos Guardados")
            self.message_dialog.show()
            self.ui_pic.pushButton_start.setEnabled(True)
            self.ui_pic.pushButton_save.setEnabled(False)
            self.ui_pic.pushButton_stop.setEnabled(False)
        else:
            print("Error al guardar")
            self.message_dialog = MessageDialog("!Error al guardar")
            self.message_dialog.show()
            
        
       
        
        
    
    def stop_listening_data(self):
        self.ui_pic.label_reading_status.setText("")
        self.ui_pic.pushButton_start.setEnabled(True)
        self.ui_pic.pushButton_save.setEnabled(False)
        self.ui_pic.pushButton_stop.setEnabled(False)
        self.thread_pictogram.stop()
        self.end_time = datetime.now()
     
    def closeEvent(self, event):
        self.stop_listening_data()
        event.accept()

    def clear_data(self):
        self.ui_pic.lineEdit_categoria_seleccionada.setText("")
        self.ui_pic.lineEdit_num_pictogramas_disponibles.setText("")
        self.ui_pic.lineEdit_pictogramas.setText("")
        self.ui_pic.lineEdit_num_pictogramas_seleccionados.setText("")
        self.ui_pic.lineEdit_tamanio_tablero.setText("")
        self.ui_pic.lineEdit_categorias_mostradas.setText("")
        self.ui_pic.lineEdit_num_correctos.setText("")
        self.ui_pic.lineEdit_list_correctos.setText("")
        self.ui_pic.lineEdit_num_incorrectos.setText("")
        self.ui_pic.lineEdit_list_incorrectos.setText("")
        self.ui_pic.lineEdit_tiempo.setText("")
    
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
            print("conectado")
        except Exception as e:
            print("Error al intentar la conexion con Raspberry:", e)
            self.finished.emit()
            return
        
        print("Leyendo datos...")
        accumulated_data = ""
        while not self.stopped:
            try:
                data = blue_socket.recv(4096)
                
                
                if data:
                    # self.stopped = True
                    data_formated = data.decode('utf-8')
                    print("datos decodificados: ")
                    print(data_formated)
                    accumulated_data += data_formated
                    
                    # Verificar si se ha recibido el mensaje completo
                    # cuando se encuentra un salto de linea '/n'
                    
                    delimiter = '\n'
                    if delimiter in accumulated_data:
                        "se detecto el salto de linea"
                        self.data_received.emit(accumulated_data)
                        self.stopped = True

                if self.stop_event.is_set():
                    self.stopped = True
                    self.stop_event.clear()
                    
            except bluetooth.btcommon.BluetoothError as e:
                print("Error occurred:", str(e))
                blue_socket.close()
                self.finished.emit()
                break
            
        blue_socket.close()
        self.finished.emit()
        print("Hilo Escucha socket bluetooth terminado")
        print("Socket bluetooth liberado")
        self.quit()
        
    def stop(self):
        self.stopped = True
        print("Hilo Escucha socket bluetooth terminado por el usuario")
        
