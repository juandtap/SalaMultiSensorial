# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\form_modulo_grafomotriz_beta.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_modulo_grafomotricidad(object):
    def setupUi(self, Form_modulo_grafomotricidad):
        Form_modulo_grafomotricidad.setObjectName("Form_modulo_grafomotricidad")
        Form_modulo_grafomotricidad.setWindowModality(QtCore.Qt.NonModal)
        Form_modulo_grafomotricidad.resize(1280, 720)
        Form_modulo_grafomotricidad.setMinimumSize(QtCore.QSize(1280, 720))
        Form_modulo_grafomotricidad.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form_modulo_grafomotricidad.setFont(font)
        Form_modulo_grafomotricidad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form_modulo_grafomotricidad)
        self.label.setGeometry(QtCore.QRect(470, 20, 350, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(56, 71, 151);")
        self.label.setObjectName("label")
        self.label_logo1 = QtWidgets.QLabel(Form_modulo_grafomotricidad)
        self.label_logo1.setGeometry(QtCore.QRect(0, 0, 161, 131))
        self.label_logo1.setText("")
        self.label_logo1.setObjectName("label_logo1")
        self.label_logo2 = QtWidgets.QLabel(Form_modulo_grafomotricidad)
        self.label_logo2.setGeometry(QtCore.QRect(1120, 0, 161, 131))
        self.label_logo2.setText("")
        self.label_logo2.setObjectName("label_logo2")
        self.label_2 = QtWidgets.QLabel(Form_modulo_grafomotricidad)
        self.label_2.setGeometry(QtCore.QRect(40, 380, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_2.setObjectName("label_2")
        self.textEdit_instructions = QtWidgets.QTextEdit(Form_modulo_grafomotricidad)
        self.textEdit_instructions.setGeometry(QtCore.QRect(40, 400, 451, 261))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.textEdit_instructions.setFont(font)
        self.textEdit_instructions.setObjectName("textEdit_instructions")
        self.label_module_image = QtWidgets.QLabel(Form_modulo_grafomotricidad)
        self.label_module_image.setGeometry(QtCore.QRect(50, 170, 441, 191))
        self.label_module_image.setText("")
        self.label_module_image.setObjectName("label_module_image")
        self.label_3 = QtWidgets.QLabel(Form_modulo_grafomotricidad)
        self.label_3.setGeometry(QtCore.QRect(770, 230, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_3.setObjectName("label_3")
        self.timeEdit_limit_time = QtWidgets.QTimeEdit(Form_modulo_grafomotricidad)
        self.timeEdit_limit_time.setGeometry(QtCore.QRect(890, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.timeEdit_limit_time.setFont(font)
        self.timeEdit_limit_time.setObjectName("timeEdit_limit_time")
        self.label_4 = QtWidgets.QLabel(Form_modulo_grafomotricidad)
        self.label_4.setGeometry(QtCore.QRect(890, 200, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayoutWidget = QtWidgets.QWidget(Form_modulo_grafomotricidad)
        self.formLayoutWidget.setGeometry(QtCore.QRect(790, 390, 211, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(9)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_success = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_success.setFont(font)
        self.lineEdit_success.setText("")
        self.lineEdit_success.setReadOnly(True)
        self.lineEdit_success.setObjectName("lineEdit_success")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_success)
        self.lineEdit_fails = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_fails.setFont(font)
        self.lineEdit_fails.setText("")
        self.lineEdit_fails.setReadOnly(True)
        self.lineEdit_fails.setObjectName("lineEdit_fails")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fails)
        self.lineEdit_remaining_time = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_remaining_time.setFont(font)
        self.lineEdit_remaining_time.setText("")
        self.lineEdit_remaining_time.setReadOnly(True)
        self.lineEdit_remaining_time.setObjectName("lineEdit_remaining_time")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_remaining_time)
        self.pushButton_start = QtWidgets.QPushButton(Form_modulo_grafomotricidad)
        self.pushButton_start.setGeometry(QtCore.QRect(710, 300, 101, 31))
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
"}")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(Form_modulo_grafomotricidad)
        self.pushButton_stop.setGeometry(QtCore.QRect(840, 300, 101, 31))
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
"\n"
"QPushButton:disabled {\n"
"background-color:#A0A0A0;\n"
"}\n")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_save = QtWidgets.QPushButton(Form_modulo_grafomotricidad)
        self.pushButton_save.setGeometry(QtCore.QRect(970, 300, 101, 31))
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

        self.retranslateUi(Form_modulo_grafomotricidad)
        QtCore.QMetaObject.connectSlotsByName(Form_modulo_grafomotricidad)

    def retranslateUi(self, Form_modulo_grafomotricidad):
        _translate = QtCore.QCoreApplication.translate
        Form_modulo_grafomotricidad.setWindowTitle(_translate("Form_modulo_grafomotricidad", "Form"))
        self.label.setText(_translate("Form_modulo_grafomotricidad", "MODULO: GRAFOMOTRICIDAD"))
        self.label_2.setText(_translate("Form_modulo_grafomotricidad", "Instrucciones"))
        self.textEdit_instructions.setHtml(_translate("Form_modulo_grafomotricidad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Arial\',\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean consectetur tristique purus vel tristique. Aliquam mattis purus ultricies, lobortis lacus at, vestibulum velit. Nam nulla ligula, sollicitudin consectetur porta blandit, fringilla a quam. Nulla suscipit mauris at semper tempor. Aliquam vestibulum eu nisl a ornare. Duis nec interdum leo. Mauris nec laoreet lectus. Nullam pharetra, risus vitae aliquet malesuada, arcu nibh malesuada erat, quis viverra dui sem et nisl. Donec eu felis finibus, maximus nulla venenatis, pulvinar mi. Donec at hendrerit ex. Donec nec turpis sed leo suscipit vulputate id ut ex. Integer ornare lorem dui, quis luctus risus maximus ac.</span></p></body></html>"))
        self.label_3.setText(_translate("Form_modulo_grafomotricidad", "Tiempo limite:"))
        self.timeEdit_limit_time.setDisplayFormat(_translate("Form_modulo_grafomotricidad", "mm:ss"))
        self.label_4.setText(_translate("Form_modulo_grafomotricidad", "MM:SS"))
        self.label_5.setText(_translate("Form_modulo_grafomotricidad", "Aciertos:"))
        self.label_6.setText(_translate("Form_modulo_grafomotricidad", "Fallos:"))
        self.label_7.setText(_translate("Form_modulo_grafomotricidad", "Tiempo tomado:"))
        self.pushButton_start.setText(_translate("Form_modulo_grafomotricidad", "Iniciar"))
        self.pushButton_stop.setText(_translate("Form_modulo_grafomotricidad", "Detener"))
        self.pushButton_save.setText(_translate("Form_modulo_grafomotricidad", "Guardar"))