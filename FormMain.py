from PyQt6 import QtCore, QtGui, QtWidgets
from FormLogin import Ui_LoginWindow
from FormRegisterMember import Ui_FormRegisterMember
from FormLoginMember import Ui_LoginWindow as Ui_FormLoginMember
from FormMember import Ui_Form as FormMember

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 762)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Define button geometries and positions
        button_width = 181
        button_height = 32
        button_x = 620
        button_y_admin_login = 230
        button_y_member_login = 270

        # Create buttons
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(button_x, 320, button_width, button_height))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(button_x, button_y_admin_login, button_width, button_height))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_member_login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_member_login.setGeometry(
            QtCore.QRect(button_x, button_y_member_login, button_width, button_height))
        self.pushButton_member_login.setObjectName("pushButton_member_login")

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(button_x, 370, button_width, button_height))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(button_x, 410, button_width, button_height))
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Initialize IS_ADMIN and IS_MEMBER_LOGGED_IN
        self.IS_ADMIN = False
        self.IS_MEMBER_LOGGED_IN = False

        # Open admin login form
        self.pushButton_2.clicked.connect(self.openAdminLoginForm)

        # Open register member form
        self.pushButton.clicked.connect(self.openFormRegisterMember)

        # Hide "Manage Member" button initially
        self.pushButton_4.hide()

        # Connect logout button
        self.pushButton_5.clicked.connect(self.logout)

        # Connect member login button
        self.pushButton_member_login.clicked.connect(self.openMemberLoginForm)

        # Connect manage member button
        self.pushButton_4.clicked.connect(self.openManageMembersForm)

    def openAdminLoginForm(self):
        self.loginWindow = QtWidgets.QMainWindow()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self.loginWindow)

        # Connect login_successful signal from Ui_LoginWindow to handleLogin method
        self.ui.login_successful.connect(self.handleLogin)

        self.loginWindow.show()

    def handleLogin(self, is_admin):
        self.IS_ADMIN = is_admin

        # Update "Manage Member" button visibility
        if self.IS_ADMIN:
            self.pushButton_4.show()
        else:
            self.pushButton_4.hide()

        if not self.IS_ADMIN:
            self.IS_MEMBER_LOGGED_IN = True
        else:
            self.IS_MEMBER_LOGGED_IN = False

    def openFormRegisterMember(self):
        self.formRegisterMember = QtWidgets.QMainWindow()
        self.ui = Ui_FormRegisterMember()
        self.ui.setupUi(self.formRegisterMember)
        self.formRegisterMember.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Register Member"))
        self.pushButton_2.setText(_translate("MainWindow", "Login admin"))
        self.pushButton_member_login.setText(_translate("MainWindow", "Member Login"))
        self.pushButton_4.setText(_translate("MainWindow", "Manage Member"))
        self.pushButton_5.setText(_translate("MainWindow", "Logout"))

    def logout(self):
        if self.IS_ADMIN:
            self.IS_ADMIN = False
            self.pushButton_4.hide()
            QtWidgets.QMessageBox.information(None, "Thông báo", "Đăng xuất admin thành công.")
        elif self.IS_MEMBER_LOGGED_IN:
            self.IS_MEMBER_LOGGED_IN = False
            QtWidgets.QMessageBox.information(None, "Thông báo", "Đăng xuất thành viên thành công.")
        else:
            QtWidgets.QMessageBox.warning(None, "Thông báo", "Bạn chưa đăng nhập.")

    def openMemberLoginForm(self):
        self.memberLoginWindow = QtWidgets.QMainWindow()
        self.ui_member_login = Ui_FormLoginMember()
        self.ui_member_login.setupUi(self.memberLoginWindow, self.handleLogin)  # Pass the login callback
        self.memberLoginWindow.show()

    def openManageMembersForm(self):
        self.manageMembersForm = QtWidgets.QWidget()
        self.ui_manage_members = FormMember()
        self.ui_manage_members.setupUi(self.manageMembersForm)
        self.manageMembersForm.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
