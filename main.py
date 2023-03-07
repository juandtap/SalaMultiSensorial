
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from View.main_window import Ui_MainWindow
from View.add_student_window import Ui_add_student
from Controller.student_control import add_student_control, get_student_list
from PyQt5.QtCore import QStringListModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        self.show_student_list()
        self.ui_main.pushButton.clicked.connect(self.open_add_student)
        
    def open_add_student(self):
        self.add_stu_win = AddStudent()
        self.add_stu_win.show()
    
    def show_student_list(self):
        student_list = get_student_list()
        new_list = []
        for st in student_list:
            new_list.append(st.apellidos+' '+st.nombres+' '+st.cedula)
        list_model = QStringListModel()
        list_model.setStringList(new_list)
        self.ui_main.listView.setModel(list_model)

class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_addstu = Ui_add_student()
        self.ui_addstu.setupUi(self)
        self.ui_addstu.pushButton_2.clicked.connect(self.close)
        self.ui_addstu.pushButton.clicked.connect(self.add_student)
        
    def add_student(self):
        flag = add_student_control(self.ui_addstu.lineEdit.text(), self.ui_addstu.lineEdit_2.text(), self.ui_addstu.lineEdit_3.text())
        if flag:
            print('estudiante agregado')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())