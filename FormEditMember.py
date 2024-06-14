from PyQt6 import QtCore, QtGui, QtWidgets
from DbManager import DbManager


class Ui_FormEditMember(QtCore.QObject):
    memberEdited = QtCore.pyqtSignal()  # Signal to notify that a member has been edited

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 320)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 100, 31))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 100, 31))
        self.label_2.setObjectName("label_2")

        self.textEdit = QtWidgets.QLineEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(150, 50, 291, 31))
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QComboBox(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 100, 291, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.addItem("")
        self.textEdit_2.addItem("")
        self.textEdit_2.addItem("")
        self.textEdit_2.addItem("")
        self.textEdit_2.addItem("")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 220, 131, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 220, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect buttons to methods
        self.pushButton.clicked.connect(self.saveEditedMember)
        self.pushButton_2.clicked.connect(Form.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Edit Member"))
        self.label.setText(_translate("Form", "Username:"))
        self.label_2.setText(_translate("Form", "Type:"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))

        # Populate combobox with member types
        self.textEdit_2.setItemText(0, _translate("Form", "Type 1"))
        self.textEdit_2.setItemText(1, _translate("Form", "Type 2"))
        self.textEdit_2.setItemText(2, _translate("Form", "Type 3"))
        self.textEdit_2.setItemText(3, _translate("Form", "Type 4"))
        self.textEdit_2.setItemText(4, _translate("Form", "Type 5"))

    def loadMemberData(self, member_id):
        db = DbManager()
        db.open_connection()

        # Retrieve member data based on member_id
        member_data = db.cursor.execute("SELECT users.username, members.type "
                                        "FROM members "
                                        "INNER JOIN users ON members.user_id = users.id "
                                        "WHERE members.id = ?", (member_id,)).fetchone()

        db.close_connection()

        if member_data:
            username, member_type = member_data
            self.textEdit.setText(username)

            # Convert member_type to string if it's not already
            member_type = str(member_type)

            index = self.textEdit_2.findText(member_type)
            if index >= 0:
                self.textEdit_2.setCurrentIndex(index)

            # Store member_id for saving edits later
            self.member_id = member_id
        else:
            # Handle case where member_id does not exist
            QtWidgets.QMessageBox.warning(None, 'Error', 'Member ID does not exist.')

    def saveEditedMember(self):
        username = self.textEdit.text().strip()
        member_type = self.textEdit_2.currentText()

        if username and member_type:
            db = DbManager()
            db.open_connection()

            # Update user's username
            db.cursor.execute("UPDATE users SET username = ? WHERE id = ?",
                              (username, self.member_id))

            # Update member's type
            db.cursor.execute("UPDATE members SET type = ? WHERE id = ?",
                              (member_type, self.member_id))

            db.conn.commit()
            db.close_connection()

            self.memberEdited.emit()  # Emit signal that a member has been edited
            QtWidgets.QMessageBox.information(None, 'Success', 'Member updated successfully!')
        else:
            QtWidgets.QMessageBox.warning(None, 'Input Error', 'All fields are required!')
