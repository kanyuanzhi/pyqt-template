import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from utils import db_utils

from UpdatePasswordWindow import Ui_UpdatePasswordWindow


class UpdatePasswordWindow(QMainWindow, Ui_UpdatePasswordWindow):
    def __init__(self):
        super(UpdatePasswordWindow, self).__init__()
        self.setupUi(self)
        self.username = ""
        self.old_password = ""
        self.new_password = ""
        self.confirm_new_password = ""
        self.conn = db_utils.connect_database()
        self.cancelButton.clicked.connect(self.close)
        self.confirmButton.clicked.connect(self.update_password)

    def update_password(self):
        self.old_password = self.lineEditOldPassword.text().replace(" ", "")  # 去掉空格
        self.new_password = self.lineEditNewPassword.text().replace(" ", "")
        self.confirm_new_password = self.lineEditConfirmNewPassword.text().replace(" ", "")
        success, message = db_utils.authenticate(self.conn, self.username, self.old_password)
        if not success:
            QMessageBox.critical(self, "更新密码", message)
            return
        if self.new_password == "":
            QMessageBox.critical(self, "更新密码", "新密码不能为空！")
            return
        if self.new_password != self.confirm_new_password:
            QMessageBox.critical(self, "更新密码", "两次输入密码不一致！")
            return
        db_utils.update(self.conn, "password", self.new_password, "username", self.username)
        QMessageBox.information(self, "更新密码", "更新密码成功！")
        self.close()
        return

    def set_username(self, username):
        self.username = username


if __name__ == "__main__":
    app = QApplication(sys.argv)
    update_password_window = UpdatePasswordWindow()
    update_password_window.show()
    sys.exit(app.exec_())
