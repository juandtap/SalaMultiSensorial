# En este modulo se encuentran las clases para :
# agregar Unidades Educatuvias, Discapacidades, Editar Estudiante, Mostrar la lista de estudiantes
# el combobox con chekitems  y la ventana de dialogo

import sys
sys.path.append(".")
from PyQt5.QtWidgets import  QVBoxLayout, QWidget, QComboBox, QFileDialog, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView
from PyQt5.QtCore import Qt, QDate, QStandardPaths, pyqtSignal
from PyQt5.QtGui import QIntValidator, QPixmap, QFont
from View.message_dialog_view import Ui_Message_dialog
from View.add_discapacidad_view import Ui_Agregar_Discapacidades
from View.add_school_view import Ui_add_Unidad_Educativa
from Controller.school_control import add_school_control, get_all_schools
from Controller.discapacidad_control import add_discapacidad_control
from View.edit_student_view import Ui_Add_student
from Controller.student_control import update_student, get_all_students, delete_student_by_id
from Controller.discapacidad_control import get_all_discapacidades
from View.student_list_view import Ui_Form_student_list
from View.confirm_dialog_view import Ui_confirm_dialog
from datetime import date
from screeninfo import get_monitors
from Controller.report_control import StudentListReport


class AddSchool(QWidget):
    
    # envia True a la ventana para recargar el combo de Unidades Educativas
    reload_flag = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()
        self.ui_add_school = Ui_add_Unidad_Educativa()
        self.ui_add_school.setupUi(self)
        self.ui_add_school.pushButton_cancel.clicked.connect(self.close)
        self.ui_add_school.pushButton_save.clicked.connect(self.add_school)
    
    def add_school(self):
        
        if self.ui_add_school.lineEdit_name_unidad_educativa.text() != "":
        
            flag = False
            
            flag = add_school_control(self.ui_add_school.lineEdit_name_unidad_educativa.text())
            
            if flag:
                self.new_message = MessageDialog("Unidad Educativa Agregada!")
                self.new_message.show()
                self.ui_add_school.lineEdit_name_unidad_educativa.clear()
                self.reload_flag.emit(True)
            else:
                self.new_message = MessageDialog("Unidad Educativa ya existe!")
                self.new_message.show()
                self.ui_add_school.lineEdit_name_unidad_educativa.clear()
        else:
            self.new_message = MessageDialog("Ingrese una Unidad Educativa!")
            self.new_message.show()
            self.ui_add_school.lineEdit_name_unidad_educativa.clear()
            

class AddDiscapacidad(QWidget):
    reload_flag = pyqtSignal(bool)
    def __init__(self):
        super().__init__()
        self.ui_add_dis = Ui_Agregar_Discapacidades()
        self.ui_add_dis.setupUi(self)
        self.ui_add_dis.pushButton_save.clicked.connect(self.add_discapacidad)
        self.ui_add_dis.pushButton_close.clicked.connect(self.close)
    
    def add_discapacidad(self):
        
        if self.ui_add_dis.line_discapacidad.text() != "":
        
            flag = False
        
            flag = add_discapacidad_control(self.ui_add_dis.line_discapacidad.text())
            if flag:
                self.new_message = MessageDialog("Discapacidad Agregada!")
                self.new_message.show()
                self.ui_add_dis.line_discapacidad.clear()
                self.reload_flag.emit(True)
            else:
                self.new_message = MessageDialog("Discapacidad ya existe!")
                self.new_message.show()
                self.ui_add_dis.line_discapacidad.clear()
        else:
            self.new_message = MessageDialog("Ingrese una Discapacidad!")
            self.new_message.show()
            self.ui_add_dis.line_discapacidad.clear()
            

class MessageDialog(QWidget):
    def __init__(self, message):
        super().__init__()
        self.ui_message = Ui_Message_dialog()
        self.ui_message.setupUi(self)
        self.message = message
        self.ui_message.label_message.setText(self.message)
        self.ui_message.pushButton_accept_dialog.clicked.connect(self.close)

