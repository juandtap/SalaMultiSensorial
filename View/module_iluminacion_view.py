# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\form_modulo_iluminacion.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_modulo_iluminacion(object):
    def setupUi(self, Form_modulo_iluminacion):
        Form_modulo_iluminacion.setObjectName("Form_modulo_iluminacion")
        Form_modulo_iluminacion.resize(1280, 720)
        Form_modulo_iluminacion.setMinimumSize(QtCore.QSize(1280, 720))
        Form_modulo_iluminacion.setMaximumSize(QtCore.QSize(1280, 720))
        Form_modulo_iluminacion.setBaseSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form_modulo_iluminacion.setFont(font)
        Form_modulo_iluminacion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_conn_status = QtWidgets.QLabel(Form_modulo_iluminacion)
        self.label_conn_status.setGeometry(QtCore.QRect(1150, 680, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_conn_status.setFont(font)
        self.label_conn_status.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_conn_status.setObjectName("label_conn_status")
        self.label_logo2 = QtWidgets.QLabel(Form_modulo_iluminacion)
        self.label_logo2.setGeometry(QtCore.QRect(1120, 0, 161, 131))
        self.label_logo2.setText("")
        self.label_logo2.setObjectName("label_logo2")
        self.label = QtWidgets.QLabel(Form_modulo_iluminacion)
        self.label.setGeometry(QtCore.QRect(470, 20, 350, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(56, 71, 151);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit_instructions = QtWidgets.QTextEdit(Form_modulo_iluminacion)
        self.textEdit_instructions.setGeometry(QtCore.QRect(40, 400, 451, 261))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.textEdit_instructions.setFont(font)
        self.textEdit_instructions.setObjectName("textEdit_instructions")
        self.label_logo1 = QtWidgets.QLabel(Form_modulo_iluminacion)
        self.label_logo1.setGeometry(QtCore.QRect(0, 0, 161, 131))
        self.label_logo1.setText("")
        self.label_logo1.setObjectName("label_logo1")
        self.label_module_image = QtWidgets.QLabel(Form_modulo_iluminacion)
        self.label_module_image.setGeometry(QtCore.QRect(50, 170, 441, 191))
        self.label_module_image.setText("")
        self.label_module_image.setObjectName("label_module_image")
        self.label_2 = QtWidgets.QLabel(Form_modulo_iluminacion)
        self.label_2.setGeometry(QtCore.QRect(40, 380, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_2.setObjectName("label_2")
        self.label_text_status = QtWidgets.QLabel(Form_modulo_iluminacion)
        self.label_text_status.setGeometry(QtCore.QRect(940, 680, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_text_status.setFont(font)
        self.label_text_status.setObjectName("label_text_status")
        self.pushButton_start = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_start.setGeometry(QtCore.QRect(710, 560, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_stop.setGeometry(QtCore.QRect(830, 560, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_save = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_save.setGeometry(QtCore.QRect(950, 560, 101, 31))
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
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_save.setObjectName("pushButton_save")
        self.label_3 = QtWidgets.QLabel(Form_modulo_iluminacion)
        self.label_3.setGeometry(QtCore.QRect(810, 160, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_3.setObjectName("label_3")
        self.pushButton_1 = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_1.setGeometry(QtCore.QRect(540, 210, 61, 61))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 210, 61, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(0,255, 0);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 210, 61, 61))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(0, 0, 255);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 210, 61, 61))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(255,215,0);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_5.setGeometry(QtCore.QRect(860, 210, 61, 61))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(0, 255, 255);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_6.setGeometry(QtCore.QRect(940, 210, 61, 61))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(255, 255,255);\n"
"   border: 1px solid;\n"
"  color: rgb(0,0,0); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_7.setGeometry(QtCore.QRect(1020, 210, 61, 61))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(255,69,0);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_8.setGeometry(QtCore.QRect(1100, 210, 61, 61))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(255,0,255);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form_modulo_iluminacion)
        self.pushButton_9.setGeometry(QtCore.QRect(1180, 210, 61, 61))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(128,0,128);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_4 = QtWidgets.QLabel(Form_modulo_iluminacion)
        self.label_4.setGeometry(QtCore.QRect(780, 390, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form_modulo_iluminacion)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(730, 420, 306, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_R_code = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_R_code.setFont(font)
        self.lineEdit_R_code.setText("")
        self.lineEdit_R_code.setPlaceholderText("")
        self.lineEdit_R_code.setObjectName("lineEdit_R_code")
        self.horizontalLayout.addWidget(self.lineEdit_R_code)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.lineEdit_G_code = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_G_code.setFont(font)
        self.lineEdit_G_code.setObjectName("lineEdit_G_code")
        self.horizontalLayout.addWidget(self.lineEdit_G_code)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.lineEdit_B_code = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_B_code.setFont(font)
        self.lineEdit_B_code.setObjectName("lineEdit_B_code")
        self.horizontalLayout.addWidget(self.lineEdit_B_code)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form_modulo_iluminacion)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(720, 300, 321, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.lineEdit_selected_color = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_selected_color.setFont(font)
        self.lineEdit_selected_color.setText("")
        self.lineEdit_selected_color.setReadOnly(True)
        self.lineEdit_selected_color.setObjectName("lineEdit_selected_color")
        self.horizontalLayout_2.addWidget(self.lineEdit_selected_color)

        self.retranslateUi(Form_modulo_iluminacion)
        QtCore.QMetaObject.connectSlotsByName(Form_modulo_iluminacion)

    def retranslateUi(self, Form_modulo_iluminacion):
        _translate = QtCore.QCoreApplication.translate
        Form_modulo_iluminacion.setWindowTitle(_translate("Form_modulo_iluminacion", "Modulo Vumetro"))
        self.label_conn_status.setText(_translate("Form_modulo_iluminacion", "Conectado"))
        self.label.setText(_translate("Form_modulo_iluminacion", "MODULO: ILUMINACION"))
        self.textEdit_instructions.setHtml(_translate("Form_modulo_iluminacion", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Arial\',\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean consectetur tristique purus vel tristique. Aliquam mattis purus ultricies, lobortis lacus at, vestibulum velit. Nam nulla ligula, sollicitudin consectetur porta blandit, fringilla a quam. Nulla suscipit mauris at semper tempor. Aliquam vestibulum eu nisl a ornare. Duis nec interdum leo. Mauris nec laoreet lectus. Nullam pharetra, risus vitae aliquet malesuada, arcu nibh malesuada erat, quis viverra dui sem et nisl. Donec eu felis finibus, maximus nulla venenatis, pulvinar mi. Donec at hendrerit ex. Donec nec turpis sed leo suscipit vulputate id ut ex. Integer ornare lorem dui, quis luctus risus maximus ac.</span></p></body></html>"))
        self.label_2.setText(_translate("Form_modulo_iluminacion", "Instrucciones"))
        self.label_text_status.setText(_translate("Form_modulo_iluminacion", "Estado Conexion Bluetooth: "))
        self.pushButton_start.setText(_translate("Form_modulo_iluminacion", "Iniciar"))
        self.pushButton_stop.setText(_translate("Form_modulo_iluminacion", "Detener"))
        self.pushButton_save.setText(_translate("Form_modulo_iluminacion", "Guardar"))
        self.label_3.setText(_translate("Form_modulo_iluminacion", "Seleccionar Color:"))
        self.pushButton_1.setText(_translate("Form_modulo_iluminacion", "R"))
        self.pushButton_2.setText(_translate("Form_modulo_iluminacion", "G"))
        self.pushButton_3.setText(_translate("Form_modulo_iluminacion", "B"))
        self.pushButton_4.setText(_translate("Form_modulo_iluminacion", "Y"))
        self.pushButton_5.setText(_translate("Form_modulo_iluminacion", "C"))
        self.pushButton_6.setText(_translate("Form_modulo_iluminacion", "W"))
        self.pushButton_7.setText(_translate("Form_modulo_iluminacion", "O"))
        self.pushButton_8.setText(_translate("Form_modulo_iluminacion", "M"))
        self.pushButton_9.setText(_translate("Form_modulo_iluminacion", "P"))
        self.label_4.setText(_translate("Form_modulo_iluminacion", "Color Personalizado (RGB):"))
        self.label_5.setText(_translate("Form_modulo_iluminacion", "R: "))
        self.label_6.setText(_translate("Form_modulo_iluminacion", "G:"))
        self.label_7.setText(_translate("Form_modulo_iluminacion", "B: "))
        self.label_8.setText(_translate("Form_modulo_iluminacion", "Color seleccionado:"))