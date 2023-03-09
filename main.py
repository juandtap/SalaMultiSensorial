
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from View.main_window_view import Ui_MainWindow
from View.add_student_view import Ui_Add_student
from Controller.student_control import add_student_control, get_student_list
from PyQt5.QtCore import QStringListModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        self.show_student_list()
        self.ui_main.pushButton_add_estudiante.clicked.connect(self.open_add_student)
        
    def open_add_student(self):
        self.add_stu_win = AddStudent()
        self.add_stu_win.show()
    
    def show_student_list(self):
        student_list = get_student_list()
        new_list = []
        for st in student_list:
            new_list.append(st.apellidos+' '+st.nombres+' '+st.cedula)
        # list_model = QStringListModel()
        # list_model.setStringList(new_list)
        self.ui_main.listWidget_estudiantes.addItems(new_list)
        # self.ui_main.listWidget_estudiantes.setModel(list_model)

class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_addstu = Ui_Add_student()
        self.ui_addstu.setupUi(self)
        self.ui_addstu.pushButton_cancel.clicked.connect(self.close)
        
        
    def add_student(self):
        flag = add_student_control()
        if flag:
            print('estudiante agregado')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())