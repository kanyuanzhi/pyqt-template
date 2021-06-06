import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from AddSettingWindow import Ui_AddSettingWindow

from DBDriver import DBDriver


class AddSettingWindow(QMainWindow, Ui_AddSettingWindow):
    def __init__(self):
        super(AddSettingWindow, self).__init__()
        self.setupUi(self)
        self.db_driver = None

        self.setting_sub_window = None

        self.pushButtonConfirm.clicked.connect(self.add_setting_name)
        self.pushButtonCancel.clicked.connect(self.close)

    def add_setting_name(self):
        name = self.lineEditName.text()
        if self.db_driver.is_setting_name_exist(name):
            QMessageBox.critical(self, "添加新的参数名称", "该参数类型名称已存在！")
        else:
            default_values = self.db_driver.insert_setting(name)
            QMessageBox.information(self, "添加新的参数名称", "新参数类型已创建，请在界面左侧进行参数设置！")
            self.setting_sub_window.append_setting_in_combo(name, default_values)
            self.close()

    def set_db_driver(self, db_driver):
        self.db_driver = db_driver


if __name__ == "__main__":
    app = QApplication(sys.argv)
    add_setting_window = AddSettingWindow()
    db_driver = DBDriver("project")
    add_setting_window.set_db_driver(db_driver)
    add_setting_window.show()
    sys.exit(app.exec_())
