# este modulo es para la ventana de reportes del estudiante

import sys
from PyQt5 import QtCore
sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QSizePolicy, QVBoxLayout, QLabel, QComboBox, QFileDialog,QTableWidget, QAbstractItemView, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import  QStandardItemModel , QColor, QBrush, QFont
from datetime import time, date

from View.student_report_view import Ui_Form_student_report
from Controller.session_control import get_session_by_student_id, get_sesion_by_id

class StudentReport(QWidget):
    def __init__(self, student):
        super().__init__()
        self.ui_rep = Ui_Form_student_report()
        self.ui_rep.setupUi(self)
        self.student = student
        
        self.load_info_student()
        
       
       
        # esconder label de regresar
        self.ui_rep.label_back.setHidden(True)
        
        # fuente para los enlaces
        self.font_table = QFont('Arial',10)
        self.font_table.setUnderline(True)
        
        # fuente para las label de tablas
        self.font = QFont('Arial', 10)
        self.font.setBold(True)
        
        # fuente label back
        self.font_in = QFont('Arial',10,1,True)
        self.font_in.setBold(True)
        self.font_in.setUnderline(True)
        self.font_out = QFont('Arial',10,1,True)
        self.font_out.setBold(False)
        self.font_out.setUnderline(True)
        
        
        # variable temporal borrar despues
        self.download = 'ver modulos'
        
        self.ui_rep.scrollArea.setWidgetResizable(True)

        
        self.set_table()
        
        self.load_table()   
        
        self.table_reports.cellClicked.connect(self.show_reports)
        
        # evento label: Regresar
       
        self.ui_rep.label_back.mousePressEvent = self.back_to
        self.ui_rep.label_back.enterEvent = self.mouse_over
        self.ui_rep.label_back.leaveEvent = self.mouse_out
        
    
    def mouse_over(self, event):
        self.ui_rep.label_back.setFont(self.font_in)
    
    def mouse_out(self,event):
        self.ui_rep.label_back.setFont(self.font_out)
        
    
    
       
    def set_table(self):
        
        self.table_reports = QTableWidget()
        self.area_table = QWidget()
        self.area_table_layout = QVBoxLayout()
        self.area_table.setLayout(self.area_table_layout)
        
        self.area_table_layout.addWidget(self.table_reports)
        
        #self.ui_rep.scrollArea.setMinimumWidth(1100)
        #self.ui_rep.scrollArea.setMinimumHeight(400)
        self.ui_rep.scrollArea.setWidgetResizable(True)
        self.ui_rep.scrollArea.setWidget(self.area_table)
        
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
                self.table_reports.setItem(i, 2, QTableWidgetItem(str(sesion.hora_inicio).split('.')[0]))
                self.table_reports.setItem(i, 3, QTableWidgetItem(str(sesion.hora_fin).split('.')[0]))
                self.table_reports.setItem(i, 4, QTableWidgetItem(self.download+"-"+(str(sesion.id))))
                self.table_reports.item(i,4).setFont(self.font_table)
                
        
    def back_to(self, event):
        print("se hizo click en la label back")
        self.ui_rep.scrollArea.takeWidget().deleteLater()
        self.set_table()
        self.load_table()
        self.ui_rep.scrollArea.setWidget(self.area_table)
        self.table_reports.cellClicked.connect(self.show_reports)
        self.ui_rep.label_back.setHidden(True)  
    
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
        
        self.ui_rep.label_back.setHidden(False)
        
        self.ui_rep.scrollArea.takeWidget().deleteLater()
       
        
        self.ui_rep.scrollArea.setWidget(self.load_modules_tables(id_ses))
       
        # recupera la sesion y muestra la info de los modulos
        # crear QWidget para mostrar la info de los modulos
        # probar conectarse, enviar y recibir datos por bluetooth usando MAC y no el puerto

    def load_modules_tables(self, id_ses):
        container = QWidget()
        
        layout = QVBoxLayout()
        container.setLayout(layout)
        
        # se recupera los datos de los modulos de la sesion
        # la sesion tiene una lista por cada modulo
        
        self.sesion_selected = get_sesion_by_id(id_ses)
        
        # muestra el id de la sesion y la fecha
        label_info_sesion = QLabel('Sesion '+str(self.sesion_selected.id)+" Fecha: "+str(self.sesion_selected.fecha))
        label_info_sesion.setFont(self.font)
        layout.addWidget(label_info_sesion)
        
        # muestra el nombre del primer modulo
        label_grafomotricidad = QLabel("Modulo Grafomotricidad")
        label_grafomotricidad.setFont(self.font)
        layout.addWidget(label_grafomotricidad)
        
         # guarda los datos del Modulo de grafomotricidad en una lista y los muestra en una tabla
        grafomotricidad_list = self.sesion_selected.modulos_grafomotricidad
        
        # crea la tabla donde muestra los datos del modulo de grafomotricidad
        self.table_grafomotricidad = QTableWidget()
        layout.addWidget(self.table_grafomotricidad)
        
        # configura la tabla
        self.table_grafomotricidad.verticalHeader().setVisible(False)
        # defino las columnas de la tabla
        self.table_grafomotricidad.setColumnCount(4)
        self.table_grafomotricidad.setHorizontalHeaderLabels(
            [
                'id',
                'Figura',
                'Tiempo Tomado',
                'Resultado',
                
            ]
        )
        
        self.table_grafomotricidad.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_grafomotricidad.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        # hace que la ultima columna ocupe el espacio restante de la tabla
        self.table_grafomotricidad.horizontalHeader().setStretchLastSection(True)
        
        # este codigo hace que las columnas  no sean redimensionables
        header = self.table_grafomotricidad.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i,QHeaderView.Fixed)
            
        for i, module in enumerate(grafomotricidad_list):
            self.table_grafomotricidad.insertRow(i)
            self.table_grafomotricidad.setItem(i, 0, QTableWidgetItem(str(module.id)))
            self.table_grafomotricidad.setItem(i, 1, QTableWidgetItem(str(module.figura)))
            self.table_grafomotricidad.setItem(i, 2, QTableWidgetItem(str(module.tiempo_tomado).split('.')[0]))
            self.table_grafomotricidad.setItem(i, 3, QTableWidgetItem(str(module.resultado)))
        
        # Modulo Vumetro
        # repite el proceso pero para el modulo vumetro
        # se usan los datos del modulo de grafomotricidad por el momento
        
        label_vumetro = QLabel("Modulo Vumetro")
        label_vumetro.setFont(self.font)
        layout.addWidget(label_vumetro)
        
        self.table_vumetro = QTableWidget()
        layout.addWidget(self.table_vumetro)
        
        self.table_vumetro.verticalHeader().setVisible(False)
        # defino las columnas de la tabla
        self.table_vumetro.setColumnCount(4)
        self.table_vumetro.setHorizontalHeaderLabels(
            [
                'id',
                'Figura',
                'Tiempo Tomado',
                'Resultado',
                
            ]
        )
        
        self.table_vumetro.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_vumetro.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        # hace que la ultima columna ocupe el espacio restante de la tabla
        self.table_vumetro.horizontalHeader().setStretchLastSection(True)
        
        # este codigo hace que las columnas  no sean redimensionables
        header = self.table_vumetro.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i,QHeaderView.Fixed)
            
        for i, module in enumerate(grafomotricidad_list):
            self.table_vumetro.insertRow(i)
            self.table_vumetro.setItem(i, 0, QTableWidgetItem(str(module.id)))
            self.table_vumetro.setItem(i, 1, QTableWidgetItem(str(module.figura)))
            self.table_vumetro.setItem(i, 2, QTableWidgetItem(str(module.tiempo_tomado).split('.')[0]))
            self.table_vumetro.setItem(i, 3, QTableWidgetItem(str(module.resultado)))
            
        # Modulo Iluminacion
        
        # label_iluminacion = QLabel("Modulo Iluminacion")
        # label_iluminacion.setFont(self.font)
        # layout.addWidget(label_iluminacion)
        
        # self.table_iluminacion = QTableWidget()
        # layout.addWidget(self.table_iluminacion)
        
        # self.table_iluminacion.verticalHeader().setVisible(False)
        # # defino las columnas de la tabla
        # self.table_iluminacion.setColumnCount(4)
        # self.table_iluminacion.setHorizontalHeaderLabels(
        #     [
        #         'id',
        #         'Figura',
        #         'Tiempo Tomado',
        #         'Resultado',
                
        #     ]
        # )
        
        # self.table_iluminacion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.table_iluminacion.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        # # hace que la ultima columna ocupe el espacio restante de la tabla
        # self.table_iluminacion.horizontalHeader().setStretchLastSection(True)
        
        # # este codigo hace que las columnas  no sean redimensionables
        # header = self.table_iluminacion.horizontalHeader()
        # for i in range(header.count()):
        #     header.setSectionResizeMode(i,QHeaderView.Fixed)
            
        # for i, module in enumerate(grafomotricidad_list):
        #     self.table_iluminacion.insertRow(i)
        #     self.table_iluminacion.setItem(i, 0, QTableWidgetItem(str(module.id)))
        #     self.table_iluminacion.setItem(i, 1, QTableWidgetItem(str(module.figura)))
        #     self.table_iluminacion.setItem(i, 2, QTableWidgetItem(str(module.tiempo_tomado).split('.')[0]))
        #     self.table_iluminacion.setItem(i, 3, QTableWidgetItem(str(module.resultado)))
        
        
        # label_pictograma = QLabel("Modulo Pictogramas")
        # label_pictograma.setFont(self.font)
        # layout.addWidget(label_pictograma)
        
           

        return container
       
        
        
        
        
        
       
            
        
        
        
        
       
    