class ConfirmDialog(QWidget):
    # envia true si SI, false si NO
    user_response = pyqtSignal(bool)
    
    def __init__(self, message):
        super().__init__()
        self.uiconf = Ui_confirm_dialog()
        self.uiconf.setupUi(self)
        self.message = message
        self.uiconf.label_message.setText(self.message)
        self.uiconf.pushButton_yes.clicked.connect(self.yes_option)
        self.uiconf.pushButton_no.clicked.connect(self.no_option)
        
    def yes_option(self):
        self.user_response.emit(True)
        self.close()
    
    def no_option(self):
        self.user_response.emit(False)
        self.close()

class CheckableComboBox(QComboBox):
	def __init__(self):
		super().__init__()
		self._changed = False

		self.view().pressed.connect(self.handleItemPressed)

	def setItemChecked(self, index, checked=False):
		item = self.model().item(index, self.modelColumn()) # QStandardItem object

		if checked:
			item.setCheckState(Qt.Checked)
		else:
			item.setCheckState(Qt.Unchecked)

	def handleItemPressed(self, index):
		item = self.model().itemFromIndex(index)

		if item.checkState() == Qt.Checked:
			item.setCheckState(Qt.Unchecked)
		else:
			item.setCheckState(Qt.Checked)
		self._changed = True


	def hidePopup(self):
		if not self._changed:
			super().hidePopup()
		self._changed = False

	def itemChecked(self, index):
		item = self.model().item(index, self.modelColumn())
		return item.checkState() == Qt.Checked

