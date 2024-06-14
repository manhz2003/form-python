from PyQt6 import QtCore, QtGui, QtWidgets
from Member import Member

class Ui_FormAddMember(QtWidgets.QWidget):
    memberAdded = QtCore.pyqtSignal()  # Signal to notify that a new member has been added

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 81, 31))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 81, 31))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 51, 31))
        self.label_3.setObjectName("label_3")

        self.textEdit = QtWidgets.QLineEdit(Form)  # Change to QLineEdit for username
        self.textEdit.setGeometry(QtCore.QRect(150, 50, 291, 31))
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QLineEdit(Form)  # Change to QLineEdit for password
        self.textEdit_2.setGeometry(QtCore.QRect(150, 100, 291, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Set as password mode

        self.textEdit_3 = QtWidgets.QLineEdit(Form)  # Change to QLineEdit for type
        self.textEdit_3.setGeometry(QtCore.QRect(150, 150, 291, 31))
        self.textEdit_3.setObjectName("textEdit_3")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 131, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 200, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect the Save button to saveMember method
        self.pushButton.clicked.connect(self.saveMember)
        # Connect the Cancel button to closeForm method
        self.pushButton_2.clicked.connect(Form.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add Member"))
        self.label.setText(_translate("Form", "UserName:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.label_3.setText(_translate("Form", "Type:"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))

    def saveMember(self):
        username = self.textEdit.text().strip()
        password = self.textEdit_2.text().strip()
        member_type = self.textEdit_3.text().strip()

        if username and password and member_type:
            member = Member(username, password, int(member_type))
            member.register()
            self.memberAdded.emit()  # Emit signal that a new member has been added
            QtWidgets.QMessageBox.information(None, 'Success', 'Member added successfully!')
        else:
            QtWidgets.QMessageBox.warning(None, 'Input Error', 'All fields are required!')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormAddMember()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
