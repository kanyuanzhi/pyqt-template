import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from Main import MainWindow

from utils.window_utils import quit_window

from LoginWindow import Ui_LoginWindow

from DBDriver import DBDriver


class LoginWindow(QMainWindow, Ui_LoginWindow):
    """
    登录子界面
    """
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.main_window = MainWindow()
        self.username = ""
        self.password = ""
        self.db_driver = None
        self.loginButton.clicked.connect(self.authenticate)
        self.quitButton.clicked.connect(quit_window)

    def authenticate(self):
        self.username = self.lineEditUsername.text()
        self.password = self.lineEditPassword.text()
        success, message = self.db_driver.authenticate(self.username, self.password)
        if success:
            self.main_window.set_username(self.username)
            self.main_window.set_db_driver(self.db_driver)
            self.main_window.show()
            self.close()
        else:
            QMessageBox.critical(self, "用户登录", message)

    def set_db_driver(self, db_driver):
        self.db_driver = db_driver
        self.main_window.set_db_driver(db_driver)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    db_driver = DBDriver("project")
    login_window.set_db_driver(db_driver)
    login_window.show()
    sys.exit(app.exec_())
