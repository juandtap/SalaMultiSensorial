# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\form_modulo_grafomotriz_beta.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
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
        self.label_logo1.setGeometry(QtCore.QRect(0, 0, 260, 150))
        self.label_logo1.setText("")
        self.label_logo1.setObjectName("label_logo1")
        self.label_logo2 = QtWidgets.QLabel(Form_modulo_grafomotricidad)
        self.label_logo2.setGeometry(QtCore.QRect(1150, 0, 130, 130))
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
        self.label_3.setGeometry(QtCore.QRect(580, 580, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_3.setObjectName("label_3")
        self.timeEdit_limit_time = QtWidgets.QTimeEdit(Form_modulo_grafomotricidad)
        self.timeEdit_limit_time.setGeometry(QtCore.QRect(700, 570, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.timeEdit_limit_time.setFont(font)
        self.timeEdit_limit_time.setObjectName("timeEdit_limit_time")
        self.label_4 = QtWidgets.QLabel(Form_modulo_grafomotricidad)
        self.label_4.setGeometry(QtCore.QRect(700, 550, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayoutWidget = QtWidgets.QWidget(Form_modulo_grafomotricidad)
        self.formLayoutWidget.setGeometry(QtCore.QRect(900, 550, 301, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(9)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_figure = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_figure.setFont(font)
        self.lineEdit_figure.setReadOnly(True)
        self.lineEdit_figure.setObjectName("lineEdit_figure")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_figure)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_result = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_result.setFont(font)
        self.lineEdit_result.setText("")
        self.lineEdit_result.setReadOnly(True)
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_result)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_time_taken = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_time_taken.setFont(font)
        self.lineEdit_time_taken.setText("")
        self.lineEdit_time_taken.setReadOnly(True)
        self.lineEdit_time_taken.setObjectName("lineEdit_time_taken")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_time_taken)
        self.pushButton_start = QtWidgets.QPushButton(Form_modulo_grafomotricidad)
        self.pushButton_start.setGeometry(QtCore.QRect(540, 630, 101, 31))
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
        self.pushButton_stop = QtWidgets.QPushButton(Form_modulo_grafomotricidad)
        self.pushButton_stop.setGeometry(QtCore.QRect(650, 630, 101, 31))
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
        self.pushButton_save = QtWidgets.QPushButton(Form_modulo_grafomotricidad)
        self.pushButton_save.setGeometry(QtCore.QRect(760, 630, 101, 31))
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
        self.label_9 = QtWidgets.QLabel(Form_modulo_grafomotricidad)
        self.label_9.setGeometry(QtCore.QRect(900, 690, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_conn_status = QtWidgets.QLabel(Form_modulo_grafomotricidad)
        self.label_conn_status.setGeometry(QtCore.QRect(1110, 690, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_conn_status.setFont(font)
        self.label_conn_status.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_conn_status.setObjectName("label_conn_status")
        self.gridLayoutWidget = QtWidgets.QWidget(Form_modulo_grafomotricidad)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(540, 130, 691, 397))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 1)
        self.label_figure_04 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_04.setText("")
        self.label_figure_04.setObjectName("label_figure_04")
        self.gridLayout.addWidget(self.label_figure_04, 0, 3, 1, 1)
        self.radioButton_9 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setText("")
        self.radioButton_9.setObjectName("radioButton_9")
        self.gridLayout.addWidget(self.radioButton_9, 3, 2, 1, 1)
        self.label_figure_05 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_05.setText("")
        self.label_figure_05.setObjectName("label_figure_05")
        self.gridLayout.addWidget(self.label_figure_05, 0, 4, 1, 1)
        self.radioButton_11 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setText("")
        self.radioButton_11.setObjectName("radioButton_11")
        self.gridLayout.addWidget(self.radioButton_11, 3, 4, 1, 1)
        self.label_figure_01 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_01.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_01.setText("")
        self.label_figure_01.setObjectName("label_figure_01")
        self.gridLayout.addWidget(self.label_figure_01, 0, 0, 1, 1)
        self.label_figure_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_12.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_12.setText("")
        self.label_figure_12.setObjectName("label_figure_12")
        self.gridLayout.addWidget(self.label_figure_12, 2, 5, 1, 1)
        self.label_figure_08 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_08.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_08.setText("")
        self.label_figure_08.setObjectName("label_figure_08")
        self.gridLayout.addWidget(self.label_figure_08, 2, 1, 1, 1)
        self.label_figure_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_11.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_11.setText("")
        self.label_figure_11.setObjectName("label_figure_11")
        self.gridLayout.addWidget(self.label_figure_11, 2, 4, 1, 1)
        self.radioButton_10 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setText("")
        self.radioButton_10.setObjectName("radioButton_10")
        self.gridLayout.addWidget(self.radioButton_10, 3, 3, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 1, 2, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setText("")
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout.addWidget(self.radioButton_1, 1, 0, 1, 1)
        self.label_figure_09 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_09.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_09.setText("")
        self.label_figure_09.setObjectName("label_figure_09")
        self.gridLayout.addWidget(self.label_figure_09, 2, 2, 1, 1)
        self.label_figure_03 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_03.setText("")
        self.label_figure_03.setObjectName("label_figure_03")
        self.gridLayout.addWidget(self.label_figure_03, 0, 2, 1, 1)
        self.radioButton_12 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setText("")
        self.radioButton_12.setObjectName("radioButton_12")
        self.gridLayout.addWidget(self.radioButton_12, 3, 5, 1, 1)
        self.label_figure_07 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_07.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_07.setText("")
        self.label_figure_07.setObjectName("label_figure_07")
        self.gridLayout.addWidget(self.label_figure_07, 2, 0, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setText("")
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 3, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 1, 3, 1, 1)
        self.label_figure_02 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_02.setText("")
        self.label_figure_02.setObjectName("label_figure_02")
        self.gridLayout.addWidget(self.label_figure_02, 0, 1, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setText("")
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 1, 4, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setText("")
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout.addWidget(self.radioButton_8, 3, 1, 1, 1)
        self.label_figure_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_10.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_10.setText("")
        self.label_figure_10.setObjectName("label_figure_10")
        self.gridLayout.addWidget(self.label_figure_10, 2, 3, 1, 1)
        self.label_figure_06 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_06.setText("")
        self.label_figure_06.setObjectName("label_figure_06")
        self.gridLayout.addWidget(self.label_figure_06, 0, 5, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setText("")
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 1, 5, 1, 1)
        self.label_figure_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_13.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_13.setText("")
        self.label_figure_13.setObjectName("label_figure_13")
        self.gridLayout.addWidget(self.label_figure_13, 4, 0, 1, 1)
        self.radioButton_13 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_13.setFont(font)
        self.radioButton_13.setText("")
        self.radioButton_13.setObjectName("radioButton_13")
        self.gridLayout.addWidget(self.radioButton_13, 5, 0, 1, 1)
        self.label_figure_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_14.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_14.setText("")
        self.label_figure_14.setObjectName("label_figure_14")
        self.gridLayout.addWidget(self.label_figure_14, 4, 1, 1, 1)
        self.label_figure_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_15.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_15.setText("")
        self.label_figure_15.setObjectName("label_figure_15")
        self.gridLayout.addWidget(self.label_figure_15, 4, 2, 1, 1)
        self.label_figure_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_16.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_16.setText("")
        self.label_figure_16.setObjectName("label_figure_16")
        self.gridLayout.addWidget(self.label_figure_16, 4, 3, 1, 1)
        self.label_figure_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_17.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_17.setText("")
        self.label_figure_17.setObjectName("label_figure_17")
        self.gridLayout.addWidget(self.label_figure_17, 4, 4, 1, 1)
        self.label_figure_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_figure_18.setMaximumSize(QtCore.QSize(100, 100))
        self.label_figure_18.setText("")
        self.label_figure_18.setObjectName("label_figure_18")
        self.gridLayout.addWidget(self.label_figure_18, 4, 5, 1, 1)
        self.radioButton_14 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_14.setFont(font)
        self.radioButton_14.setText("")
        self.radioButton_14.setObjectName("radioButton_14")
        self.gridLayout.addWidget(self.radioButton_14, 5, 1, 1, 1)
        self.radioButton_15 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_15.setFont(font)
        self.radioButton_15.setText("")
        self.radioButton_15.setObjectName("radioButton_15")
        self.gridLayout.addWidget(self.radioButton_15, 5, 2, 1, 1)
        self.radioButton_16 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_16.setFont(font)
        self.radioButton_16.setText("")
        self.radioButton_16.setObjectName("radioButton_16")
        self.gridLayout.addWidget(self.radioButton_16, 5, 3, 1, 1)
        self.radioButton_17 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_17.setFont(font)
        self.radioButton_17.setText("")
        self.radioButton_17.setObjectName("radioButton_17")
        self.gridLayout.addWidget(self.radioButton_17, 5, 4, 1, 1)
        self.radioButton_18 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_18.setFont(font)
        self.radioButton_18.setText("")
        self.radioButton_18.setObjectName("radioButton_18")
        self.gridLayout.addWidget(self.radioButton_18, 5, 5, 1, 1)

        self.retranslateUi(Form_modulo_grafomotricidad)
        QtCore.QMetaObject.connectSlotsByName(Form_modulo_grafomotricidad)

    def retranslateUi(self, Form_modulo_grafomotricidad):
        _translate = QtCore.QCoreApplication.translate
        Form_modulo_grafomotricidad.setWindowTitle(_translate("Form_modulo_grafomotricidad", "Modulo Grafomotricidad"))
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
        self.label_8.setText(_translate("Form_modulo_grafomotricidad", "Figura seleccionada"))
        self.label_5.setText(_translate("Form_modulo_grafomotricidad", "Resultado:"))
        self.label_7.setText(_translate("Form_modulo_grafomotricidad", "Tiempo Tomado:"))
        self.pushButton_start.setText(_translate("Form_modulo_grafomotricidad", "Iniciar"))
        self.pushButton_stop.setText(_translate("Form_modulo_grafomotricidad", "Detener"))
        self.pushButton_save.setText(_translate("Form_modulo_grafomotricidad", "Guardar"))
        self.label_9.setText(_translate("Form_modulo_grafomotricidad", "Estado Conexion Bluetooth: "))
        self.label_conn_status.setText(_translate("Form_modulo_grafomotricidad", "Conectado"))