class EditStudent(QWidget):
    
    #Envia signasl a la ventana principal en caso de actualizar o eliminar estudiante 
    # Editar estudiante: se envia True, actualiza los datos del estudiante
    # Eliminar : se envia False limpia la ventana
    editFlag = pyqtSignal(bool)
    
    def __init__(self, student):
        
        
        
        super().__init__()
        self.ui_edit = Ui_Add_student()
        self.ui_edit.setupUi(self)
        self.student = student
        self.ui_edit.pushButton_add_discapacidad.setEnabled(False)
        self.ui_edit.pushButton_add_unidad_educativa.setEnabled(False)
        #self.ui_edit.lineEdit_cedula.setEnabled(False)
        self.load_schools()
        self.filename = None
        
         # calendar picker
        self.ui_edit.dateEdit_estudiante.setCalendarPopup(True)
        self.ui_edit.dateEdit_estudiante.setStyleSheet("background-color : rgb(200, 200, 200);")
        
        # ComboBox Opcion Multiple
        self.checkeable_combo = CheckableComboBox()
        self.ui_edit.gridLayout_2.addWidget(self.checkeable_combo, 1,1,1,1)
        
        self.load_discapacidades()
         # eventos ComboBox Discapacidades
        self.checkeable_combo.activated.connect(self.get_selected_discapacidades)
         # revisa que el campo cedula no exeda los 10 caracteres y solo se ingresen numeros
        validator = QIntValidator(self)
        validator.setRange(0,999999999)
        self.ui_edit.lineEdit_cedula.setValidator(validator)
        self.ui_edit.lineEdit_cedula_representante.setValidator(validator)
        self.ui_edit.lineEdit_cedula.textChanged.connect(self.check_cedula_fields)
        self.ui_edit.lineEdit_cedula_representante.textChanged.connect(self.check_cedula_representate_fields)
        
        self.ui_edit.pushButton_cancel.clicked.connect(self.close)
        self.ui_edit.pushButton_save.clicked.connect(self.edit_student)
        self.ui_edit.pushButton_load_picture.clicked.connect(self.load_image)
        self.ui_edit.pushButton_delete.clicked.connect(self.delete_student)
        
        self.check_guest_user()
        
        self.load_info_student()
        
    def check_guest_user(self):
        if self.student.id == 1:
            self.ui_edit.lineEdit_cedula.setReadOnly(True)
            self.ui_edit.lineEdit_apellido.setReadOnly(True)
            self.ui_edit.lineEdit_nombre.setReadOnly(True)
            self.ui_edit.lineEdit_cedula_representante.setReadOnly(True)
            self.ui_edit.lineEdit_representante.setReadOnly(True)
            
    
    def delete_student(self):
        print("Confirmar eliminacion de estudiante: ")
        self.confirm_dialog = ConfirmDialog("Seguro que desea eliminar ?")
        self.confirm_dialog.user_response.connect(self.confirm_delete_action)
        self.confirm_dialog.show()
        
    def confirm_delete_action(self, reponse):
        if reponse:
            print("Si, se eliminar el usuario")
            if self.student.id == 1:
                print("Usuario Invitado no puede eliminarse")
                self.message_dialog = MessageDialog("Invitado no puede eliminarse!")
                self.message_dialog.show()
                self.close()
            else:
                print("eliminando estudiante...")
                if delete_student_by_id(self.student.id):
                    print("estudiante eliminado")
                    self.message_dialog = MessageDialog("Estudiante Eliminado!")
                    self.message_dialog.show()
                    self.editFlag.emit(False)
                    self.close()
                else:
                    self.message_dialog = MessageDialog("Error al eliminar!")
                    self.message_dialog.show()
                    self.close()
                    
                    
        else:
            print("No, se cancela")
            
    
    def load_schools(self):
        self.ui_edit.comboBox_unidad_educativa.clear()
        self.ui_edit.comboBox_unidad_educativa.addItem("Sin especificar")
        # obtengo todos los objetos de tipo Unidad_educativa
        school_list = get_all_schools()
        # separo los nombres en otra lista
        self.school_names = []
        for sc in school_list:
            self.school_names.append(sc.nombre)
        self.ui_edit.comboBox_unidad_educativa.addItems(self.school_names)
    
    def load_info_student(self):
        self.ui_edit.lineEdit_cedula.setText(self.student.cedula)
        self.ui_edit.lineEdit_apellido.setText(self.student.apellidos)
        self.ui_edit.lineEdit_nombre.setText(self.student.nombres)
        self.ui_edit.lineEdit_cedula_representante.setText(self.student.cedula_representante)
        self.ui_edit.lineEdit_representante.setText(self.student.nombre_representante)
        self.ui_edit.dateEdit_estudiante.setDate(
            QDate(
                self.student.fecha_nacimiento.year,
                self.student.fecha_nacimiento.month,
                self.student.fecha_nacimiento.day
            )
        )
        
        self.ui_edit.lineEdit_telefono.setText(self.student.telefonos)
        self.ui_edit.lineEdit_direccion_est.setText(self.student.direccion)
        self.ui_edit.checkBox_discapacidad.setChecked(self.student.discapacidad)
        self.ui_edit.comboBox_unidad_educativa.setCurrentIndex(self.student.id_unidad_educativa)
        # cargar discapacidades
        self.load_discapacidades_from_student()
        
        self.ui_edit.label_file_name.setText("")
        self.get_selected_discapacidades()
        
    def load_discapacidades_from_student(self):
        student_disc_list = []
        for dis in self.student.discapacidades:
            student_disc_list.append(dis)
        print("Discapacidades del estudiante:")
        student_disc_indexes = []
        for i in range(len(student_disc_list)):
            print(student_disc_list[i].nombre_discapacidad)
            student_disc_indexes.append(student_disc_list[i].id)
        # marcar items del checkComboBox
        print("indices de las discapacidades del estudiante")
        for indice in student_disc_indexes:
            print(str(indice))
            self.checkeable_combo.setItemChecked(indice, True)
        
        if len(student_disc_indexes) == 0:
            self.checkeable_combo.setCurrentIndex(0)
        else:
            self.checkeable_combo.setCurrentIndex(student_disc_indexes[0])
        # cargarlas tambien a la lista
        
    
    def load_discapacidades(self):
        # cargar desde la base de datos 
        self.checkeable_combo.clear()
        discapacidades_list = get_all_discapacidades()
        # primera opcion : Sin especificar
        self.checkeable_combo.addItem("Sin especificar")
        self.checkeable_combo.setItemChecked(0, False)
        for i in range(len(discapacidades_list)):
            self.checkeable_combo.addItem(discapacidades_list[i].nombre_discapacidad)
            self.checkeable_combo.setItemChecked(i+1, False)
    
    
    
    
    def get_selected_discapacidades(self):
        self.ui_edit.listDiscapacidades.clear()
        for i in range(self.checkeable_combo.count()):
            print('Index: {0} is checked {1}'.format(i, self.checkeable_combo.itemChecked(i)))
            if self.checkeable_combo.itemChecked(i):
                self.ui_edit.listDiscapacidades.addItem(self.checkeable_combo.itemText(i))
      
    def get_student_discapacidades(self):
        
        student_discapacidades = []
        for i in range(self.ui_edit.listDiscapacidades.count()):
            student_discapacidades.append(self.ui_edit.listDiscapacidades.item(i).text())
            print("Lo que agrega el combo al seleccionar: "+self.ui_edit.listDiscapacidades.item(i).text())
        print("Discapacidade seleccionadas: ")
        print(student_discapacidades)
        return student_discapacidades
    
    
    
    def check_cedula_fields(self, text_cedula):
        if len(text_cedula) > 10:
            self.ui_edit.lineEdit_cedula.setText(text_cedula[:10])
            self.ui_edit.lineEdit_cedula.setCursorPosition(10)
    
    def check_cedula_representate_fields(self, text_cedula):
        if len(text_cedula) > 10:
            self.ui_edit.lineEdit_cedula_representante.setText(text_cedula[:10])
            self.ui_edit.lineEdit_cedula_representante.setCursorPosition(10)
            
    def load_image(self):
        folder_path = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        file_dialog = QFileDialog()
        file_dialog.setDirectory(folder_path)
        self.filename = file_dialog.getOpenFileName(filter="Image (*.*)")[0]
        print(self.filename)
        self.ui_edit.label_file_name.setText(self.filename)
    
    def edit_student(self):
        
        flag = False
              
        new_student_data = [
            self.ui_edit.lineEdit_cedula.text(),
            self.ui_edit.lineEdit_apellido.text(),
            self.ui_edit.lineEdit_nombre.text(),
            self.ui_edit.lineEdit_cedula_representante.text(),
            self.ui_edit.lineEdit_representante.text(),
            date(
                self.ui_edit.dateEdit_estudiante.date().year(),
                self.ui_edit.dateEdit_estudiante.date().month(),
                self.ui_edit.dateEdit_estudiante.date().day()
            ),
            self.ui_edit.lineEdit_direccion_est.text(),
            self.ui_edit.lineEdit_telefono.text(),
            self.ui_edit.checkBox_discapacidad.isChecked(),
            self.filename, # image path
            self.ui_edit.comboBox_unidad_educativa.currentIndex(),
            self.get_student_discapacidades(),
        ]
     
        flag = update_student(self.student.id,new_student_data)
           
        if flag:
            self.edit_message = MessageDialog("Datos Estudiante Actualizados")
            self.edit_message.show()
            # envia signal a la ventana principal para que actualize los datos
            self.editFlag.emit(True)
            # cerrar ventana edicion estudiante
            self.close()
        else:
            self.edit_message = MessageDialog("Error!")
            self.edit_message.show()
            # cerrar ventana edicion estudiante
            self.close()
            

