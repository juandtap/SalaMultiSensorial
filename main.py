
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QCompleter, QFileDialog
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap, QIntValidator, QFont
from PyQt5.QtCore import Qt, QStandardPaths

from datetime import date

from View.main_window_view import Ui_MainWindow
from View.add_student_view import Ui_Add_student

from View.components import CheckableComboBox, MessageDialog, AddSchool, AddDiscapacidad, EditStudent, StudentList
from View.module_components import ModuleSelection
from View.components_2 import StudentReport
from Controller.student_control import add_student_control, get_all_students, get_student_by_id, get_student_by_cedula, get_student_by_names
from Controller.school_control import add_school_control, get_all_schools, get_school_by_id
from Controller.discapacidad_control import get_all_discapacidades, get_discapacidad_by_id


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        self.ui_main.scrollArea_info_estudiante.setHidden(True)
        # Fuente label 
        self.font_in = QFont('Arial',10,1,True)
        self.font_in.setBold(True)
        self.font_in.setUnderline(True)
        self.font_out = QFont('Arial',10,1,True)
        self.font_out.setBold(False)
        self.font_out.setUnderline(True)
        
        self.ui_main.label_list.setFont(self.font_out)
        
        self.set_logos()
        
        # revisa si hay un usuario de prueba, si no lo crea, el usuario de prueba es siempre el id=1
        self.check_guest_user()
        # campo de discapacidades del estudiante no son editables
        self.ui_main.textEdit_discapacidad_est.setReadOnly(True)
        
        self.ui_main.pushButton_add_estudiante.clicked.connect(self.open_add_student)
        # placeholder barra de busqueda
       
        self.ui_main.lineEdit_search_bar.setPlaceholderText("Buscar Estudiante (Apellidos o Nombres)")
        
        
        
        self.ui_main.listWidget_estudiantes.clicked.connect(self.show_info_student)
        
       
        self.ui_main.lineEdit_search_bar.textChanged.connect(self.search_students)
        
        # Editar estudiante
        
        self.ui_main.pushButton_edit_estudiante.clicked.connect(self.open_edit_student)
        
        # abrir ventana selccion de modulos
        
        self.ui_main.pushButton_goto_modules.clicked.connect(self.open_modules)
        
        # ventana reportes del estudiante
        
        self.ui_main.pushButton_goto_reports.clicked.connect(self.open_student_reports)
        
        # boton de selccion de usuario invitado
        self.ui_main.pushButton_reportes.clicked.connect(self.open_guest_user)
        
        # eventos para la label Ver lista de estudiantes
        self.ui_main.label_list.mousePressEvent = self.show_student_list
        self.ui_main.label_list.enterEvent = self.mouse_over
        self.ui_main.label_list.leaveEvent = self.mouse_out
        
        
    def open_add_student(self):
        self.add_stu = AddStudent()
        self.add_stu.show()
        
    def open_edit_student(self):
        self.edit_stu = EditStudent(get_student_by_cedula(self.ui_main.label_cedula.text()))
        self.edit_stu.show()
        
    def open_student_reports(self):
        self.stu_report = StudentReport(get_student_by_cedula(self.ui_main.label_cedula.text()))
        self.stu_report.show()
        
    def set_logos(self):
        pixmap1 = QPixmap("Assets/logo2.png")
        self.ui_main.label_logo1.setPixmap(
            pixmap1.scaled(
            self.ui_main.label_logo1.width(),
            self.ui_main.label_logo1.height(),
            aspectRatioMode=False
            )
        )
        pixmap2 = QPixmap("Assets/logo1.png")
        self.ui_main.label_logo2.setPixmap(
            pixmap2.scaled(
            self.ui_main.label_logo2.width(),
            self.ui_main.label_logo2.height(),
            aspectRatioMode=False
            )
        )
    
    # Eventos para la label para ver y descargar (PDF) la lista de todos los estudiantes registrados
    
   
    def show_student_list(self, event):
        self.list_window = StudentList()
        self.list_window.show()
        
    def mouse_over(self, event):
        self.ui_main.label_list.setFont(self.font_in)
    
    def mouse_out(self, event):
        self.ui_main.label_list.setFont(self.font_out)

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
        if student.nombre_representante != "":
            self.ui_main.label_representante.setText(student.nombre_representante)
        else: self.ui_main.label_representante.setText("Sin especificar")
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
            
        # mostrar imagen
        if student.fotografia is None:
            self.ui_main.label_imagen.setText("Sin imagen")
        else:
            pixmap = QPixmap()
            pixmap.loadFromData(student.fotografia)
            #self.ui_main.label_imagen.setPixmap(pixmap)
            self.ui_main.label_imagen.setPixmap(pixmap.scaled(
                self.ui_main.label_imagen.width(),
                self.ui_main.label_imagen.height(),
                aspectRatioMode=False
            ))
           
            
    def calculate_age(self, date):
        # Obtenemos la fecha actual
        current_date = date.today()
    
        # Calculamos la edad restando el año actual menos el año de nacimiento
        age = current_date.year - date.year
    
        # Si el cumpleaños de la persona aun no ha llegado en el anioo actual, se resta 1 a la edad
        if (current_date.month, current_date.day) < (date.month, date.day):
            age -= 1
        
        return age
    
    def search_students(self):
        if len(self.ui_main.lineEdit_search_bar.text()) >= 3:
            self.ui_main.listWidget_estudiantes.clear()
            self.ui_main.label_search_results.setText("")
            # busqueda 
            list_search = get_student_by_names(self.ui_main.lineEdit_search_bar.text().strip())
            if len(list_search) > 0:
                for st in list_search:
                    print(st.apellidos+" "+st.nombres+" "+st.cedula)
                    self.ui_main.listWidget_estudiantes.addItem(st.apellidos+" "+st.nombres+" - "+st.cedula)
            else:
                self.ui_main.label_search_results.setText("Sin resultados")
        else:
            self.ui_main.listWidget_estudiantes.clear()
            self.ui_main.scrollArea_info_estudiante.setHidden(True)
            
    
    
    def get_selected_cedula(self, selected_student):
        return selected_student.split('-')[-1].strip()
    
    
    def check_guest_user(self):
        guest = get_student_by_id(1)
        if guest is None:
            print("No existe usuario Invitado, creando ...")
            #crea el usuario invitado siempre que la DB sea reiniciada
            guest_estudent = [
                "000000000",
                "ESTUDIANTE",
                "INVITADO",
                "000000001",
                "ESTUDIANTE DE PRUEBA",
                date(2015,1,1),
                "",
                "",
                False,
                None,
                0,
                [],
                
            ]
            if add_student_control(guest_estudent):
                print("USUARIO INVITADO CREADO!")
        else:
            print("Usuario invitado encontrado")
    
    def open_guest_user(self):
        # el usario invitado es el que tiene el id=1
        
        guest = get_student_by_id(1)
        
        self.load_info_student(guest)
        self.ui_main.scrollArea_info_estudiante.setHidden(False)
        
            
    
    def open_modules(self):
        self.modules = ModuleSelection(get_student_by_cedula(self.ui_main.label_cedula.text()))
        self.modules.show()
        
