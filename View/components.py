import sys
sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QFileDialog
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIntValidator
from View.message_dialog_view import Ui_Message_dialog
from View.add_discapacidad_view import Ui_Agregar_Discapacidades
from View.add_school_view import Ui_add_Unidad_Educativa
from Controller.school_control import add_school_control, get_all_schools
from Controller.discapacidad_control import add_discapacidad_control
from View.edit_student_view import Ui_Add_student
from Controller.student_control import update_student
from Controller.discapacidad_control import get_all_discapacidades

from datetime import date


class AddSchool(QWidget):
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
            else:
                self.new_message = MessageDialog("Unidad Educativa ya existe!")
                self.new_message.show()
                self.ui_add_school.lineEdit_name_unidad_educativa.clear()
        else:
            self.new_message = MessageDialog("Ingrese una Unidad Educativa!")
            self.new_message.show()
            self.ui_add_school.lineEdit_name_unidad_educativa.clear()
            

class AddDiscapacidad(QWidget):
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
        
        self.load_info_student()
    
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
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
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
        self.ui_list = None
        
    