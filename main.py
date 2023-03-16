
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

from datetime import date

from View.main_window_view import Ui_MainWindow
from View.add_student_view import Ui_Add_student
from View.add_school_view import Ui_add_Unidad_Educativa
from View.message_dialog_view import Ui_Message_dialog

from Controller.student_control import add_student_control, get_student_list, get_student_by_id
from Controller.school_control import add_school_control, get_all_schools, get_school_by_id

from PyQt5.QtCore import QStringListModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        self.ui_main.scrollArea_info_estudiante.setHidden(True)
        
        self.ui_main.pushButton_add_estudiante.clicked.connect(self.open_add_student)
        # placeholder barra de busqueda
        self.ui_main.textEdit_search_bar.setText("")
        self.ui_main.textEdit_search_bar.setPlaceholderText("Buscar Estudiante (nombre o cedula)")
        
        # metodo temporal, se implementara barra de busqueda
        self.show_student_list()
        self.ui_main.listWidget_estudiantes.clicked.connect(self.show_info_student)
        
        
    def open_add_student(self):
        self.add_stu = AddStudent()
        self.add_stu.show()
        
    
    def show_student_list(self):
        student_list = get_student_list()
        new_list = []
        if student_list is not None:
            for st in student_list:
                new_list.append(st.apellidos+' '+st.nombres+' '+st.cedula)
        #list_model = QStringListModel()
        #list_model.setStringList(new_list)
        self.ui_main.listWidget_estudiantes.addItems(new_list)
        # self.ui_main.listWidget_estudiantes.setModel(list_model)

    def show_info_student(self):
        selected_student_id = self.ui_main.listWidget_estudiantes.currentIndex().row()+1
        if selected_student_id > 0:
            self.ui_main.scrollArea_info_estudiante.setHidden(False)
            print("Lista: "+str(selected_student_id))
            # Cargar Datos de estudiante desde la base de datos:
            sel_student = get_student_by_id(selected_student_id)
            print(sel_student.nombres + " "+ sel_student.apellidos)
            self.load_info_student(sel_student)
        else:
            self.ui_main.scrollArea_info_estudiante.setHidden(True)
    
    def load_info_student(self, student):
        self.ui_main.label_cedula.setText(student.cedula)
        self.ui_main.label_apellido.setText(student.apellidos)
        self.ui_main.label_nombre.setText(student.nombres)
        self.ui_main.label_cedula_representante.setText(student.cedula_representante)
        self.ui_main.label_representante.setText(student.nombre_representante)
        self.ui_main.label_direccion.setText(student.direccion)
        self.ui_main.label_telefonos.setText(student.telefonos)
        self.ui_main.label_fecha_nac.setText(
            str(student.fecha_nacimiento.day)+"/"+
            str(student.fecha_nacimiento.month)+"/"+
            str(student.fecha_nacimiento.year)   
                
        )
        self.ui_main.label_edad.setText(str(self.calculate_age(student.fecha_nacimiento)))
        
        self.ui_main.label_unidad_educativa.setText(get_school_by_id(student.id_unidad_educativa).nombre)
        
    def calculate_age(self, date):
        # Obtenemos la fecha actual
        current_date = date.today()
    
        # Calculamos la edad restando el año actual menos el año de nacimiento
        age = current_date.year - date.year
    
        # Si el cumpleaños de la persona aún no ha llegado en el año actual, restamos 1 a la edad
        if (current_date.month, current_date.day) < (date.month, date.day):
            age -= 1
        
        return age
    