class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_addstu = Ui_Add_student()
        self.ui_addstu.setupUi(self)
        self.load_schools()
        self.filename = None
        self.ui_addstu.pushButton_cancel.clicked.connect(self.close)
        self.ui_addstu.pushButton_add_unidad_educativa.clicked.connect(self.open_add_school)
        
        
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
        
        # oculta la lista de combobox y el boton de agregar discapacidad 
        # si el checkbox tiene discapacidad no esta marcado
        
        self.checkeable_combo.setHidden(True)
        self.ui_addstu.pushButton_add_discapacidad.setHidden(True)
        
        self.ui_addstu.checkBox_discapacidad.clicked.connect(self.show_combo_discapacidades)
        
        
        # revisa que el campo cedula no exeda los 10 caracteres y solo se ingrese numeros
        validator = QIntValidator(self)
        validator.setRange(0,999999999)
        self.ui_addstu.lineEdit_cedula.setValidator(validator)
        self.ui_addstu.lineEdit_cedula_representante.setValidator(validator)
        self.ui_addstu.lineEdit_cedula.textChanged.connect(self.check_cedula_fields)
        self.ui_addstu.lineEdit_cedula_representante.textChanged.connect(self.check_cedula_representate_fields)
        # cargar fotografia del estudiante
        self.ui_addstu.pushButton_load_picture.clicked.connect(self.load_image)
        
        # guardar estudiante
        self.ui_addstu.pushButton_save.clicked.connect(self.add_student)
        
    def reload_combo_schools(self, flag):
        if flag:
            self.load_schools()
            print("combo unidades educativas recargado")
            
    def reload_combo_discapacidades(self, flag):
        if flag:
            self.load_discapacidades()
            print("combo discapacidades recargado")
    
    
    
    def open_add_school(self):
        self.add_shool = AddSchool()
        self.add_shool.reload_flag.connect(self.reload_combo_schools)
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
        
        
    def show_combo_discapacidades(self):
        if self.ui_addstu.checkBox_discapacidad.isChecked():
            self.checkeable_combo.setHidden(False)
            self.ui_addstu.pushButton_add_discapacidad.setHidden(False)
        else:
            self.checkeable_combo.setHidden(True)
            self.ui_addstu.pushButton_add_discapacidad.setHidden(True)
            
    
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
        self.add_discapacidad.reload_flag.connect(self.reload_combo_discapacidades)
        self.add_discapacidad.show()
        
    def load_image(self):
        folder_path = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        file_dialog = QFileDialog()
        file_dialog.setDirectory(folder_path)
        self.filename = file_dialog.getOpenFileName(filter="Image (*.*)")[0]
        print(self.filename)
        self.ui_addstu.label_file_name.setText(self.filename)
       
    # verifica que el campo cedula no exeda los 10 caracteres
    def check_cedula_fields(self, text_cedula):
        if len(text_cedula) > 10:
            self.ui_addstu.lineEdit_cedula.setText(text_cedula[:10])
            self.ui_addstu.lineEdit_cedula.setCursorPosition(10)
    
    def check_cedula_representate_fields(self, text_cedula):
        if len(text_cedula) > 10:
            self.ui_addstu.lineEdit_cedula_representante.setText(text_cedula[:10])
            self.ui_addstu.lineEdit_cedula_representante.setCursorPosition(10)
    
    
    def add_student(self):
        # para agregar un estudiante como minimo se debe de llenar los campos
        # cedula, apellido y nombre
        
        if self.ui_addstu.lineEdit_cedula.text() != "" and self.ui_addstu.lineEdit_apellido.text() != "" and self.ui_addstu.lineEdit_nombre.text() != "" :
            
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
                    self.filename, # enviar  path imagen (str)
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
        else:
            self.student_message = MessageDialog("!Ingrese los datos")
            self.student_message.show()
            self.clear_student_fields()
            print("Ingresar datos del estudante!")
    
    def clear_student_fields(self):
        self.ui_addstu.lineEdit_cedula.clear()
        self.ui_addstu.lineEdit_apellido.clear()
        self.ui_addstu.lineEdit_nombre.clear()
        self.ui_addstu.lineEdit_cedula_representante.clear()
        self.ui_addstu.lineEdit_representante.clear()
        self.ui_addstu.lineEdit_direccion_est.clear()
        self.ui_addstu.lineEdit_telefono.clear()
        self.ui_addstu.checkBox_discapacidad.setChecked(False)
        self.ui_addstu.label_file_name.clear()
        
                  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())