from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication


def messageDialog():
    msg_box = QMessageBox(QMessageBox.Warning, "成功", "添加用户成功")
    msg_box.exec_()

def quit_window():
    QCoreApplication.quit()