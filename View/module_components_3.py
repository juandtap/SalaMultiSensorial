# Este modulo controla la ventana del modulo Iluminacion

import sys

sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QPushButton
from PyQt5.QtCore import Qt, QDate, QTimer, QTime, QThread, pyqtSignal, QRectF
from PyQt5.QtGui import QPixmap, QPen, QBrush, QColor, QIntValidator
from PyQt5.QtCore import QTimer
from Controller.module_codes import ilumination_colors
from View.module_iluminacion_view import Ui_Form_modulo_iluminacion

class ModuleIlumination(QWidget):
    def __init__(self, sesion, com_port):
        super().__init__()
        self.ui_ilu = Ui_Form_modulo_iluminacion()
        self.ui_ilu.setupUi(self)
        self.sesion = sesion
        self.port = com_port
        self.set_module_images()
        self.ui_ilu.label_text_status.setHidden(True)
        self.ui_ilu.label_conn_status.setHidden(True)
        
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
        
        # defino el color rojo por defecto para evitar valores nullos al momento de enviar datos
        
        self.ui_ilu.lineEdit_selected_color.setText(ilumination_colors[1])
        
        # valido que los datos para el codigo RGB solo ingresen numeros entre  0-255
        self.ui_ilu.lineEdit_R_code.setValidator(QIntValidator(0,255))
        self.ui_ilu.lineEdit_R_code.textChanged.connect(self.check_code)
        
        self.ui_ilu.lineEdit_G_code.setValidator(QIntValidator(0,255))
        self.ui_ilu.lineEdit_G_code.textChanged.connect(self.check_code)
        
        self.ui_ilu.lineEdit_B_code.setValidator(QIntValidator(0,255))
        self.ui_ilu.lineEdit_B_code.textChanged.connect(self.check_code)
        
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
        print('evento del radio button '+ str(self.ui_ilu.radioButton_defined_color.isChecked()))
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