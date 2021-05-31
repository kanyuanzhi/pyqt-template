from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication


def messageDialog():
    """
    操作提示框
    封装了QMessageBox的功能
    Returns:

    """
    msg_box = QMessageBox(QMessageBox.Warning, "成功", "添加用户成功")
    msg_box.exec_()


def quit_window():
    """
    退出程序
    Returns:

    """
    QCoreApplication.quit()
