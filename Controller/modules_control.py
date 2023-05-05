# Thread para enviar los caracteres de i (inicio) y f (finalizacion) 
# para controlar el modulo
# si se envia i prende el modulo, si se envia f lo apaga  

import sys
import serial, bluetooth

sys.path.append(".")
from datetime import datetime
from datetime import time 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QRadioButton
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal
from module_codes import module_mac_address

class TurnOnOffModule(QThread):
    def __init__(self, port, signal_code):
        super().__init__()
        self._is_runnig = False
        self.code = signal_code
        self.com_port = port
        
        
    def run(self):
        self._is_runnig = True
        try:
            socket_bluetooth = bluetooth.BluetoothSocket()
            socket_bluetooth.connect(module_mac_address[0],1)
            socket_bluetooth.send(self.code.encode('utf-8'))
            socket_bluetooth.close()
            
            print("caracter  " + self.code+" enviado al modulo HC05 ")
            self._is_runnig = False
        except serial.SerialException as ex:
            print("Error en la conexion serial: ", ex)
        except Exception as ex:
            print("Error al enviar el caracter "+self.code)
            print(ex)

