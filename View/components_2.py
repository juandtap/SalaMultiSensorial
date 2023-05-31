# este modulo es para la ventana de reportes del estudiante

import sys
from PyQt5 import QtCore
sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QSizePolicy, QVBoxLayout, QLabel, QComboBox, QFileDialog,QTableWidget, QAbstractItemView, QTableWidgetItem, QHeaderView, QAbstractScrollArea
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import  QStandardItemModel , QColor, QBrush, QFont
from datetime import time, date

from View.student_report_view import Ui_Form_student_report
from Controller.session_control import get_session_by_student_id, get_sesion_by_id
from Controller.report_control import Report

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
        self.download_report = 'descargar reporte'
        
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
        self.table_reports.setColumnCount(6)
        self.table_reports.setHorizontalHeaderLabels(
            [
                'Sesion',
                'Fecha',
                'Hora Inicio',
                'Hora Fin',
                'Ver Modulos ',
                'Descargar Reporte de la Sesion'              
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
        
        self.student_sessions_list = self.student.sesiones
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
                self.table_reports.setItem(i, 5, QTableWidgetItem(self.download_report+"-"+(str(sesion.id))))
                self.table_reports.item(i,5).setFont(self.font_table)
        
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
        # la  columna 4 es para abrir la ventana donde se muestran el resto de tablas
        # la 5 (ultima) es para descargar en pdf el reporte
        show_modules_pos = 4
        download_pos = 5
        item = self.table_reports.item(row, 4)
        id_ses = item.text().split('-')[-1]
        print("id sesion : "+id_ses)
        
        
        if column == show_modules_pos:
            self.ui_rep.label_back.setHidden(False)
            self.ui_rep.scrollArea.takeWidget().deleteLater()
            self.ui_rep.scrollArea.setWidgetResizable(False)
           
            self.ui_rep.scrollArea.setWidget(self.load_modules_tables(id_ses))
            
            self.ui_rep.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
       
        # recupera la sesion y muestra la info de los modulos
        elif column == download_pos:
            print("Se descarga reporte de la sesion "+id_ses)
            report = Report(self.student, id_ses)
            report.download_report()
            
       

    # esta funcion muestra los modulos trabajados en cada sesion
    
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
        
        
        
         # guarda los datos del Modulo de grafomotricidad en una lista y los muestra en una tabla
        grafomotricidad_list = self.sesion_selected.modulos_grafomotricidad
        # datos del modulo vumetro
        vumetro_list = self.sesion_selected.modulos_vumetro
        # data del modulo de iluminacion
        iluminacion_list = self.sesion_selected.modulos_iluminacion
        
        
        if grafomotricidad_list:
            
            # muestra el nombre del primer modulo
            label_grafomotricidad = QLabel("Modulo Grafomotricidad")
            label_grafomotricidad.setFont(self.font)
            layout.addWidget(label_grafomotricidad)
            
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
            
            

            self.table_grafomotricidad.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
            self.table_grafomotricidad.resize(self.ui_rep.scrollArea.width(),self.ui_rep.scrollArea.height())
            

                            
            for i, module in enumerate(grafomotricidad_list):
                self.table_grafomotricidad.insertRow(i)
                self.table_grafomotricidad.setItem(i, 0, QTableWidgetItem(str(module.id)))
                self.table_grafomotricidad.setItem(i, 1, QTableWidgetItem(str(module.figura)))
                self.table_grafomotricidad.setItem(i, 2, QTableWidgetItem(str(module.tiempo_tomado).split('.')[0]))
                self.table_grafomotricidad.setItem(i, 3, QTableWidgetItem(str(module.resultado)))
                
            
            
            #este codigo hace que las columnas  no sean redimensionables
            header = self.table_grafomotricidad.horizontalHeader()
            
            for i in range(header.count()):
                header.setSectionResizeMode(i,QHeaderView.ResizeToContents)
        
        # Modulo Vumetro
        # repite el proceso pero para el modulo vumetro
        
        if vumetro_list:
        
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
                    'nivel maximo',
                    'nivel promedio',
                    'tiempo',
                    
                ]
            )
            
            self.table_vumetro.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.table_vumetro.setSelectionBehavior(QAbstractItemView.SelectRows)
            
            # hace que la ultima columna ocupe el espacio restante de la tabla
            self.table_vumetro.horizontalHeader().setStretchLastSection(True)
            
            self.table_vumetro.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
            self.table_vumetro.resize(self.ui_rep.scrollArea.width(),self.ui_rep.scrollArea.height())
            
            # este codigo hace que las columnas  no sean redimensionables
            header = self.table_vumetro.horizontalHeader()
            
            for i in range(header.count()):
                header.setSectionResizeMode(i,QHeaderView.ResizeToContents)
                
            for i, module in enumerate(vumetro_list):
                self.table_vumetro.insertRow(i)
                self.table_vumetro.setItem(i, 0, QTableWidgetItem(str(module.id)))
                self.table_vumetro.setItem(i, 1, QTableWidgetItem(str(module.nivel_maximo)))
                self.table_vumetro.setItem(i, 2, QTableWidgetItem(str(module.nivel_promedio)))
                self.table_vumetro.setItem(i, 3, QTableWidgetItem(str(module.tiempo).split('.')[0]))
            
        # Modulo Iluminacion
        
        if iluminacion_list:
        
            label_iluminacion = QLabel("Modulo Iluminacion")
            label_iluminacion.setFont(self.font)
            layout.addWidget(label_iluminacion)
            
            self.table_iluminacion = QTableWidget()
            layout.addWidget(self.table_iluminacion)
            
            self.table_iluminacion.verticalHeader().setVisible(False)
            # # defino las columnas de la tabla
            self.table_iluminacion.setColumnCount(4)
            self.table_iluminacion.setHorizontalHeaderLabels(
                [
                    'id',
                    'Color',
                    'Reconoce color',
                    'Tiempo',
                    
                ]
            )
            
            self.table_iluminacion.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.table_iluminacion.setSelectionBehavior(QAbstractItemView.SelectRows)
            
            # # hace que la ultima columna ocupe el espacio restante de la tabla
            self.table_iluminacion.horizontalHeader().setStretchLastSection(True)
            
            self.table_iluminacion.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
            self.table_iluminacion.resize(self.ui_rep.scrollArea.width(),self.ui_rep.scrollArea.height())
            
            # # este codigo hace que las columnas  no sean redimensionables
            header = self.table_iluminacion.horizontalHeader()
            for i in range(header.count()):
                header.setSectionResizeMode(i,QHeaderView.ResizeToContents)
                
            for i, module in enumerate(iluminacion_list):
                self.table_iluminacion.insertRow(i)
                self.table_iluminacion.setItem(i, 0, QTableWidgetItem(str(module.id)))
                self.table_iluminacion.setItem(i, 1, QTableWidgetItem(str(module.color)))
                self.table_iluminacion.setItem(i, 2, QTableWidgetItem(str(module.reconoce_color)))
                self.table_iluminacion.setItem(i, 3, QTableWidgetItem(str(module.tiempo).split('.')[0]))
        
        
        # label_pictograma = QLabel("Modulo Pictogramas")
        # label_pictograma.setFont(self.font)
        # layout.addWidget(label_pictograma)
        
           

        return container
       
        
        
        
        
        
       
            
        
        
        
        
       
    