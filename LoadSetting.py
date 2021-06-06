import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal

from LoadSettingWindow import Ui_LoadSettingWindow

from DBDriver import DBDriver


class LoadSettingWindow(QMainWindow, Ui_LoadSettingWindow):
    setting = pyqtSignal(dict)

    def __init__(self):
        super(LoadSettingWindow, self).__init__()
        self.setupUi(self)
        self.db_driver = None
        self.settings = {}

        self.pushButtonConfirm.clicked.connect(self.confirm_selection)
        self.pushButtonCancel.clicked.connect(self.close)

    def init_data(self):
        self.settings = self.db_driver.get_all_settings()
        self.comboBox.clear()
        for key in self.settings:
            self.comboBox.addItem(key)

    def confirm_selection(self):
        name = self.comboBox.currentText()
        self.setting.emit(self.settings[name])
        self.close()

    def set_db_driver(self, db_driver):
        self.db_driver = db_driver


if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_setting_window = LoadSettingWindow()
    db_driver = DBDriver("project")
    load_setting_window.set_db_driver(db_driver)
    load_setting_window.init_data()
    load_setting_window.show()
    sys.exit(app.exec_())
