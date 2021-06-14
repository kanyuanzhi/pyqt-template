import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from AddUserWindow import Ui_AddUserWindow

from DBDriver import DBDriver


class AddUserWindow(QMainWindow, Ui_AddUserWindow):
    """
    添加用户子界面
    """
    def __init__(self):
        super(AddUserWindow, self).__init__()
        self.setupUi(self)
        self.username = ""
        self.password = ""
        self.confirm_password = ""
        self.db_driver = None
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
            if self.db_driver.is_username_exist(self.username):
                QMessageBox.critical(self, "添加错误", "用户名已被注册！")
                return
            else:
                self.db_driver.insert_user(self.username, self.password)
                QMessageBox.information(self, "添加成功", "添加用户成功！")
                self.close()
                return

    def set_db_driver(self, db_driver):
        self.db_driver = db_driver


if __name__ == "__main__":
    app = QApplication(sys.argv)
    add_user_window = AddUserWindow()
    db_driver = DBDriver("project")
    add_user_window.set_db_driver(db_driver)
    add_user_window.show()
    sys.exit(app.exec_())
