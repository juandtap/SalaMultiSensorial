# Este modulo controla la ventana del modulo Iluminacion

import sys

sys.path.append(".")
import serial, threading, bluetooth
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QPushButton, QButtonGroup
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal, QRectF
from PyQt5.QtGui import QPixmap, QPen, QBrush, QColor, QIntValidator
from PyQt5.QtCore import QTimer
from Controller.module_codes import ilumination_colors, rgb_colors, module_mac_address
from Controller.modules_control import TurnOnOffModule
from Controller.session_control import add_module_iluminacion
from PyQt5 import QtCore
from View.module_iluminacion_view import Ui_Form_modulo_iluminacion
from View.components import MessageDialog
from datetime import datetime
from Model.model import ModuloIluminacion

class ModuleIlumination(QWidget):
    def __init__(self, sesion):
        super().__init__()
        self.ui_ilu = Ui_Form_modulo_iluminacion()
        self.ui_ilu.setupUi(self)
        self.sesion = sesion
        
       
        self.set_module_images()
        self.ui_ilu.label_text_status.setText("Conectado...")
        self.ui_ilu.label_conn_status.setHidden(True)
        
        # envio de senal de inicio 'i'
        self.turn_on_off_thread = TurnOnOffModule('i',0)
        self.turn_on_off_thread.my_signal.connect(self.socket_free)
        self.turn_on_off_thread.start()
        
        self.ui_ilu.pushButton_start.clicked.connect(self.send_color_data)
        
        # se agregar los radiobutton a un buttonGroup
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.ui_ilu.radioButton_yes)
        self.button_group.addButton(self.ui_ilu.radioButton_no)
        
        
        # se bloquea los radio button de si y no, se activan al pulsar el boton 'enviar'
        self.ui_ilu.radioButton_yes.setEnabled(False)
        self.ui_ilu.radioButton_no.setEnabled(False)
        self.ui_ilu.pushButton_save.setEnabled(False)
        
        #variable que guarda si reconocio o no el valor
        self.recognize = ''
        # eventos radio buttons SI,NO
        self.ui_ilu.radioButton_yes.clicked.connect(lambda: self.does_recognize_color(self.ui_ilu.radioButton_yes))
        self.ui_ilu.radioButton_no.clicked.connect(lambda: self.does_recognize_color(self.ui_ilu.radioButton_no))
        
        
        
        
        self.ui_ilu.pushButton_save.clicked.connect(self.save_module_data)
        
        # radiobutton color definido seleccionado por default
        self.ui_ilu.radioButton_defined_color.setChecked(True)
        
        self.ui_ilu.lineEdit_R_code.setDisabled(True)
        self.ui_ilu.lineEdit_G_code.setDisabled(True)
        self.ui_ilu.lineEdit_B_code.setDisabled(True)
        
        self.ui_ilu.radioButton_defined_color.clicked.connect(self.disable_RGB_text)
        self.ui_ilu.radioButton_custom_color.clicked.connect(self.disable_RGB_text)
        
        # asigno evento clicked.connect a los botones de los colores
        
        color_button_list = [self.findChild(QPushButton, f"pushButton_{i}") for i in range(1, 10)]
        for color_button in color_button_list:
            color_button.clicked.connect(self.get_selected_color)
        
        # defino el valor por defecto del slider que controla la intencidad
        # 0=bajo, 1=normal, 2=alto
        self.light_level = 1
        self.ui_ilu.slider_level.valueChanged.connect(self.get_selected_level)
        
        # defino el color rojo por defecto para evitar valores nullos al momento de enviar datos
        
        self.ui_ilu.lineEdit_selected_color.setText(ilumination_colors[1])
        
        # valido que los datos para el codigo RGB solo ingresen numeros entre  0-255
        self.ui_ilu.lineEdit_R_code.setValidator(QIntValidator(0,255))
        self.ui_ilu.lineEdit_R_code.textChanged.connect(self.check_code)
        
        self.ui_ilu.lineEdit_G_code.setValidator(QIntValidator(0,255))
        self.ui_ilu.lineEdit_G_code.textChanged.connect(self.check_code)
        
        self.ui_ilu.lineEdit_B_code.setValidator(QIntValidator(0,255))
        self.ui_ilu.lineEdit_B_code.textChanged.connect(self.check_code)
        
        
        # variables para tomar el tiempo desde que presiona el boton encender hasta el boton de guardar
        self.init_time = None
        self.end_time = None
        self.total_time = None
        
    def closeEvent(self, event):
        # envia la senial de finializacion 'f'
        self.turn_on_off_thread = TurnOnOffModule('f',0)
        self.turn_on_off_thread.start()
       
        event.accept()
    
    def socket_free(self, flag):
        if flag == 'free':
            self.ui_ilu.label_text_status.setHidden(True)
            self.ui_ilu.label_conn_status.setHidden(False)
        else:
            self.ui_ilu.label_text_status.setText('!Sin Conexion')
    
    
    def set_module_images(self):
        pixmap1 = QPixmap("Assets/modulo_3_iluminacion.jpg")
        self.ui_ilu.label_module_image.setPixmap(
            pixmap1.scaled(
            self.ui_ilu.label_module_image.width(),
            self.ui_ilu.label_module_image.height(),
            aspectRatioMode=False
            )
        )
    
    # funcion para seleccionar como se envian los colores, definidos, o personalizados con codigo RGB  
    def disable_RGB_text(self):
        
        if self.ui_ilu.radioButton_defined_color.isChecked():
            value = True
            self.ui_ilu.lineEdit_R_code.setDisabled(value)
            self.ui_ilu.lineEdit_G_code.setDisabled(value)
            self.ui_ilu.lineEdit_B_code.setDisabled(value)
            
        if self.ui_ilu.radioButton_custom_color.isChecked():
            value = False
            self.ui_ilu.lineEdit_R_code.setDisabled(value)
            self.ui_ilu.lineEdit_G_code.setDisabled(value)
            self.ui_ilu.lineEdit_B_code.setDisabled(value)
            
    
    def get_selected_level(self, value):
        print('nivel selccionado: ',value)
        self.light_level = value
    
    def get_selected_color(self):
        color_button = self.sender()
        color_code = color_button.objectName()
        code = int(color_code.split('_')[-1])
        self.ui_ilu.lineEdit_selected_color.setText(ilumination_colors[code])
    
    def check_code(self):
        if len(self.ui_ilu.lineEdit_R_code.text()) > 3:
            self.ui_ilu.lineEdit_R_code.text()[:3]
        else: # si la longitud es menor o igual a 3
            value = int(self.ui_ilu.lineEdit_R_code.text()) if self.ui_ilu.lineEdit_R_code.text() else 0 
            # obtiene el valor como un entero
            value = max(0, min(255, value)) # asegura que el valor esté dentro del rango de 0 a 255
            self.ui_ilu.lineEdit_R_code.setText(str(value)) # actualiza el texto con el valor validado
        
        if len(self.ui_ilu.lineEdit_G_code.text()) > 3:
            self.ui_ilu.lineEdit_G_code.text()[:3]
        else: # si la longitud es menor o igual a 3
            value = int(self.ui_ilu.lineEdit_G_code.text()) if self.ui_ilu.lineEdit_G_code.text() else 0 
            # obtiene el valor como un entero
            value = max(0, min(255, value)) # asegura que el valor esté dentro del rango de 0 a 255
            self.ui_ilu.lineEdit_G_code.setText(str(value)) # actualiza el texto con el valor validado
        
        if len(self.ui_ilu.lineEdit_B_code.text()) > 3:
            self.ui_ilu.lineEdit_B_code.text()[:3]
        else: # si la longitud es menor o igual a 3
            value = int(self.ui_ilu.lineEdit_B_code.text()) if self.ui_ilu.lineEdit_B_code.text() else 0 
            # obtiene el valor como un entero
            value = max(0, min(255, value)) # asegura que el valor esté dentro del rango de 0 a 255
            self.ui_ilu.lineEdit_B_code.setText(str(value)) # actualiza el texto con el valor validado
            
    def send_color_data(self):
        selected_color_code = ''
        
        self.button_group.setExclusive(False)
        self.ui_ilu.radioButton_yes.setChecked(False)
        self.ui_ilu.radioButton_no.setChecked(False)
        self.button_group.setExclusive(True)
        self.ui_ilu.radioButton_no.setEnabled(True)
        self.ui_ilu.radioButton_yes.setEnabled(True)
        
        
        
        if self.ui_ilu.radioButton_defined_color.isChecked():
            
            print("Se envia color definido:")
            
            self.init_time = datetime.now()
            
            selected_color_code = rgb_colors[self.ui_ilu.lineEdit_selected_color.text()]
            print("color seleccionado: "+self.ui_ilu.lineEdit_selected_color.text()+" > "+selected_color_code)
            
            selected_color_code += ','+str(self.light_level)
            
            self.send_data_thread = SendDataThread(selected_color_code)
            
            self.send_data_thread.start()
            
        else:
            print("Se envia color personalizado (RGB):")
            # si los campos estan vacios, envia 255,255,255 por defecto
            r_code = '255'
            g_code = '255'
            b_code = '255'
            if self.ui_ilu.lineEdit_R_code.text() != "":
                r_code = self.ui_ilu.lineEdit_R_code.text().strip()
            if self.ui_ilu.lineEdit_G_code.text() != "":
                g_code = self.ui_ilu.lineEdit_G_code.text().strip()
            if self.ui_ilu.lineEdit_B_code.text() != "":
                b_code = self.ui_ilu.lineEdit_B_code.text().strip()
            
            selected_color_code = r_code+','+g_code+','+b_code
            
            print('Color seleccionado: '+selected_color_code)
            
            selected_color_code += ','+str(self.light_level)
            
            self.send_data_thread = SendDataThread(selected_color_code)
            
            self.send_data_thread.start()
        
        # se adjunto al color el nivel de intensidad,de la siguiente forma
        # 255,255,255,1 ; el ultimo valor corresponde la nivel de instensidad

    def does_recognize_color(self, radio_button_sender):
        
        if radio_button_sender.text() == 'SI':
            self.recognize = 'SI'
            print("Reconoce el color : SI")
        
        if radio_button_sender.text() == 'NO':
            self.recognize = 'NO'
            print("Reconoce el color : NO")
            
        self.end_time = datetime.now()
        self.ui_ilu.pushButton_save.setEnabled(True)
    
    def save_module_data(self):
        
        sel_color = ''
        reconoce_sel_color = ''
        
        
        if self.recognize == '':
            print("no se ha marcado la opcion de SI o NO")
            self.message_dialog = MessageDialog("! Reconoce el color?")
            self.message_dialog.show()
        else:
            
            self.ui_ilu.radioButton_yes.setChecked(False)
            self.ui_ilu.radioButton_no.setChecked(False)
            self.ui_ilu.radioButton_yes.setEnabled(False)
            self.ui_ilu.radioButton_no.setEnabled(False)
            self.ui_ilu.pushButton_save.setEnabled(False)
            
            # calcular tiempo que tarda en reconocer el color
        
            self.total_time = self.end_time - self.init_time
            
            if self.ui_ilu.radioButton_defined_color.isChecked():
                print("Datos a guardar (color definido):")
                sel_color = self.ui_ilu.lineEdit_selected_color.text()
                reconoce_sel_color = self.recognize
                print(sel_color + " "+ reconoce_sel_color+" "+str(self.total_time))
                
                    
            else:
                print("Datos a guardar (color personalizado):")
                sel_color = self.ui_ilu.lineEdit_R_code.text()+","+self.ui_ilu.lineEdit_G_code.text()+","+self.ui_ilu.lineEdit_B_code.text()
                reconoce_sel_color = self.recognize
                print(sel_color + " "+ reconoce_sel_color+" "+str(self.total_time))
            
            new_ilu = ModuloIluminacion(
                id_sesion = self.sesion,
                color = sel_color,
                reconoce_color = reconoce_sel_color,
                tiempo = str(self.total_time).split('.')[0]
                
            )
              
            if add_module_iluminacion(new_ilu):
                self.message_dialog = MessageDialog("!Datos guardados")
                self.message_dialog.show()
            else:
                self.message_dialog = MessageDialog("Error al guardar")
                self.message_dialog.show()
                

            
class SendDataThread(QThread):
    def __init__(self,color_data):
        super().__init__()
        
        self.color_data = color_data
        self._is_runnig = False
    def run(self):
        self._is_runnig = True
        try:
            socket_bluetooth = bluetooth.BluetoothSocket()
            socket_bluetooth.connect((module_mac_address[0],1))
            socket_bluetooth.send(self.color_data.encode('utf-8'))
            socket_bluetooth.close()
            print('codigo de color '+self.color_data+ " enviado por el puerto el socket bluetooth")
            self._is_runnig = False
        
        except Exception as ex:
            print("Error al enviar el codigo "+self.color_data)
            print(ex)
        
        
    