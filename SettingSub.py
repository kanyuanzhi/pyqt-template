import multiprocessing
import queue
import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import QThread, pyqtSignal

from SettingSubWindow import Ui_SettingSubWindow

from DBDriver import DBDriver


class SettingSubWindow(QWidget, Ui_SettingSubWindow):
    def __init__(self):
        super(SettingSubWindow, self).__init__()
        self.setupUi(self)
        self.db_driver = None  # 数据库实例，负责各种增删改查操作


    def set_db_driver(self, db_driver):
        """
        设置sqlite数据库驱动
        Args:
            db_driver: sqlite数据库驱动

        Returns:

        """
        self.db_driver = db_driver


if __name__ == "__main__":
    app = QApplication(sys.argv)
    setting_sub_window = SettingSubWindow()
    db_driver = DBDriver("project")  # 新建sqlite数据库驱动
    setting_sub_window.set_db_driver(db_driver)  # 在参数设置子窗口程序中安装sqlite数据库驱动
    setting_sub_window.show()
    sys.exit(app.exec_())
