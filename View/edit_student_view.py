# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\form_agregar_estudiante_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_student(object):
    def setupUi(self, Add_student):
        Add_student.setObjectName("Add_student")
        Add_student.resize(1280, 720)
        Add_student.setMinimumSize(QtCore.QSize(1280, 720))
        Add_student.setMaximumSize(QtCore.QSize(1280, 720))
        Add_student.setBaseSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Add_student.setFont(font)
        Add_student.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Add_student)
        self.label.setGeometry(QtCore.QRect(510, 40, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(56, 71, 151);")
        self.label.setObjectName("label")
        self.pushButton_save = QtWidgets.QPushButton(Add_student)
        self.pushButton_save.setGeometry(QtCore.QRect(520, 630, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}")
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_cancel = QtWidgets.QPushButton(Add_student)
        self.pushButton_cancel.setGeometry(QtCore.QRect(660, 630, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayoutWidget = QtWidgets.QWidget(Add_student)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 160, 591, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.lineEdit_cedula = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_cedula.setFont(font)
        self.lineEdit_cedula.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.lineEdit_cedula.setObjectName("lineEdit_cedula")
        self.gridLayout.addWidget(self.lineEdit_cedula, 1, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.dateEdit_estudiante = QtWidgets.QDateEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.dateEdit_estudiante.setFont(font)
        self.dateEdit_estudiante.setMinimumDate(QtCore.QDate(2010, 1, 1))
        self.dateEdit_estudiante.setObjectName("dateEdit_estudiante")
        self.gridLayout.addWidget(self.dateEdit_estudiante, 6, 1, 1, 2)
        self.lineEdit_cedula_representante = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_cedula_representante.setFont(font)
        self.lineEdit_cedula_representante.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.lineEdit_cedula_representante.setObjectName("lineEdit_cedula_representante")
        self.gridLayout.addWidget(self.lineEdit_cedula_representante, 4, 1, 1, 2)
        self.lineEdit_representante = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_representante.setFont(font)
        self.lineEdit_representante.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.lineEdit_representante.setObjectName("lineEdit_representante")
        self.gridLayout.addWidget(self.lineEdit_representante, 5, 1, 1, 2)
        self.lineEdit_telefono = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_telefono.setFont(font)
        self.lineEdit_telefono.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.lineEdit_telefono.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.lineEdit_telefono.setPlaceholderText("")
        self.lineEdit_telefono.setObjectName("lineEdit_telefono")
        self.gridLayout.addWidget(self.lineEdit_telefono, 9, 1, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 11, 1, 1, 1)
        self.lineEdit_direccion_est = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_direccion_est.setFont(font)
        self.lineEdit_direccion_est.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.lineEdit_direccion_est.setObjectName("lineEdit_direccion_est")
        self.gridLayout.addWidget(self.lineEdit_direccion_est, 8, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_nombre = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_nombre.setFont(font)
        self.lineEdit_nombre.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.gridLayout.addWidget(self.lineEdit_nombre, 3, 1, 1, 2)
        self.lineEdit_apellido = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_apellido.setFont(font)
        self.lineEdit_apellido.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.gridLayout.addWidget(self.lineEdit_apellido, 2, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.label_file_name = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_file_name.setFont(font)
        self.label_file_name.setObjectName("label_file_name")
        self.gridLayout.addWidget(self.label_file_name, 10, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.pushButton_load_picture = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_load_picture.setMinimumSize(QtCore.QSize(96, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_load_picture.setFont(font)
        self.pushButton_load_picture.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}")
        self.pushButton_load_picture.setObjectName("pushButton_load_picture")
        self.gridLayout.addWidget(self.pushButton_load_picture, 10, 2, 1, 1)
        self.comboBox_unidad_educativa = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_unidad_educativa.setFont(font)
        self.comboBox_unidad_educativa.setObjectName("comboBox_unidad_educativa")
        self.comboBox_unidad_educativa.addItem("")
        self.gridLayout.addWidget(self.comboBox_unidad_educativa, 7, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_add_unidad_educativa = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_add_unidad_educativa.setMinimumSize(QtCore.QSize(50, 28))
        self.pushButton_add_unidad_educativa.setMaximumSize(QtCore.QSize(50, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_add_unidad_educativa.setFont(font)
        self.pushButton_add_unidad_educativa.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}")
        self.pushButton_add_unidad_educativa.setObjectName("pushButton_add_unidad_educativa")
        self.gridLayout.addWidget(self.pushButton_add_unidad_educativa, 7, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Add_student)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(630, 160, 631, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_discapacidad = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkBox_discapacidad.setFont(font)
        self.checkBox_discapacidad.setObjectName("checkBox_discapacidad")
        self.gridLayout_2.addWidget(self.checkBox_discapacidad, 0, 1, 1, 1)
        # self.comboBox_discapacidades = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        # font = QtGui.QFont()
        # font.setFamily("Arial")
        # font.setPointSize(9)
        # self.comboBox_discapacidades.setFont(font)
        # self.comboBox_discapacidades.setObjectName("comboBox_discapacidades")
        # self.comboBox_discapacidades.addItem("")
        # self.gridLayout_2.addWidget(self.comboBox_discapacidades, 1, 1, 1, 1)
        self.pushButton_add_discapacidad = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_add_discapacidad.setMinimumSize(QtCore.QSize(50, 28))
        self.pushButton_add_discapacidad.setMaximumSize(QtCore.QSize(50, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_add_discapacidad.setFont(font)
        self.pushButton_add_discapacidad.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}")
        self.pushButton_add_discapacidad.setObjectName("pushButton_add_discapacidad")
        self.gridLayout_2.addWidget(self.pushButton_add_discapacidad, 1, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.listDiscapacidades = QtWidgets.QListWidget(Add_student)
        self.listDiscapacidades.setGeometry(QtCore.QRect(630, 260, 581, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.listDiscapacidades.setFont(font)
        self.listDiscapacidades.setObjectName("listDiscapacidades")

        self.retranslateUi(Add_student)
        QtCore.QMetaObject.connectSlotsByName(Add_student)

    def retranslateUi(self, Add_student):
        _translate = QtCore.QCoreApplication.translate
        Add_student.setWindowTitle(_translate("Add_student", "Editar Estudiante"))
        self.label.setText(_translate("Add_student", "Editar Estudiante"))
        self.pushButton_save.setText(_translate("Add_student", "Guardar"))
        self.pushButton_cancel.setText(_translate("Add_student", "Cancelar"))
        self.label_7.setText(_translate("Add_student", "Fecha Nacimiento*:"))
        self.label_8.setText(_translate("Add_student", "Unidad Educativa*:"))
        self.label_14.setText(_translate("Add_student", "Tamaño imagen 30x40cm (carnet)"))
        self.label_3.setText(_translate("Add_student", "Apellidos*:"))
        self.label_9.setText(_translate("Add_student", "Direccion*:"))
        self.label_6.setText(_translate("Add_student", "Nombre representante*:"))
        self.label_4.setText(_translate("Add_student", "Nombres*:"))
        self.label_10.setText(_translate("Add_student", "Telefono/celular*:"))
        self.label_file_name.setText(_translate("Add_student", "imagen cargada: nombrearchivo.png"))
        self.label_11.setText(_translate("Add_student", "Fotografia:"))
        self.label_5.setText(_translate("Add_student", "Cedula representante*:"))
        self.pushButton_load_picture.setText(_translate("Add_student", "Cargar"))
        self.comboBox_unidad_educativa.setItemText(0, _translate("Add_student", "Sin especificar"))
        self.label_2.setText(_translate("Add_student", "Cedula* :"))
        self.pushButton_add_unidad_educativa.setText(_translate("Add_student", "+"))
        self.checkBox_discapacidad.setText(_translate("Add_student", "Si"))
        #self.comboBox_discapacidades.setItemText(0, _translate("Add_student", "Sin especificar"))
        self.pushButton_add_discapacidad.setText(_translate("Add_student", "+"))
        self.label_15.setText(_translate("Add_student", "Discapacidad:"))
        self.label_13.setText(_translate("Add_student", "Asociado a una discapacidad:"))
