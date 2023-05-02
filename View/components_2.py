import sys
sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QFileDialog, QAbstractItemView, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import  QStandardItemModel  
from datetime import time, date

from View.student_report_view import Ui_Form_student_report
from Controller.session_control import get_session_by_student_id

class StudentReport(QWidget):
    def __init__(self, student):
        super().__init__()
        self.ui_rep = Ui_Form_student_report()
        self.ui_rep.setupUi(self)
        self.student = student
        
        self.load_info_student()
       
        # variable temporal borrar despues
        self.download = 'enlace descarga'
        
        self.set_table()
        
        self.load_table()   
        
       
    def set_table(self):
         
        # defino las columnas de la tabla
        self.ui_rep.tableWidget.setColumnCount(5)
        self.ui_rep.tableWidget.setHorizontalHeaderLabels(
            [
                'Sesion',
                'Fecha',
                'Hora Inicio',
                'Hora Fin',
                'Ver/Descargar'
            ]
        )
        
        self.ui_rep.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui_rep.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        # hace que la ultima columna ocupe el espacio restante de la tabla
        self.ui_rep.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        # este codigo hace que las columnas  no sean redimensionables
        header = self.ui_rep.tableWidget.horizontalHeader()
        
        for i in range(header.count()):
            header.setSectionResizeMode(i,QHeaderView.Fixed)
            
        
    
    def load_table(self):
         # recuperar de la DB las sesiones del estudiante
        self.student_sessions_list = get_session_by_student_id(self.student.id)
        if self.student_sessions_list:
            # la lista contiene elementos
            # Agregar las filas a la tabla
            for i, sesion in enumerate(self.student_sessions_list):
                self.ui_rep.tableWidget.insertRow(i)
                self.ui_rep.tableWidget.setItem(i, 0, QTableWidgetItem(str(sesion.id)))
                self.ui_rep.tableWidget.setItem(i, 1, QTableWidgetItem(str(sesion.fecha)))
                self.ui_rep.tableWidget.setItem(i, 2, QTableWidgetItem(str(sesion.hora_inicio)))
                self.ui_rep.tableWidget.setItem(i, 3, QTableWidgetItem(str(sesion.hora_fin)))
                self.ui_rep.tableWidget.setItem(i, 4, QTableWidgetItem(self.download))
        
    
    def load_info_student(self):
        self.ui_rep.label_cedula.setText(self.student.cedula)
        self.ui_rep.label_apellidos.setText(self.student.apellidos)
        self.ui_rep.label_nombres.setText(self.student.nombres)         
        
        

