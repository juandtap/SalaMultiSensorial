# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog_message.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Message_dialog(object):
    def setupUi(self, Message_dialog):
        Message_dialog.setObjectName("Message_dialog")
        Message_dialog.resize(350, 100)
        Message_dialog.setMinimumSize(QtCore.QSize(350, 100))
        Message_dialog.setMaximumSize(QtCore.QSize(350, 100))
        Message_dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_1 = QtWidgets.QLabel(Message_dialog)
        self.label_1.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.pushButton_accept_dialog = QtWidgets.QPushButton(Message_dialog)
        self.pushButton_accept_dialog.setGeometry(QtCore.QRect(130, 60, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.pushButton_accept_dialog.setFont(font)
        self.pushButton_accept_dialog.setStyleSheet("QPushButton {\n"
"   border-radius: 10px;\n"
"    background-color: rgb(56, 71, 151);\n"
"  color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid;\n"
"}\n"
"")
        self.pushButton_accept_dialog.setObjectName("pushButton_accept_dialog")
        self.label_message = QtWidgets.QLabel(Message_dialog)
        self.label_message.setGeometry(QtCore.QRect(100, 20, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_message.setFont(font)
        self.label_message.setObjectName("label_message")

        self.retranslateUi(Message_dialog)
        QtCore.QMetaObject.connectSlotsByName(Message_dialog)

    def retranslateUi(self, Message_dialog):
        _translate = QtCore.QCoreApplication.translate
        Message_dialog.setWindowTitle(_translate("Message_dialog", "Mensaje"))
        self.label_1.setText(_translate("Message_dialog", "Mensaje: "))
        self.pushButton_accept_dialog.setText(_translate("Message_dialog", "Aceptar"))
        self.label_message.setText(_translate("Message_dialog", "Estudiante agregado !"))
