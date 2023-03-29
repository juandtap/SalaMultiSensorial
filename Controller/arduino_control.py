import sys
sys.path.append(".")
import serial, time
from PyQt5.QtCore import QThread, pyqtSignal

class ArduinoThread(QThread):
    # Señal para enviar datos a la ventana modulo grafomotricidad
    actualizar_datos = pyqtSignal(str)

    def __init__(self, port, baud_rate, listen_time):
        super().__init__()
        self.port = port
        self.baud_rate = baud_rate
        self.listen_time = listen_time  # valor en segundos

    def run(self):
        init_time = time.time()
        
        with serial.Serial(self.port, self.baud_rate) as ser:
            while (time.time() - init_time) < self.listen_time:
                # Esperar hasta que haya datos disponibles
                if ser.in_waiting > 0:
                    # Leer los datos
                    datos = ser.readline().decode().rstrip()
                    # Enviar los datos a la ventana modulo
                    self.actualizar_datos.emit(datos)