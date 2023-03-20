
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QCompleter, QFileDialog
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
import cv2, imutils
from datetime import date

from View.main_window_view import Ui_MainWindow
from View.add_student_view import Ui_Add_student

from View.components import CheckableComboBox, MessageDialog, AddSchool, AddDiscapacidad

from Controller.student_control import add_student_control, get_all_students, get_student_by_id, get_student_by_cedula, get_student_by_names
from Controller.school_control import add_school_control, get_all_schools, get_school_by_id
from Controller.discapacidad_control import get_all_discapacidades, get_discapacidad_by_id


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        self.ui_main.scrollArea_info_estudiante.setHidden(True)
       
        self.ui_main.pushButton_add_estudiante.clicked.connect(self.open_add_student)
        # placeholder barra de busqueda
       
        self.ui_main.lineEdit_search_bar.setPlaceholderText("Buscar Estudiante (Apellidos o Nombres)")
        
        
        
        self.ui_main.listWidget_estudiantes.clicked.connect(self.show_info_student)
        
        # barra de busqueda sin el Qcompleter
        self.ui_main.lineEdit_search_bar.textChanged.connect(self.search_students)
        # Mostrar mensaje cuando no hay resultados de la busqueda
        #self.ui_main.label_search_results.setText("Sin resultados")
        
        
    def open_add_student(self):
        self.add_stu = AddStudent()
        self.add_stu.show()
        
    
    def show_student_list(self):
        student_list = get_all_students()
        new_list = []
        if student_list is not None:
            for st in student_list:
                new_list.append(st.apellidos+' '+st.nombres+' - '+st.cedula)
        
        self.ui_main.listWidget_estudiantes.addItems(new_list)
        return new_list
        # self.ui_main.listWidget_estudiantes.setModel(list_model)

    def show_info_student(self):
        selected_student = self.ui_main.listWidget_estudiantes.selectedItems()[0].text()
        print('texto de lista seleccionada')
        print(selected_student)
        print('cedula recortada')
        print(self.get_selected_cedula(selected_student))
        if selected_student is not None:
            self.ui_main.scrollArea_info_estudiante.setHidden(False)
            # Cargar Datos de estudiante desde la base de datos:
            sel_student = get_student_by_cedula(self.get_selected_cedula(selected_student))
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
        
        if student.id_unidad_educativa != 0:
            self.ui_main.label_unidad_educativa.setText(get_school_by_id(student.id_unidad_educativa).nombre)
        else:
            self.ui_main.label_unidad_educativa.setText("Sin especificar")
            
        self.ui_main.textEdit_discapacidad_est.clear()
        if len(student.discapacidades) != 0:
            for i in range(len(student.discapacidades)):
                self.ui_main.textEdit_discapacidad_est.append(student.discapacidades[i].nombre_discapacidad)
        else:
            self.ui_main.textEdit_discapacidad_est.append("Sin especificar")
            
    def calculate_age(self, date):
        # Obtenemos la fecha actual
        current_date = date.today()
    
        # Calculamos la edad restando el año actual menos el año de nacimiento
        age = current_date.year - date.year
    
        # Si el cumpleaños de la persona aún no ha llegado en el año actual, restamos 1 a la edad
        if (current_date.month, current_date.day) < (date.month, date.day):
            age -= 1
        
        return age
    
    def search_students(self):
        if len(self.ui_main.lineEdit_search_bar.text()) >= 3:
            self.ui_main.listWidget_estudiantes.clear()
            # busqueda 
            list_search = get_student_by_names(self.ui_main.lineEdit_search_bar.text().strip())
            if len(list_search) > 0:
                for st in list_search:
                    print(st.apellidos+" "+st.nombres+" "+st.cedula)
                    self.ui_main.listWidget_estudiantes.addItem(st.apellidos+" "+st.nombres+" - "+st.cedula)
            else:
                self.ui_main.label_search_results.setText("Sin resultados")
    
    
    def get_selected_cedula(self, selected_student):
        return selected_student.split('-')[-1].strip()
        
        
        
        
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
        
        self.ui_addstu.pushButton_add_discapacidad.clicked.connect(self.open_add_discapacidad)
        
        # cargar fotografia del estudiante
        self.ui_addstu.pushButton_load_picture.clicked.connect(self.load_image)
        
        # guardar estudiante
        self.ui_addstu.pushButton_save.clicked.connect(self.add_student)
        
    def on_focus_change(self):
       
        if not self.isActiveWindow():
            self.reload_flag = True
    
        if self.isActiveWindow() and self.reload_flag:
            self.load_schools()
            self.load_discapacidades()
            print("combos recargados")
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
        discapacidades_list = get_all_discapacidades()
        # primera opcion : Sin especificar
        self.checkeable_combo.addItem("Sin especificar")
        self.checkeable_combo.setItemChecked(0, False)
        for i in range(len(discapacidades_list)):
            self.checkeable_combo.addItem(discapacidades_list[i].nombre_discapacidad)
            self.checkeable_combo.setItemChecked(i+1, False)
    
    # agrega las discapacidades seleccionadas a un QlistWidget
    def get_selected_discapacidades(self):
        self.ui_addstu.listDiscapacidades.clear()
        for i in range(self.checkeable_combo.count()):
            print('Index: {0} is checked {1}'.format(i, self.checkeable_combo.itemChecked(i)))
            if self.checkeable_combo.itemChecked(i):
                self.ui_addstu.listDiscapacidades.addItem(self.checkeable_combo.itemText(i))

    # retorna una lista de discapacidaes del QlistWidget
    def get_student_discapacidades(self):
        
        student_discapacidades = []
        for i in range(self.ui_addstu.listDiscapacidades.count()):
            student_discapacidades.append(self.ui_addstu.listDiscapacidades.item(i).text())
        print("Discapacidade seleccionadas: ")
        print(student_discapacidades)
        return student_discapacidades
    
    def open_add_discapacidad(self):
        self.add_discapacidad = AddDiscapacidad()
        self.add_discapacidad.show()
        
    def load_image(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        print(self.filename)
        self.ui_addstu.label_file_name.setText(self.filename)
        
    
    def add_student(self):
        # pendiente validacion
        
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
                None, # enviar imagen
                self.ui_addstu.comboBox_unidad_educativa.currentIndex(),
                self.get_student_discapacidades()
                
                
            ]
        )
        if flag:
            self.student_message = MessageDialog("Estudiante Agregado/a!")
            self.student_message.show()
            self.clear_student_fields()
            print('estudiante agregado')
        else:
            self.student_message = MessageDialog("Estudiante ya existe!")
            self.student_message.show()
            self.clear_student_fields()
            print("Estudiante ya existe!")
    
    def clear_student_fields(self):
        self.ui_addstu.lineEdit_cedula.clear()
        self.ui_addstu.lineEdit_apellido.clear()
        self.ui_addstu.lineEdit_nombre.clear()
        self.ui_addstu.lineEdit_cedula_representante.clear()
        self.ui_addstu.lineEdit_representante.clear()
        self.ui_addstu.lineEdit_direccion_est.clear()
        self.ui_addstu.lineEdit_telefono.clear()
        self.ui_addstu.checkBox_discapacidad.setChecked(False)
                  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())