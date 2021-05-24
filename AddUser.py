import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from utils import db_utils
from utils.db_utils import connect_database

from AddUserWindow import Ui_AddUserWindow


class AddUserWindow(QMainWindow, Ui_AddUserWindow):
    def __init__(self):
        super(AddUserWindow, self).__init__()
        self.setupUi(self)
        self.username = ""
        self.password = ""
        self.confirm_password = ""
        self.conn = connect_database()
        self.cancelButton.clicked.connect(self.close)
        self.confirmButton.clicked.connect(self.add_user)

    def add_user(self):
        self.username = self.lineEditUsername.text().replace(" ", "")  # 去掉空格
        self.password = self.lineEditPassword.text().replace(" ", "")
        self.confirm_password = self.lineEditConfirmPassword.text().replace(" ", "")
        if self.password == "":
            QMessageBox.critical(self, "添加错误", "密码不能为空！")
            return
        elif self.password != self.confirm_password:
            QMessageBox.critical(self, "添加错误", "两次输入密码不一致！")
            return
        elif self.username == "":
            QMessageBox.critical(self, "添加错误", "用户名不能为空！")
            return
        else:
            if db_utils.is_username_exist(self.conn, self.username):
                QMessageBox.critical(self, "添加错误", "用户名已被注册！")
                return
            else:
                db_utils.insert_user(self.conn, self.username, self.password)
                QMessageBox.information(self, "添加成功", "添加用户成功！")
                self.close()
                return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    add_user_window = AddUserWindow()
    add_user_window.show()
    sys.exit(app.exec_())