class StudentList(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_list = Ui_Form_student_list()
        self.ui_list.setupUi(self)
       
        self.set_logos()
        # Fuente label 
        self.font_over = QFont('Arial',10,1,True)
        self.font_over.setBold(True)
        self.font_over.setUnderline(True)
        self.font_out = QFont('Arial',10,1,True)
        self.font_out.setBold(False)
        self.font_out.setUnderline(True)
        
        # guardo todos los estudiantes en la lista
        self.student_list = get_all_students()
        
        # cargo la tabla de estudiante
        self.set_table()
        self.load_table()
        
        
        # y muestro los datos en la tabla
        print("recuperado la lista de estudiantes")
        
        self.ui_list.label_list.mousePressEvent =  self.download_list
        self.ui_list.label_list.enterEvent = self.mouse_over
        self.ui_list.label_list.leaveEvent = self.mouse_out
    
    
        
    def download_list(self, event):
        print("Descargando lista de estudiantes")
        student_report_list = StudentListReport(self.student_list)
        if student_report_list.download_list():
            self.message = MessageDialog("Reporte Guardado en Descargas")
            self.message.show()
    
    def set_logos(self):
        pixmap1 = QPixmap("Assets/logo1.png")
        self.ui_list.label_logo1.setPixmap(
            pixmap1.scaled(
            self.ui_list.label_logo1.width(),
            self.ui_list.label_logo1.height(),
            aspectRatioMode=False
            )
        )
        pixmap2 = QPixmap("Assets/logo2.png")
        self.ui_list.label_logo2.setPixmap(
            pixmap2.scaled(
            self.ui_list.label_logo2.width(),
            self.ui_list.label_logo2.height(),
            aspectRatioMode=False
            )
        )
    
    def mouse_over(self, event):
        self.ui_list.label_list.setFont(self.font_over)
    
    def mouse_out(self, event):
        self.ui_list.label_list.setFont(self.font_out)
        
    def set_table(self):
        
        self.table_reports = QTableWidget()
        self.area_table = QWidget()
        self.area_table_layout = QVBoxLayout()
        self.area_table.setLayout(self.area_table_layout)
        
        self.area_table_layout.addWidget(self.table_reports)
        
        
        self.ui_list.scrollArea.setWidgetResizable(True)
        self.ui_list.scrollArea.setWidget(self.area_table)
        
        self.table_reports.verticalHeader().setVisible(False)
        # defino las columnas de la tabla
        self.table_reports.setColumnCount(8)
        self.table_reports.setHorizontalHeaderLabels(
            [
                'ID',
                'Cedula',
                'Apellido',
                'Nombre',
                'Fecha de nacimiento',
                'Cedula Representante',
                'Nombre Representante',
                'Contacto'
                      
            ]
        )
        
        self.table_reports.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_reports.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        # hace que la ultima columna ocupe el espacio restante de la tabla
        self.table_reports.horizontalHeader().setStretchLastSection(True)
        
        # este codigo hace que las columnas  no sean redimensionables
        header = self.table_reports.horizontalHeader()
        
        for i in range(header.count()):
            header.setSectionResizeMode(i,QHeaderView.ResizeToContents)
            
        
    
    def load_table(self):
         # recuperar de la DB las sesiones del estudiante
        if self.student_list:
            # la lista contiene elementos
            # Agregar las filas a la tabla
            for i, est in enumerate(self.student_list):
                self.table_reports.insertRow(i)
                self.table_reports.setItem(i, 0, QTableWidgetItem(str(est.id)))
                self.table_reports.setItem(i, 1, QTableWidgetItem(str(est.cedula)))
                self.table_reports.setItem(i, 2, QTableWidgetItem(str(est.apellidos)))
                self.table_reports.setItem(i, 3, QTableWidgetItem(str(est.nombres)))
                self.table_reports.setItem(i, 4, QTableWidgetItem(est.fecha_nacimiento.strftime("%d/%m/%Y")))
                self.table_reports.setItem(i, 5, QTableWidgetItem(str(est.cedula_representante)))
                self.table_reports.setItem(i, 6, QTableWidgetItem(str(est.nombre_representante)))
                self.table_reports.setItem(i, 7, QTableWidgetItem(str(est.telefonos)))
                
               
        
    