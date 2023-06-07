
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_student_list(object):
    def setupUi(self, Form_student_list):
        Form_student_list.setObjectName("Form_student_list")
        Form_student_list.resize(1280, 720)
        Form_student_list.setMinimumSize(QtCore.QSize(1280, 720))
        Form_student_list.setMaximumSize(QtCore.QSize(1280, 720))
        Form_student_list.setBaseSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form_student_list.setFont(font)
        Form_student_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_logo2 = QtWidgets.QLabel(Form_student_list)
        self.label_logo2.setGeometry(QtCore.QRect(1120, 0, 130, 130))
        self.label_logo2.setText("")
        self.label_logo2.setObjectName("label_logo2")
        self.label = QtWidgets.QLabel(Form_student_list)
        self.label.setGeometry(QtCore.QRect(460, 40, 350, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(56, 71, 151);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_logo1 = QtWidgets.QLabel(Form_student_list)
        self.label_logo1.setGeometry(QtCore.QRect(0, 0, 280, 160))
        self.label_logo1.setText("")
        self.label_logo1.setObjectName("label_logo1")
        self.scrollArea = QtWidgets.QScrollArea(Form_student_list)
        self.scrollArea.setGeometry(QtCore.QRect(30, 186, 1221, 521))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1219, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_list = QtWidgets.QLabel(Form_student_list)
        self.label_list.setGeometry(QtCore.QRect(970, 160, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_list.setFont(font)
        self.label_list.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_list.setObjectName("label_list")

        self.retranslateUi(Form_student_list)
        QtCore.QMetaObject.connectSlotsByName(Form_student_list)

    def retranslateUi(self, Form_student_list):
        _translate = QtCore.QCoreApplication.translate
        Form_student_list.setWindowTitle(_translate("Form_student_list", "Lista de Estudiantes"))
        self.label.setText(_translate("Form_student_list", "Lista de Estudiantes"))
        self.label_list.setText(_translate("Form_student_list", "Descargar Lista de estudiantes"))
