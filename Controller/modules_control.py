# Thread para enviar los caracteres de i (inicio) y f (finalizacion) 
# para controlar el modulo
# si se envia i prende el modulo, si se envia f lo apaga  

import sys
import serial, threading

sys.path.append(".")
from datetime import datetime
from datetime import time 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QRadioButton
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal

class TurnOnOffModule(QThread):
    def __init__(self, port, signal_code):
        super().__init__()
        self._is_runnig = False
        self.code = signal_code
        self.com_port = port
        
        
    def run(self):
        self._is_runnig = True
        try:
            serial_port = serial.Serial(self.com_port, 9600)
            serial_port.write(self.code.encode())
            serial_port.close()
            print("caracter  " + self.code+" enviado por el puerto: "+self.com_port)
            self._is_runnig = False
        except serial.SerialException as ex:
            print("Error en la conexion serial: ", ex)
        except Exception as ex:
            print("Error al enviar el caracter "+self.code)
            print(ex)

