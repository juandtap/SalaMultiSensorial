import sys
sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox
from PyQt5.QtCore import Qt, QDate
from View.module_selection_view import Ui_Form_seleccion_modulos

class ModuleSelection(QWidget):
    def __init__(self, student):
        super().__init__()
        self.ui_modules = Ui_Form_seleccion_modulos()
        self.ui_modules.setupUi(self)
        self.student = student
        self.load_info_student()
        
        
    def load_info_student(self):
        self.ui_modules.label_cedula.setText(self.student.cedula)
        self.ui_modules.label_apellidos.setText(self.student.apellidos)
        self.ui_modules.label_nombres.setText(self.student.nombres)


        
