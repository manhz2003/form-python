from PyQt6 import QtCore, QtGui, QtWidgets
from DbManager import DbManager
from Member import Member
from FormEditMember import Ui_FormEditMember
from FormAddMember import Ui_FormAddMember


class Ui_Form(QtWidgets.QWidget):
    memberAdded = QtCore.pyqtSignal()  # Signal to notify that a new member has been added

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1440, 763)

        self.txtSearch = QtWidgets.QTextEdit(Form)
        self.txtSearch.setGeometry(QtCore.QRect(550, 280, 381, 31))
        self.txtSearch.setObjectName("txtSearch")

        self.btnSearch = QtWidgets.QPushButton(Form)
        self.btnSearch.setGeometry(QtCore.QRect(550, 230, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")

        self.tableLoadingData = QtWidgets.QTableWidget(Form)
        self.tableLoadingData.setGeometry(QtCore.QRect(550, 320, 381, 192))
        self.tableLoadingData.setObjectName("tableLoadingData")
        self.tableLoadingData.setColumnCount(3)
        self.tableLoadingData.setHorizontalHeaderLabels(["ID", "Username", "Type"])

        self.btnAdd = QtWidgets.QPushButton(Form)
        self.btnAdd.setGeometry(QtCore.QRect(650, 230, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")

        self.btnEdit = QtWidgets.QPushButton(Form)
        self.btnEdit.setGeometry(QtCore.QRect(720, 230, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnEdit.setFont(font)
        self.btnEdit.setObjectName("btnEdit")

        self.btnDelete = QtWidgets.QPushButton(Form)
        self.btnDelete.setGeometry(QtCore.QRect(790, 230, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName("btnDelete")

        self.btnClose = QtWidgets.QPushButton(Form)
        self.btnClose.setGeometry(QtCore.QRect(860, 230, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect buttons to methods
        self.btnAdd.clicked.connect(self.openAddMemberForm)
        self.btnEdit.clicked.connect(self.openEditMemberForm)
        self.btnDelete.clicked.connect(self.deleteMember)
        self.btnClose.clicked.connect(Form.close)
        self.btnSearch.clicked.connect(self.searchMembers)

        # Load initial members data
        self.loadMembers()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Member Management"))
        self.txtSearch.setPlaceholderText(_translate("Form", "Enter search term"))
        self.btnSearch.setText(_translate("Form", "Search"))
        self.btnAdd.setText(_translate("Form", "Add"))
        self.btnEdit.setText(_translate("Form", "Edit"))
        self.btnDelete.setText(_translate("Form", "Delete"))
        self.btnClose.setText(_translate("Form", "Close"))

    def openAddMemberForm(self):
        self.addMemberForm = QtWidgets.QWidget()
        self.ui_add_member = Ui_FormAddMember()
        self.ui_add_member.setupUi(self.addMemberForm)

        # Connect signal emitted by FormAddMember to refresh table on member added
        self.ui_add_member.memberAdded.connect(self.loadMembers)

        # Add button click handler to save member
        self.ui_add_member.pushButton.clicked.connect(self.saveMember)

        self.addMemberForm.show()

    def saveMember(self):
        username = self.ui_add_member.textEdit.text().strip()
        password = self.ui_add_member.textEdit_2.text().strip()
        member_type = self.ui_add_member.textEdit_3.text().strip()

        if username and password and member_type:
            member = Member(username, password, int(member_type))
            member.register()
            self.memberAdded.emit()  # Emit signal that a new member has been added
            self.addMemberForm.close()  # Close the add member form
        else:
            QtWidgets.QMessageBox.warning(None, 'Input Error', 'All fields are required!')

    def openEditMemberForm(self):
        selected_row = self.tableLoadingData.currentRow()
        if selected_row >= 0:
            member_id = int(self.tableLoadingData.item(selected_row, 0).text())
            self.editMemberForm = QtWidgets.QWidget()
            self.ui_edit_member = Ui_FormEditMember()
            self.ui_edit_member.setupUi(self.editMemberForm)

            # Connect signal emitted by FormEditMember to refresh table on member edited
            self.ui_edit_member.memberEdited.connect(self.loadMembers)

            # Load member data into edit form
            self.ui_edit_member.loadMemberData(member_id)  # Pass member_id to loadMemberData

            self.editMemberForm.show()

    def deleteMember(self):
        selected_row = self.tableLoadingData.currentRow()
        if selected_row >= 0:
            member_id = int(self.tableLoadingData.item(selected_row, 0).text())
            confirmation = QtWidgets.QMessageBox.question(None, 'Delete Member',
                                                          f"Are you sure you want to delete member ID {member_id}?",
                                                          QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            if confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
                # Delete member from database
                db = DbManager()
                db.open_connection()
                db.cursor.execute("DELETE FROM members WHERE user_id=?", (member_id,))
                db.conn.commit()
                db.close_connection()

                # Remove row from table view
                self.tableLoadingData.removeRow(selected_row)

    def loadMembers(self, search_term=''):
        # Clear existing table content
        self.tableLoadingData.setRowCount(0)

        # Fetch members data based on search term
        if search_term:
            members = Member.search_members(search_term)
        else:
            members = Member.get_members()

        # Populate table with retrieved members
        for row_number, row_data in enumerate(members):
            self.tableLoadingData.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableLoadingData.setItem(row_number, column_number, item)

    def searchMembers(self):
        search_term = self.txtSearch.toPlainText().strip()
        self.loadMembers(search_term)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
