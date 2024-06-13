from PyQt6 import QtCore, QtGui, QtWidgets
from FormAddMember import Ui_Form as FormAddMember
from FormEditMember import Ui_Form as FormEditMember

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1440, 763)
        self.txtSearch = QtWidgets.QTextEdit(parent=Form)
        self.txtSearch.setGeometry(QtCore.QRect(550, 280, 381, 31))
        self.txtSearch.setObjectName("txtSearch")
        self.btnSearch = QtWidgets.QPushButton(parent=Form)
        self.btnSearch.setGeometry(QtCore.QRect(550, 230, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")
        self.tableLoaddingData = QtWidgets.QTableWidget(parent=Form)
        self.tableLoaddingData.setGeometry(QtCore.QRect(550, 320, 381, 192))
        self.tableLoaddingData.setObjectName("tableLoaddingData")
        self.tableLoaddingData.setColumnCount(3)  # Adjust column count to 3
        self.tableLoaddingData.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableLoaddingData.setHorizontalHeaderItem(0, item)  # Placeholder for ID
        item = QtWidgets.QTableWidgetItem()
        self.tableLoaddingData.setHorizontalHeaderItem(1, item)  # Assuming this is UserName
        item = QtWidgets.QTableWidgetItem()
        self.tableLoaddingData.setHorizontalHeaderItem(2, item)  # Assuming this is Type

        self.btnAdd = QtWidgets.QPushButton(parent=Form)
        self.btnAdd.setGeometry(QtCore.QRect(650, 230, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")

        self.btnEdit = QtWidgets.QPushButton(parent=Form)
        self.btnEdit.setGeometry(QtCore.QRect(720, 230, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnEdit.setFont(font)
        self.btnEdit.setObjectName("btnEdit")

        self.btnDelete = QtWidgets.QPushButton(parent=Form)
        self.btnDelete.setGeometry(QtCore.QRect(790, 230, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName("btnDelete")

        self.btnClose = QtWidgets.QPushButton(parent=Form)
        self.btnClose.setGeometry(QtCore.QRect(860, 230, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect the Add button to openAddMemberForm method
        self.btnAdd.clicked.connect(self.openAddMemberForm)

        # Connect the Edit button to openEditMemberForm method
        self.btnEdit.clicked.connect(self.openEditMemberForm)

        # Connect the Close button to close only the current form
        self.btnClose.clicked.connect(Form.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.txtSearch.setPlaceholderText(_translate("Form", "Nhập vào giá trị tìm kiếm"))
        self.btnSearch.setText(_translate("Form", "Search"))
        item = self.tableLoaddingData.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))  # Assuming this is ID
        item = self.tableLoaddingData.horizontalHeaderItem(1)
        item.setText(_translate("Form", "UserName"))  # Assuming this is UserName
        item = self.tableLoaddingData.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Type"))  # Assuming this is Type
        self.btnAdd.setText(_translate("Form", "Add"))
        self.btnEdit.setText(_translate("Form", "Edit"))
        self.btnDelete.setText(_translate("Form", "Delete"))
        self.btnClose.setText(_translate("Form", "Close"))

    def openAddMemberForm(self):
        self.addMemberForm = QtWidgets.QWidget()
        self.ui_add_member = FormAddMember()
        self.ui_add_member.setupUi(self.addMemberForm)
        self.addMemberForm.show()

    def openEditMemberForm(self):
        self.editMemberForm = QtWidgets.QWidget()
        self.ui_edit_member = FormEditMember()
        self.ui_edit_member.setupUi(self.editMemberForm)
        self.editMemberForm.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
