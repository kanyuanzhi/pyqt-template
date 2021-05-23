import sys

from PyQt5.QtCore import QThread, pyqtSignal, QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from main import MainWindow
from addUser import AddUserWindow

from db_utils import connect_database
from window_utils import quit_window

from LoginWindow import Ui_LoginWindow


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.main_window = MainWindow()
        self.username = ""
        self.password = ""
        self.conn = connect_database()
        self.loginButton.clicked.connect(self.authenticate)
        self.quitButton.clicked.connect(quit_window)

    def authenticate(self):
        self.username = self.lineEditUsername.text()
        self.password = self.lineEditPassword.text()
        sql = "SELECT password FROM user WHERE username='{}'".format(self.username)
        cursor = self.conn.execute(sql)
        for row in cursor:
            password = row[0]
            if password == self.password:
                self.main_window.show()
                self.close()
            else:
                QMessageBox.critical(self, "登录失败", "密码错误！")
            cursor.close()
            self.conn.close()
            return
        QMessageBox.critical(self, "登录失败", "用户名错误！")
        self.conn.close()
        cursor.close()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
