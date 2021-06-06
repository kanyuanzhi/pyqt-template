import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from UpdateSettingNameWindow import Ui_UpdateSettingNameWindow

from DBDriver import DBDriver


class UpdateSettingNameWindow(QMainWindow, Ui_UpdateSettingNameWindow):
    def __init__(self):
        super(UpdateSettingNameWindow, self).__init__()
        self.setupUi(self)
        self.db_driver = None

        self.setting_sub_window = None
        self.current_name = ""

        self.pushButtonConfirm.clicked.connect(self.update_setting_name)
        self.pushButtonCancel.clicked.connect(self.close)

    def update_setting_name(self):
        new_name = self.lineEditUpdatedName.text()
        if self.db_driver.is_setting_name_exist(new_name):
            QMessageBox.critical(self, "修改参数名称", "该参数类型名称已存在！")
        else:
            pass
            self.db_driver.update_setting_name(new_name, self.current_name)
            QMessageBox.information(self, "修改参数名称", "参数名称已修改！")
            self.setting_sub_window.update_setting_in_combo(new_name)
            self.close()

    def set_db_driver(self, db_driver):
        self.db_driver = db_driver

    def set_current_name(self, name):
        self.current_name = name
        self.labelCurrentName.setText(name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    udpate_setting_name_window = UpdateSettingNameWindow()
    db_driver = DBDriver("project")
    udpate_setting_name_window.set_db_driver(db_driver)
    udpate_setting_name_window.show()
    sys.exit(app.exec_())
