import sys

from PyQt5.QtCore import QThread, pyqtSignal, QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from Main import MainWindow
from AddUser import AddUserWindow

import db_utils
from window_utils import quit_window

from LoginWindow import Ui_LoginWindow


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.main_window = MainWindow()
        self.username = ""
        self.password = ""
        self.conn = db_utils.connect_database()
        self.loginButton.clicked.connect(self.authenticate)
        self.quitButton.clicked.connect(quit_window)

    def authenticate(self):
        self.username = self.lineEditUsername.text()
        self.password = self.lineEditPassword.text()
        success, message = db_utils.authenticate(self.conn, self.username, self.password)
        if success:
            self.main_window.set_username(self.username)
            self.main_window.show()
            self.close()
        else:
            QMessageBox.critical(self, "用户登录", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
