# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\form_reportes_estudiante.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_student_report(object):
    def setupUi(self, Form_student_report):
        Form_student_report.setObjectName("Form_student_report")
        Form_student_report.resize(1280, 720)
        Form_student_report.setMinimumSize(QtCore.QSize(1280, 720))
        Form_student_report.setMaximumSize(QtCore.QSize(1280, 720))
        Form_student_report.setBaseSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form_student_report.setFont(font)
        Form_student_report.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_logo2 = QtWidgets.QLabel(Form_student_report)
        self.label_logo2.setGeometry(QtCore.QRect(1120, 0, 161, 131))
        self.label_logo2.setText("")
        self.label_logo2.setObjectName("label_logo2")
        self.label = QtWidgets.QLabel(Form_student_report)
        self.label.setGeometry(QtCore.QRect(470, 10, 350, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(56, 71, 151);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_logo1 = QtWidgets.QLabel(Form_student_report)
        self.label_logo1.setGeometry(QtCore.QRect(0, 0, 161, 131))
        self.label_logo1.setText("")
        self.label_logo1.setObjectName("label_logo1")
        self.label_8 = QtWidgets.QLabel(Form_student_report)
        self.label_8.setGeometry(QtCore.QRect(540, 90, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_8.setObjectName("label_8")
        self.formLayoutWidget = QtWidgets.QWidget(Form_student_report)
        self.formLayoutWidget.setGeometry(QtCore.QRect(400, 130, 491, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_apellidos = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_apellidos.setFont(font)
        self.label_apellidos.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_apellidos.setObjectName("label_apellidos")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_apellidos)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"color: rgb(56, 71, 151);")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_nombres = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_nombres.setFont(font)
        self.label_nombres.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_nombres.setObjectName("label_nombres")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_nombres)
        self.label_cedula = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_cedula.setFont(font)
        self.label_cedula.setStyleSheet("\n"
"color: rgb(56, 71, 151);")
        self.label_cedula.setObjectName("label_cedula")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_cedula)
        self.tableWidget = QtWidgets.QTableWidget(Form_student_report)
        self.tableWidget.setGeometry(QtCore.QRect(60, 260, 1161, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form_student_report)
        QtCore.QMetaObject.connectSlotsByName(Form_student_report)

    def retranslateUi(self, Form_student_report):
        _translate = QtCore.QCoreApplication.translate
        Form_student_report.setWindowTitle(_translate("Form_student_report", "Reportes Estudiante"))
        self.label.setText(_translate("Form_student_report", "REPORTES"))
        self.label_8.setText(_translate("Form_student_report", "INFORMACION ESTUDIANTE"))
        self.label_3.setText(_translate("Form_student_report", "CEDULA:"))
        self.label_4.setText(_translate("Form_student_report", "APELLIDOS:"))
        self.label_apellidos.setText(_translate("Form_student_report", "TextLabel"))
        self.label_6.setText(_translate("Form_student_report", "NOMBRES:"))
        self.label_nombres.setText(_translate("Form_student_report", "TextLabel"))
        self.label_cedula.setText(_translate("Form_student_report", "TextLabel"))