class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_addstu = Ui_Add_student()
        self.ui_addstu.setupUi(self)
        self.load_schools()
        self.ui_addstu.pushButton_cancel.clicked.connect(self.close)
        self.ui_addstu.pushButton_add_unidad_educativa.clicked.connect(self.open_add_school)
        self.setFocus()
        # flags para recargar datos de los ComboBox
        self.reload_flag = False
        app.focusChanged.connect(self.on_focus_change)
        
        # placeholder Telefono
        self.ui_addstu.lineEdit_telefono.setPlaceholderText("numero 1, numero 2, ...")
        # calendar picker
        self.ui_addstu.dateEdit_estudiante.setCalendarPopup(True)
        self.ui_addstu.dateEdit_estudiante.setStyleSheet("background-color : rgb(200, 200, 200);")

        # ComboBox Opcion Multiple
        self.checkeable_combo = CheckableComboBox()
        self.ui_addstu.gridLayout_2.addWidget(self.checkeable_combo, 1,1,1,1)
        
        # eventos ComboBox Discapacidades
        self.checkeable_combo.activated.connect(self.get_selected_discapacidades)
        
        self.load_discapacidades()
        
        # guardar estudiante
        self.ui_addstu.pushButton_save.clicked.connect(self.add_student)
        
    def on_focus_change(self):
       
        if not self.isActiveWindow():
            self.reload_flag = True
    
        if self.isActiveWindow() and self.reload_flag:
            self.load_schools()
            print("recargo combo")
            self.reload_flag = False
    
    def open_add_school(self):
        self.add_shool = AddSchool()
        self.add_shool.show()
        
    def load_schools(self):
        self.ui_addstu.comboBox_unidad_educativa.clear()
        self.ui_addstu.comboBox_unidad_educativa.addItem("Sin especificar")
        # obtengo todos los objetos de tipo Unidad_educativa
        school_list = get_all_schools()
        # separo los nombres en otra lista
        self.school_names = []
        for sc in school_list:
            self.school_names.append(sc.nombre)
        self.ui_addstu.comboBox_unidad_educativa.addItems(self.school_names)
    
    # Combo Box con checkitems
    def load_discapacidades(self):
        # cargar desde la base de datos 
        self.checkeable_combo.clear()
        
        for i in range(4):
            if i == 0:
                self.checkeable_combo.addItem("Sin especificar")
                self.checkeable_combo.setItemChecked(i, False)
            else:
                self.checkeable_combo.addItem("Discapacidad {0}".format(str(i)))
                self.checkeable_combo.setItemChecked(i, False)
    
    def get_selected_discapacidades(self):
        self.ui_addstu.listDiscapacidades.clear()
        for i in range(self.checkeable_combo.count()):
            print('Index: {0} is checked {1}'.format(i, self.checkeable_combo.itemChecked(i)))
            if self.checkeable_combo.itemChecked(i):
                self.ui_addstu.listDiscapacidades.addItem(self.checkeable_combo.itemText(i))

    
    def add_student(self):
        # pendiente datos y validacion
        
        flag = add_student_control(
            student_data=[
                self.ui_addstu.lineEdit_cedula.text(),
                self.ui_addstu.lineEdit_apellido.text(),
                self.ui_addstu.lineEdit_nombre.text(),
                self.ui_addstu.lineEdit_cedula_representante.text(),
                self.ui_addstu.lineEdit_representante.text(),
                date(
                    self.ui_addstu.dateEdit_estudiante.date().year(), 
                    self.ui_addstu.dateEdit_estudiante.date().month(),
                    self.ui_addstu.dateEdit_estudiante.date().day()
                ),
                self.ui_addstu.lineEdit_direccion_est.text(),
                self.ui_addstu.lineEdit_telefono.text(),
                self.ui_addstu.checkBox_discapacidad.isChecked(),
                None,
                self.ui_addstu.comboBox_unidad_educativa.currentIndex()
                
            ]
        )
        if flag:
            self.student_message = MessageDialog("Estudiante Agregado/a!")
            self.student_message.show()
            self.clear_student_fields()
            print('estudiante agregado')
    
    def clear_student_fields(self):
        self.ui_addstu.lineEdit_cedula.clear()
        self.ui_addstu.lineEdit_apellido.clear()
        self.ui_addstu.lineEdit_nombre.clear()
        self.ui_addstu.lineEdit_cedula_representante.clear()
        self.ui_addstu.lineEdit_representante.clear()
        self.ui_addstu.lineEdit_direccion_est.clear()
        self.ui_addstu.lineEdit_telefono.clear()
        self.ui_addstu.checkBox_discapacidad.setChecked(False)
        
        
        
        
         
        
    
     
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

   
   
class MessageDialog(QWidget):
    def __init__(self, message):
        super().__init__()
        self.ui_message = Ui_Message_dialog()
        self.ui_message.setupUi(self)
        self.message = message
        self.ui_message.label_message.setText(self.message)
        self.ui_message.pushButton_accept_dialog.clicked.connect(self.close)
    
    
        
    
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())