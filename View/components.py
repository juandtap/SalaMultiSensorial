import sys
sys.path.append(".")
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox
from PyQt5.QtCore import Qt
from View.message_dialog_view import Ui_Message_dialog
from View.add_school_view import Ui_add_Unidad_Educativa
from Controller.school_control import add_school_control

class AddSchool(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_add_school = Ui_add_Unidad_Educativa()
        self.ui_add_school.setupUi(self)
        self.ui_add_school.pushButton_cancel.clicked.connect(self.close)
        self.ui_add_school.pushButton_save.clicked.connect(self.add_school)
    
    def add_school(self):
        flag = False
        
        flag = add_school_control(self.ui_add_school.lineEdit_name_unidad_educativa.text())
        
        if flag:
            self.new_message = MessageDialog("Unidad Educativa Agregada!")
            self.new_message.show()
            self.ui_add_school.lineEdit_name_unidad_educativa.clear()

class MessageDialog(QWidget):
    def __init__(self, message):
        super().__init__()
        self.ui_message = Ui_Message_dialog()
        self.ui_message.setupUi(self)
        self.message = message
        self.ui_message.label_message.setText(self.message)
        self.ui_message.pushButton_accept_dialog.clicked.connect(self.close)

class CheckableComboBox(QComboBox):
	def __init__(self):
		super().__init__()
		self._changed = False

		self.view().pressed.connect(self.handleItemPressed)

	def setItemChecked(self, index, checked=False):
		item = self.model().item(index, self.modelColumn()) # QStandardItem object

		if checked:
			item.setCheckState(Qt.Checked)
		else:
			item.setCheckState(Qt.Unchecked)

	def handleItemPressed(self, index):
		item = self.model().itemFromIndex(index)

		if item.checkState() == Qt.Checked:
			item.setCheckState(Qt.Unchecked)
		else:
			item.setCheckState(Qt.Checked)
		self._changed = True


	def hidePopup(self):
		if not self._changed:
			super().hidePopup()
		self._changed = False

	def itemChecked(self, index):
		item = self.model().item(index, self.modelColumn())
		return item.checkState() == Qt.Checked