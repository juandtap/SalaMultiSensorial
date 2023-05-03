# este modulo es para la ventana de reportes del estudiante

import sys
sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox, QFileDialog,QTableWidget, QAbstractItemView, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import  QStandardItemModel , QColor, QBrush, QFont
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
       
       
        # esconder label de regresar
        self.ui_rep.label_back.setHidden(True)
       
        self.font_table = QFont('Arial',10)
        self.font_table.setUnderline(True)
        
        # variable temporal borrar despues
        self.download = 'ver modulos'
        
        self.table_reports = QTableWidget()
        self.area_table = QWidget()
        area_table_layout = QVBoxLayout()
        self.area_table.setLayout(area_table_layout)
        
        area_table_layout.addWidget(self.table_reports)
        
        self.ui_rep.scrollArea.setWidget(self.area_table)
        
        self.set_table()
        
        self.load_table()   
        
        self.table_reports.cellClicked.connect(self.show_reports)
        
       
    def set_table(self):
        self.table_reports.verticalHeader().setVisible(False)
        # defino las columnas de la tabla
        self.table_reports.setColumnCount(5)
        self.table_reports.setHorizontalHeaderLabels(
            [
                'Sesion',
                'Fecha',
                'Hora Inicio',
                'Hora Fin',
                'Ver Modulos '
            ]
        )
        
        self.table_reports.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_reports.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        # hace que la ultima columna ocupe el espacio restante de la tabla
        self.table_reports.horizontalHeader().setStretchLastSection(True)
        
        # este codigo hace que las columnas  no sean redimensionables
        header = self.table_reports.horizontalHeader()
        
        for i in range(header.count()):
            header.setSectionResizeMode(i,QHeaderView.Fixed)
            
        
    
    def load_table(self):
         # recuperar de la DB las sesiones del estudiante
        self.student_sessions_list = get_session_by_student_id(self.student.id)
        if self.student_sessions_list:
            # la lista contiene elementos
            # Agregar las filas a la tabla
            for i, sesion in enumerate(self.student_sessions_list):
                self.table_reports.insertRow(i)
                self.table_reports.setItem(i, 0, QTableWidgetItem(str(sesion.id)))
                self.table_reports.setItem(i, 1, QTableWidgetItem(str(sesion.fecha)))
                self.table_reports.setItem(i, 2, QTableWidgetItem(str(sesion.hora_inicio)))
                self.table_reports.setItem(i, 3, QTableWidgetItem(str(sesion.hora_fin)))
                self.table_reports.setItem(i, 4, QTableWidgetItem(self.download+"-"+(str(sesion.id))))
                self.table_reports.item(i,4).setFont(self.font_table)
                
                
    
    def load_info_student(self):
        self.ui_rep.label_cedula.setText(self.student.cedula)
        self.ui_rep.label_apellidos.setText(self.student.apellidos)
        self.ui_rep.label_nombres.setText(self.student.nombres)         
        
        
    def show_reports(self, row, column):
        # la ultima columna para abrir la ventana donde se muestran el resto de tablas
        show_modules_pos = 4
        item = self.table_reports.item(row, 4)
        id_ses = item.text().split('-')[-1]
        print("id sesion : "+id_ses)
        
        # recupera la sesion y muestra la info de los modulos
        # crear QWidget para mostrar la info de los modulos
        # probar conectarse, enviar y recibir datos por bluetooth usando MAC y no el puerto
        
