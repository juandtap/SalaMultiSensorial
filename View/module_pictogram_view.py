# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\form_modulo_pictograma.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_modulo_pictograma(object):
    def setupUi(self, Form_modulo_pictograma):
        Form_modulo_pictograma.setObjectName("Form_modulo_pictograma")
        Form_modulo_pictograma.resize(1280, 720)
        Form_modulo_pictograma.setMinimumSize(QtCore.QSize(1280, 720))
        Form_modulo_pictograma.setMaximumSize(QtCore.QSize(1280, 720))
        Form_modulo_pictograma.setBaseSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form_modulo_pictograma.setFont(font)
        Form_modulo_pictograma.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_conn_status = QtWidgets.QLabel(Form_modulo_pictograma)
        self.label_conn_status.setGeometry(QtCore.QRect(1150, 680, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_conn_status.setFont(font)
        self.label_conn_status.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_conn_status.setObjectName("label_conn_status")
        self.label_logo2 = QtWidgets.QLabel(Form_modulo_pictograma)
        self.label_logo2.setGeometry(QtCore.QRect(1120, 0, 161, 131))
        self.label_logo2.setText("")
        self.label_logo2.setObjectName("label_logo2")
        self.label = QtWidgets.QLabel(Form_modulo_pictograma)
        self.label.setGeometry(QtCore.QRect(470, 20, 350, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(56, 71, 151);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit_instructions = QtWidgets.QTextEdit(Form_modulo_pictograma)
        self.textEdit_instructions.setGeometry(QtCore.QRect(40, 400, 451, 261))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.textEdit_instructions.setFont(font)
        self.textEdit_instructions.setObjectName("textEdit_instructions")
        self.label_logo1 = QtWidgets.QLabel(Form_modulo_pictograma)
        self.label_logo1.setGeometry(QtCore.QRect(0, 0, 161, 131))
        self.label_logo1.setText("")
        self.label_logo1.setObjectName("label_logo1")
        self.label_module_image = QtWidgets.QLabel(Form_modulo_pictograma)
        self.label_module_image.setGeometry(QtCore.QRect(50, 170, 441, 191))
        self.label_module_image.setText("")
        self.label_module_image.setObjectName("label_module_image")
        self.label_2 = QtWidgets.QLabel(Form_modulo_pictograma)
        self.label_2.setGeometry(QtCore.QRect(40, 380, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_2.setObjectName("label_2")
        self.label_text_status = QtWidgets.QLabel(Form_modulo_pictograma)
        self.label_text_status.setGeometry(QtCore.QRect(940, 680, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_text_status.setFont(font)
        self.label_text_status.setObjectName("label_text_status")
        self.pushButton_start = QtWidgets.QPushButton(Form_modulo_pictograma)
        self.pushButton_start.setGeometry(QtCore.QRect(710, 610, 101, 31))
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
        self.pushButton_stop = QtWidgets.QPushButton(Form_modulo_pictograma)
        self.pushButton_stop.setGeometry(QtCore.QRect(830, 610, 101, 31))
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
        self.pushButton_save = QtWidgets.QPushButton(Form_modulo_pictograma)
        self.pushButton_save.setGeometry(QtCore.QRect(950, 610, 101, 31))
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
        self.gridLayoutWidget = QtWidgets.QWidget(Form_modulo_pictograma)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(510, 400, 291, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_correctos = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_correctos.setFont(font)
        self.lineEdit_correctos.setReadOnly(True)
        self.lineEdit_correctos.setObjectName("lineEdit_correctos")
        self.gridLayout.addWidget(self.lineEdit_correctos, 1, 1, 1, 1)
        self.lineEdit_incorrectos = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_incorrectos.setFont(font)
        self.lineEdit_incorrectos.setText("")
        self.lineEdit_incorrectos.setReadOnly(True)
        self.lineEdit_incorrectos.setObjectName("lineEdit_incorrectos")
        self.gridLayout.addWidget(self.lineEdit_incorrectos, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form_modulo_pictograma)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(510, 200, 671, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEdit_num_pistogramas_seleccionados = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_num_pistogramas_seleccionados.setObjectName("lineEdit_num_pistogramas_seleccionados")
        self.gridLayout_2.addWidget(self.lineEdit_num_pistogramas_seleccionados, 2, 1, 1, 1)
        self.lineEdit_tamanio_tabla = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_tamanio_tabla.setObjectName("lineEdit_tamanio_tabla")
        self.gridLayout_2.addWidget(self.lineEdit_tamanio_tabla, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEdit_num_pictogramas_disponibles = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_num_pictogramas_disponibles.setFont(font)
        self.lineEdit_num_pictogramas_disponibles.setReadOnly(True)
        self.lineEdit_num_pictogramas_disponibles.setObjectName("lineEdit_num_pictogramas_disponibles")
        self.gridLayout_2.addWidget(self.lineEdit_num_pictogramas_disponibles, 1, 1, 1, 1)
        self.lineEdit_categoria_seleccionada = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_categoria_seleccionada.setFont(font)
        self.lineEdit_categoria_seleccionada.setText("")
        self.lineEdit_categoria_seleccionada.setReadOnly(True)
        self.lineEdit_categoria_seleccionada.setObjectName("lineEdit_categoria_seleccionada")
        self.gridLayout_2.addWidget(self.lineEdit_categoria_seleccionada, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)
        self.lineEdit_categorias_mostradas = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_categorias_mostradas.setObjectName("lineEdit_categorias_mostradas")
        self.gridLayout_2.addWidget(self.lineEdit_categorias_mostradas, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form_modulo_pictograma)
        self.label_3.setGeometry(QtCore.QRect(510, 370, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form_modulo_pictograma)
        self.label_4.setGeometry(QtCore.QRect(510, 160, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_4.setObjectName("label_4")
        self.label_reading_status = QtWidgets.QLabel(Form_modulo_pictograma)
        self.label_reading_status.setGeometry(QtCore.QRect(810, 560, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_reading_status.setFont(font)
        self.label_reading_status.setStyleSheet("color: rgb(56, 71, 151);")
        self.label_reading_status.setObjectName("label_reading_status")

        self.retranslateUi(Form_modulo_pictograma)
        QtCore.QMetaObject.connectSlotsByName(Form_modulo_pictograma)

    def retranslateUi(self, Form_modulo_pictograma):
        _translate = QtCore.QCoreApplication.translate
        Form_modulo_pictograma.setWindowTitle(_translate("Form_modulo_pictograma", "Modulo Panel de Pictogramas"))
        self.label_conn_status.setText(_translate("Form_modulo_pictograma", "Conectado"))
        self.label.setText(_translate("Form_modulo_pictograma", "MODULO: PICTOGRAMAS"))
        self.textEdit_instructions.setHtml(_translate("Form_modulo_pictograma", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Arial\',\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean consectetur tristique purus vel tristique. Aliquam mattis purus ultricies, lobortis lacus at, vestibulum velit. Nam nulla ligula, sollicitudin consectetur porta blandit, fringilla a quam. Nulla suscipit mauris at semper tempor. Aliquam vestibulum eu nisl a ornare. Duis nec interdum leo. Mauris nec laoreet lectus. Nullam pharetra, risus vitae aliquet malesuada, arcu nibh malesuada erat, quis viverra dui sem et nisl. Donec eu felis finibus, maximus nulla venenatis, pulvinar mi. Donec at hendrerit ex. Donec nec turpis sed leo suscipit vulputate id ut ex. Integer ornare lorem dui, quis luctus risus maximus ac.</span></p></body></html>"))
        self.label_2.setText(_translate("Form_modulo_pictograma", "Instrucciones"))
        self.label_text_status.setText(_translate("Form_modulo_pictograma", "Estado Conexion Bluetooth: "))
        self.pushButton_start.setText(_translate("Form_modulo_pictograma", "Iniciar"))
        self.pushButton_stop.setText(_translate("Form_modulo_pictograma", "Detener"))
        self.pushButton_save.setText(_translate("Form_modulo_pictograma", "Guardar"))
        self.label_7.setText(_translate("Form_modulo_pictograma", "Selecciones Correctas:"))
        self.label_8.setText(_translate("Form_modulo_pictograma", "Selecciones Incorrectas:"))
        self.label_9.setText(_translate("Form_modulo_pictograma", "Categoria seleccionada:"))
        self.label_10.setText(_translate("Form_modulo_pictograma", "Numero de picrogramas disponibles:"))
        self.label_5.setText(_translate("Form_modulo_pictograma", "Numero de pictogramas seleccionados:"))
        self.label_6.setText(_translate("Form_modulo_pictograma", "Tamaño tabla:"))
        self.label_11.setText(_translate("Form_modulo_pictograma", "Categorias mostradas:"))
        self.label_3.setText(_translate("Form_modulo_pictograma", "Resultados:"))
        self.label_4.setText(_translate("Form_modulo_pictograma", "Configuración:"))
        self.label_reading_status.setText(_translate("Form_modulo_pictograma", "Esperando datos ..."))
