
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtGui, QtCore

from View.main_window_view import Ui_MainWindow
from View.add_student_view import Ui_Add_student
from View.add_school_view import Ui_add_Unidad_Educativa
from View.message_dialog_view import Ui_Message_dialog

from Controller.student_control import add_student_control, get_student_list
from Controller.school_control import add_school_control, get_all_schools

from PyQt5.QtCore import QStringListModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        # self.show_student_list()
        self.show_info_student(False)
        self.ui_main.pushButton_add_estudiante.clicked.connect(self.open_add_student)
        
        
    def open_add_student(self):
        self.add_stu = AddStudent()
        self.add_stu.show()
        
    
    def show_student_list(self):
        student_list = get_student_list()
        new_list = []
        #for st in student_list:
        #    new_list.append(st.apellidos+' '+st.nombres+' '+st.cedula)
        #list_model = QStringListModel()
        #list_model.setStringList(new_list)
        self.ui_main.listWidget_estudiantes.addItems(new_list)
        # self.ui_main.listWidget_estudiantes.setModel(list_model)

    def show_info_student(self, value):
        self.ui_main.scrollArea_info_estudiante.setHidden(value)
        
    
class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_addstu = Ui_Add_student()
        self.ui_addstu.setupUi(self)
        self.load_schools()
        self.ui_addstu.pushButton_cancel.clicked.connect(self.close)
        self.ui_addstu.pushButton_add_unidad_educativa.clicked.connect(self.open_add_school)
    
    
    
    def open_add_school(self):
        self.add_shool = AddSchool()
        self.add_shool.show()
        
    def add_student(self):
        # pendiente
        flag = add_student_control()
        if flag:
            print('estudiante agregado')
            
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