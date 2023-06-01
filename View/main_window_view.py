# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setBaseSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_add_estudiante = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_estudiante.setGeometry(QtCore.QRect(480, 120, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_add_estudiante.setFont(font)
        self.pushButton_add_estudiante.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"\n"
"\n"
"")     
        #labels para los logos
        self.label_logo1 = QtWidgets.QLabel(self.centralwidget)
        self.label_logo1.setGeometry(QtCore.QRect(0,0,110,110))
        self.label_logo1.setObjectName("label_logo1")
        
        self.label_logo2 = QtWidgets.QLabel(self.centralwidget)
        self.label_logo2.setGeometry(QtCore.QRect(1010,0,270,140))
        self.label_logo2.setObjectName("label_logo2")
        
        self.pushButton_add_estudiante.setObjectName("pushButton_add_estudiante")
        self.listWidget_estudiantes = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_estudiantes.setGeometry(QtCore.QRect(20, 180, 441, 461))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.listWidget_estudiantes.setFont(font)
        self.listWidget_estudiantes.setObjectName("listWidget_estudiantes")
        self.scrollArea_info_estudiante = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_info_estudiante.setGeometry(QtCore.QRect(480, 160, 781, 481))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.scrollArea_info_estudiante.setFont(font)
        self.scrollArea_info_estudiante.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_info_estudiante.setWidgetResizable(True)
        self.scrollArea_info_estudiante.setObjectName("scrollArea_info_estudiante")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_apellido = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_apellido.setGeometry(QtCore.QRect(380, 20, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_apellido.setFont(font)
        self.label_apellido.setObjectName("label_apellido")
        self.label_imagen = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_imagen.setGeometry(QtCore.QRect(20, 10, 191, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_imagen.setFont(font)
        self.label_imagen.setStyleSheet("\n"
"border: 1px solid ;")
        self.label_imagen.setObjectName("label_imagen")
        self.label_nombre = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_nombre.setGeometry(QtCore.QRect(380, 50, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_nombre.setFont(font)
        self.label_nombre.setObjectName("label_nombre")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(230, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(230, 50, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(230, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_cedula = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_cedula.setGeometry(QtCore.QRect(380, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_cedula.setFont(font)
        self.label_cedula.setObjectName("label_cedula")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(230, 110, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_fecha_nac = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_fecha_nac.setGeometry(QtCore.QRect(380, 110, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_fecha_nac.setFont(font)
        self.label_fecha_nac.setObjectName("label_fecha_nac")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setGeometry(QtCore.QRect(230, 140, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_edad = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_edad.setGeometry(QtCore.QRect(380, 140, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_edad.setFont(font)
        self.label_edad.setObjectName("label_edad")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setGeometry(QtCore.QRect(20, 230, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_unidad_educativa = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_unidad_educativa.setGeometry(QtCore.QRect(380, 170, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_unidad_educativa.setFont(font)
        self.label_unidad_educativa.setObjectName("label_unidad_educativa")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setGeometry(QtCore.QRect(20, 260, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setGeometry(QtCore.QRect(230, 170, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setGeometry(QtCore.QRect(20, 290, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setGeometry(QtCore.QRect(20, 320, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setGeometry(QtCore.QRect(20, 350, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.textEdit_discapacidad_est = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_discapacidad_est.setGeometry(QtCore.QRect(220, 350, 541, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_discapacidad_est.setFont(font)
        self.textEdit_discapacidad_est.setObjectName("textEdit_discapacidad_est")
        self.label_telefonos = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_telefonos.setGeometry(QtCore.QRect(220, 320, 541, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_telefonos.setFont(font)
        self.label_telefonos.setObjectName("label_telefonos")
        self.label_direccion = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_direccion.setGeometry(QtCore.QRect(220, 290, 531, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_direccion.setFont(font)
        self.label_direccion.setObjectName("label_direccion")
        self.label_cedula_representante = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_cedula_representante.setGeometry(QtCore.QRect(220, 260, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_cedula_representante.setFont(font)
        self.label_cedula_representante.setObjectName("label_cedula_representante")
        self.label_representante = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_representante.setGeometry(QtCore.QRect(220, 230, 521, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_representante.setFont(font)
        self.label_representante.setObjectName("label_representante")
        self.pushButton_goto_modules = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_goto_modules.setGeometry(QtCore.QRect(640, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_goto_modules.setFont(font)
        self.pushButton_goto_modules.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}")
        self.pushButton_goto_modules.setObjectName("pushButton_goto_modules")
        self.pushButton_goto_reports = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_goto_reports.setGeometry(QtCore.QRect(640, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_goto_reports.setFont(font)
        self.pushButton_goto_reports.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}")
        self.pushButton_goto_reports.setObjectName("pushButton_goto_reports")
        self.pushButton_edit_estudiante = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_edit_estudiante.setGeometry(QtCore.QRect(640, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_edit_estudiante.setFont(font)
        self.pushButton_edit_estudiante.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}")
        self.pushButton_edit_estudiante.setObjectName("pushButton_edit_estudiante")
        self.scrollArea_info_estudiante.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 50, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(56, 71, 151);")
        self.label.setObjectName("label")
        self.pushButton_reportes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reportes.setGeometry(QtCore.QRect(700, 120, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_reportes.setFont(font)
        self.pushButton_reportes.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}")
        self.pushButton_reportes.setCheckable(False)
        self.pushButton_reportes.setFlat(False)
        self.pushButton_reportes.setObjectName("pushButton_reportes")
        self.lineEdit_search_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search_bar.setGeometry(QtCore.QRect(20, 121, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_search_bar.setFont(font)
        self.lineEdit_search_bar.setObjectName("lineEdit")
        self.label_search_results = QtWidgets.QLabel(self.centralwidget)
        self.label_search_results.setGeometry(QtCore.QRect(20, 150, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_search_results.setFont(font)
        self.label_search_results.setText("")
        self.label_search_results.setObjectName("label_search_results")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sala Multisensorial"))
        self.pushButton_add_estudiante.setText(_translate("MainWindow", "Agregar Estudiante"))
        self.label_apellido.setText(_translate("MainWindow", "Tapia Vasquez"))
        self.label_imagen.setText(_translate("MainWindow", "Sin Imagen"))
        self.label_logo1.setText(_translate("MainWindow", ""))
        self.label_logo2.setText(_translate("MainWindow", ""))
        self.label_nombre.setText(_translate("MainWindow", "Juan Diego"))
        self.label_5.setText(_translate("MainWindow", "Apellidos:"))
        self.label_6.setText(_translate("MainWindow", "Nombres:"))
        self.label_7.setText(_translate("MainWindow", "Cedula:"))
        self.label_cedula.setText(_translate("MainWindow", "0105922587"))
        self.label_9.setText(_translate("MainWindow", "Fecha Nacimiento:"))
        self.label_fecha_nac.setText(_translate("MainWindow", "01/01/2015"))
        self.label_11.setText(_translate("MainWindow", "Edad:"))
        self.label_edad.setText(_translate("MainWindow", "8 años"))
        self.label_13.setText(_translate("MainWindow", "Representante:"))
        self.label_unidad_educativa.setText(_translate("MainWindow", "Nombre de unidad educativa"))
        self.label_15.setText(_translate("MainWindow", "Cedula Representante:"))
        self.label_16.setText(_translate("MainWindow", "Unidad Educativa:"))
        self.label_17.setText(_translate("MainWindow", "Direccion:"))
        self.label_18.setText(_translate("MainWindow", "Telefono/s Contacto:"))
        self.label_19.setText(_translate("MainWindow", "Discapacidad/es:"))
        self.textEdit_discapacidad_est.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_telefonos.setText(_translate("MainWindow", "0984239035, 4085702,"))
        self.label_direccion.setText(_translate("MainWindow", "Parroquia comunidad "))
        self.label_cedula_representante.setText(_translate("MainWindow", "01059224447"))
        self.label_representante.setText(_translate("MainWindow", "Tapia Vazques Juan Diego"))
        self.pushButton_goto_modules.setText(_translate("MainWindow", "Ir a Modulos"))
        self.pushButton_goto_reports.setText(_translate("MainWindow", "Ir a Reportes"))
        self.pushButton_edit_estudiante.setText(_translate("MainWindow", "Editar"))
        self.label.setText(_translate("MainWindow", "Sala Multisensorial"))
        self.pushButton_reportes.setText(_translate("MainWindow", "Invitado"))
