import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal

from UpdateSettingNameWindow import Ui_UpdateSettingNameWindow

from DBDriver import DBDriver


class UpdateSettingNameWindow(QMainWindow, Ui_UpdateSettingNameWindow):
    """
    修改参数类型名称子界面
    """
    new_name = pyqtSignal(str)  # 新的参数类型名称组成的信号

    def __init__(self):
        super(UpdateSettingNameWindow, self).__init__()
        self.setupUi(self)
        self.db_driver = None

        self.current_name = ""

        self.pushButtonConfirm.clicked.connect(self.update_setting_name)
        self.pushButtonCancel.clicked.connect(self.close)

    def update_setting_name(self):
        new_name = self.lineEditUpdatedName.text().replace(" ", "")
        if new_name == "":
            QMessageBox.critical(self, "修改参数名称", "参数类型名称不能为空！")
        elif self.db_driver.is_setting_name_exist(new_name):
            QMessageBox.critical(self, "修改参数名称", "该参数类型名称已存在！")
        else:
            pass
            self.db_driver.update_setting_name(new_name, self.current_name)  # 在数据库中更新参数类型名称
            QMessageBox.information(self, "修改参数名称", "参数名称已修改！")
            self.new_name.emit(new_name)  # 数据库修改完毕后发出信号
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
