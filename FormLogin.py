# Ui_LoginWindow.py

from PyQt6 import QtCore, QtWidgets
from Admini import Admin  # Import your Admin class
from PyQt6.QtWidgets import QMessageBox

class Ui_LoginWindow(QtCore.QObject):
    login_successful = QtCore.pyqtSignal(bool)  # Declare login_successful signal

    def setupUi(self, LoginWindow):
        self.LoginWindow = LoginWindow  # Store reference to LoginWindow
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 50, 61, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 61, 16))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 100, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        # Connect buttons to methods
        self.pushButton.clicked.connect(self.emitLoginSignal)  # Login button
        self.pushButton_2.clicked.connect(LoginWindow.close)  # Close button

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login Window"))
        self.label.setText(_translate("LoginWindow", "Username"))
        self.label_2.setText(_translate("LoginWindow", "Password"))
        self.pushButton.setText(_translate("LoginWindow", "Login"))
        self.pushButton_2.setText(_translate("LoginWindow", "Cancel"))

    def emitLoginSignal(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # Create an Admin object with username and password
        admin = Admin(username, password)

        # Try to log in
        admin.login()

        if admin.is_admin:
            self.login_successful.emit(True)
            QMessageBox.information(None, "Thành công", "Đăng nhập admin thành công.")
            self.LoginWindow.close()  # Close the LoginWindow
        else:
            self.login_successful.emit(False)
            QMessageBox.warning(None, "Thất bại", "Đăng nhập admin thất bại.")
