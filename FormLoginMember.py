# Trong file Ui_LoginWindow.py
from PyQt6 import QtCore, QtGui, QtWidgets
from Member import Member  # Import Member class
from PyQt6.QtWidgets import QMessageBox

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow, main_window_login_callback):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 100, 20))
        self.label.setObjectName("label")
        self.label.setText("Username:")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 100, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Password:")

        self.usernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLineEdit.setGeometry(QtCore.QRect(150, 50, 200, 20))
        self.usernameLineEdit.setObjectName("usernameLineEdit")

        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setGeometry(QtCore.QRect(150, 100, 200, 20))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(150, 150, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setText("Login")

        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(250, 150, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.setText("Cancel")

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        # Connect buttons to methods
        self.loginButton.clicked.connect(lambda: self.login(LoginWindow, main_window_login_callback))
        self.cancelButton.clicked.connect(LoginWindow.close)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        self.label.setText(_translate("LoginWindow", "Username:"))
        self.label_2.setText(_translate("LoginWindow", "Password:"))

    def login(self, LoginWindow, main_window_login_callback):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()

        # Create a Member object with username and password
        member = Member(username, password)

        # Try to log in
        if member.login():
            msg = QMessageBox()
            msg.setWindowTitle("Login Successful")
            msg.setText("Logged in as member")
            msg.exec()
            main_window_login_callback(False)  # Pass False for member login
            LoginWindow.close()  # Close the login form after successful login
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Login Failed")
            msg.setText("Login failed")
            msg.exec()

