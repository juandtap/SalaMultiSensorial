# Thread para enviar los caracteres de i (inicio) y f (finalizacion) 
# para controlar el modulo
# si se envia i prende el modulo, si se envia f lo apaga  

import sys
import bluetooth

sys.path.append(".")
from datetime import datetime
from datetime import time 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QRadioButton
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal
from Controller.module_codes import module_mac_address

class TurnOnOffModule(QThread):
    # envia una signal a la ventana del modulo una vez este thread 
    # libera el socket pata que los modulos puedan 
    # enviar o recibir datos por el socket sin conflictos
    my_signal = pyqtSignal(str)
    
    def __init__(self,signal_code, module):
        super().__init__()
        self._is_runnig = False
        self.code = signal_code
        self.mod_num = module
        
        
    def run(self):
        self._is_runnig = True
        try:
            socket_bluetooth = bluetooth.BluetoothSocket()
            socket_bluetooth.connect((module_mac_address[self.mod_num],1))
            socket_bluetooth.send(self.code.encode('utf-8'))
            socket_bluetooth.close()
            
            print("caracter  " + self.code+" enviado al modulo HC05 ")
            # envio de signal
            self.my_signal.emit('free')
            print("El socket bluetooth a sido liberado")
            self._is_runnig = False
        except Exception as ex:
            print("Error al enviar el caracter "+self.code)
            self.my_signal.emit('not_free')
            print(ex)

