from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from DbManager import DbManager
from Member import Member

class Ui_FormRegisterMember(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 762)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 260, 141, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 310, 141, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 350, 141, 16))
        self.label_3.setObjectName("label_3")

        self.username_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.username_edit.setGeometry(QtCore.QRect(680, 250, 271, 31))
        self.username_edit.setObjectName("username_edit")

        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(680, 300, 271, 31))
        self.password_edit.setObjectName("password_edit")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Set password echo mode

        self.confirm_password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_password_edit.setGeometry(QtCore.QRect(680, 340, 271, 31))
        self.confirm_password_edit.setObjectName("confirm_password_edit")
        self.confirm_password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Set password echo mode

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 410, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 410, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Kết nối nút "Đăng ký" với phương thức đăng ký thành viên
        self.pushButton.clicked.connect(self.registerMember)

        # Kết nối nút "Hủy" để đóng cửa sổ
        self.pushButton_2.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Đăng ký"))
        self.pushButton_2.setText(_translate("MainWindow", "Hủy"))
        self.label.setText(_translate("MainWindow", "Tên đăng nhập"))
        self.label_2.setText(_translate("MainWindow", "Mật khẩu"))
        self.label_3.setText(_translate("MainWindow", "Xác nhận mật khẩu"))

    def registerMember(self):
        username = self.username_edit.toPlainText()
        password = self.password_edit.text()
        confirm_password = self.confirm_password_edit.text()

        if not username or not password or not confirm_password:
            QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return

        if password != confirm_password:
            QMessageBox.warning(None, "Lỗi", "Mật khẩu không khớp.")
            return

        # Tạo một thể hiện mới của lớp Member
        member = Member(username, password)

        # Đăng ký thành viên (lưu vào cơ sở dữ liệu)
        try:
            member.register()
            QMessageBox.information(None, "Thành công", "Đăng ký thành viên thành công.")
            self.MainWindow.close()
            self.MainForm.show()
        except Exception as e:
            print()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FormRegisterMember()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
