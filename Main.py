import sys
import queue
import multiprocessing
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from MainWindow import Ui_MainWindow

from AddUser import AddUserWindow
from SettingSub import SettingSubWindow
from UpdatePassword import UpdatePasswordWindow

from RunningSub import RunningSubWindow

from DBDriver import DBDriver


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    主界面，负责显示和导航至各功能界面
    """

    def __init__(self):
        """
        初始化函数
        """
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.db_driver = None

        self.labelCurrentUser = QLabel(self)  # 当前登录用户，在底部状态栏中显示
        self.setup_statusbar()  # 装载主界面底部状态栏

        self.stack_running = RunningSubWindow()
        self.stack_setting = SettingSubWindow()
        self.stackedWidget.addWidget(self.stack_running)
        self.stackedWidget.addWidget(self.stack_setting)
        self.stackedWidget.setCurrentIndex(0)

        self.add_user_window = AddUserWindow()  # 添加用户界面
        self.update_password_window = UpdatePasswordWindow()  # 更新密码界面

        self.actionAddUser.triggered.connect(self.add_user_window.show)  # 添加用户菜单
        self.actionUpdatePassword.triggered.connect(self.update_password_window.show)  # 更新密码菜单

        self.actionRunning.triggered.connect(self.show_stack_running)  # 显示运行程序界面
        self.actionSetting.triggered.connect(self.show_stack_setting)  # 显示参数设置界面

    def show_stack_running(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_stack_setting(self):
        self.stackedWidget.setCurrentIndex(1)

    def setup_statusbar(self):
        """
        装载主界面底部状态栏
        Returns:

        """
        labelCurrentUserTag = QLabel(self)
        labelCurrentUserTag.setText("当前登录用户：")

        # 在主界面底部状态栏从左至右依次挂载两个label，
        # 例如：当前登录用户：admin
        self.statusbar.addWidget(labelCurrentUserTag)
        self.statusbar.addWidget(self.labelCurrentUser)

    def set_username(self, username):
        """
        设置当前登录用户的用户名
        Args:
            username: 用户名

        Returns:

        """
        self.username = username
        self.labelCurrentUser.setText(username)

        # 在更新密码界面中设置username，因为更新密码界面中更新密码时需要根据用户名查询旧密码和设置新密码
        self.update_password_window.set_username(self.username)

    def set_db_driver(self, db_driver):
        """
        设置sqlite数据库驱动
        Args:
            db_driver: sqlite数据库驱动

        Returns:

        """
        self.db_driver = db_driver

        # 在添加用户界面和更新密码界面中设置sqlite数据库驱动，因为这两个界面均涉及数据库操作
        self.add_user_window.set_db_driver(db_driver)
        self.update_password_window.set_db_driver(db_driver)
        self.stack_setting.set_db_driver(db_driver)
        self.stack_running.set_db_driver(db_driver)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    db_driver = DBDriver("project")  # 新建sqlite数据库驱动
    main_window.set_db_driver(db_driver)  # 在主窗口程序中安装sqlite数据库驱动
    main_window.show()
    sys.exit(app.exec_())
