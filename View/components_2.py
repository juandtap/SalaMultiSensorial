import sys
sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QFileDialog
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIntValidator
from datetime import time, date

from View.student_report_view import Ui_Form_student_report

class StudentReport(QWidget):
    def __init__(self, student):
        super().__init__()
        self.ui_rep = Ui_Form_student_report()
        self.ui_rep.setupUi(self)
        self.student = student
        

