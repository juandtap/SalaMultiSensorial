import sys
sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox
from PyQt5.QtCore import Qt, QDate
from View.message_dialog_view import Ui_Message_dialog
from View.add_discapacidad_view import Ui_Agregar_Discapacidades
from View.add_school_view import Ui_add_Unidad_Educativa
from Controller.school_control import add_school_control, get_all_schools
from Controller.discapacidad_control import add_discapacidad_control
from View.edit_student_view import Ui_Add_student

class AddSchool(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_add_school = Ui_add_Unidad_Educativa()
        self.ui_add_school.setupUi(self)
        self.ui_add_school.pushButton_cancel.clicked.connect(self.close)
        self.ui_add_school.pushButton_save.clicked.connect(self.add_school)
    
    def add_school(self):
        flag = False
        
        flag = add_school_control(self.ui_add_school.lineEdit_name_unidad_educativa.text())
        
        if flag:
            self.new_message = MessageDialog("Unidad Educativa Agregada!")
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
        flag = False
       
        flag = add_discapacidad_control(self.ui_add_dis.line_discapacidad.text())
        if flag:
            self.new_message = MessageDialog("Discapacidad Agregada!")
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
        self.ui_edit.lineEdit_cedula.setText(self.student.cedula)
        self.ui_edit.lineEdit_cedula.setEnabled(False)
        self.load_schools()
        self.load_info_student()
        
        self.ui_edit.pushButton_cancel.clicked.connect(self.close)
    
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
        