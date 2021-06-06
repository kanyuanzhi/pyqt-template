import copy
import multiprocessing
import queue
import sys
import time
from functools import wraps

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QButtonGroup
from PyQt5.QtCore import QThread, pyqtSignal

from SettingSubWindow import Ui_SettingSubWindow

from DBDriver import DBDriver


class SettingSubWindow(QWidget, Ui_SettingSubWindow):
    def __init__(self):
        super(SettingSubWindow, self).__init__()
        self.setupUi(self)
        self.db_driver = DBDriver("project")  # 数据库实例，负责各种增删改查操作
        self.original_settings = {}
        self.updated_settings = {}

        self.buttonGroupPara3 = QButtonGroup(self)
        self.buttonGroupPara3.addButton(self.InputPara3True, 1)
        self.buttonGroupPara3.addButton(self.InputPara3False, 2)

        self.buttonGroupPara4 = QButtonGroup(self)
        self.buttonGroupPara4.addButton(self.InputPara4Algo1, 1)
        self.buttonGroupPara4.addButton(self.InputPara4Algo2, 2)
        self.buttonGroupPara4.addButton(self.InputPara4Algo3, 3)

        self.reset_settings()

        self.comboBox.activated.connect(self.combo_box_select_handle)
        self.pushButtonSaveCurrent.clicked.connect(self.save_current)
        self.pushButtoSaveAll.clicked.connect(self.save_all)
        self.pushButtonCancelCurrent.clicked.connect(self.cancel_current)
        self.pushButtonCancelAll.clicked.connect(self.cancel_all)

        self.InputPara1.valueChanged.connect(self.para1_changed_handle)
        self.InputPara2.valueChanged.connect(self.para2_changed_handle)
        self.buttonGroupPara3.buttonClicked.connect(self.para3_changed_handle)
        self.buttonGroupPara4.buttonClicked.connect(self.para4_changed_handle)

    def reset_settings(self):
        self.original_settings = self.db_driver.get_all_settings()
        self.updated_settings = copy.deepcopy(self.original_settings)
        self.comboBox.clear()
        for key in self.original_settings:
            self.comboBox.addItem(key)
        print(self.original_settings)
        self.combo_box_select_handle()

    def set_input_group_value(self, para1, para2, para3, para4):
        self.InputPara1.setValue(para1)
        self.InputPara2.setValue(para2)
        self.buttonGroupPara3.button(para3).setChecked(True)
        self.buttonGroupPara4.button(para4).setChecked(True)

    def combo_box_select_handle(self):
        para1 = self.updated_settings[self.comboBox.currentText()]["para1"]
        para2 = self.updated_settings[self.comboBox.currentText()]["para2"]
        para3 = self.updated_settings[self.comboBox.currentText()]["para3"]
        para4 = self.updated_settings[self.comboBox.currentText()]["para4"]
        self.set_input_group_value(para1, para2, para3, para4)

    def para_changed_wrapper(para_changed_handle):
        @wraps(para_changed_handle)
        def wrapper(self):
            para_name, para_value = para_changed_handle(self)
            name = self.comboBox.currentText()
            self.updated_settings[name][para_name] = para_value

        return wrapper

    @para_changed_wrapper
    def para1_changed_handle(self):
        para_name = "para1"
        para_value = self.InputPara1.value()
        return para_name, para_value

    @para_changed_wrapper
    def para2_changed_handle(self):
        para_name = "para2"
        para_value = self.InputPara2.value()
        return para_name, para_value

    @para_changed_wrapper
    def para3_changed_handle(self):
        para_name = "para3"
        para_value = self.buttonGroupPara3.checkedId()
        return para_name, para_value

    @para_changed_wrapper
    def para4_changed_handle(self):
        para_name = "para4"
        para_value = self.buttonGroupPara4.checkedId()
        return para_name, para_value

    def save_current(self):
        name = self.comboBox.currentText()
        para1 = self.updated_settings[name]["para1"]
        para2 = self.updated_settings[name]["para2"]
        para3 = self.updated_settings[name]["para3"]
        para4 = self.updated_settings[name]["para4"]
        # "para1", "para2", "para3", "para4", "name" 顺序不能错
        updated_setting = [para1, para2, para3, para4, name]
        db_driver.update_one_setting(updated_setting)
        self.original_settings = copy.deepcopy(self.updated_settings)
        QMessageBox.critical(self, "参数设置", "已保存当前{}修改！".format(name))

    def save_all(self):
        # updated_settings格式：[[para1, para2, para3, name], [para1, para2, para3, name], ... ]
        updated_settings = []
        for name in self.updated_settings:
            para1 = self.updated_settings[name]["para1"]
            para2 = self.updated_settings[name]["para2"]
            para3 = self.updated_settings[name]["para3"]
            para4 = self.updated_settings[name]["para4"]
            updated_setting = [para1, para2, para3, para4, name]
            updated_settings.append(updated_setting)
        self.db_driver.update_all_settings(updated_settings)
        self.original_settings = copy.deepcopy(self.updated_settings)
        QMessageBox.critical(self, "参数设置", "已保存所有修改！")

    def cancel_current(self):
        reply = QMessageBox.question(self, "参数设置", "都否取消当前修改？", QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            name = self.comboBox.currentText()
            para1 = self.original_settings[name]["para1"]
            para2 = self.original_settings[name]["para2"]
            para3 = self.original_settings[name]["para3"]
            para4 = self.original_settings[name]["para4"]
            self.updated_settings[name] = copy.deepcopy(self.original_settings[name])
            self.set_input_group_value(para1, para2, para3, para4)
            QMessageBox.critical(self, "参数设置", "已取消当前{}的修改！".format(name))

    def cancel_all(self):
        reply = QMessageBox.question(self, "参数设置", "都否取消所有修改？", QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            name = self.comboBox.currentText()
            para1 = self.original_settings[name]["para1"]
            para2 = self.original_settings[name]["para2"]
            para3 = self.original_settings[name]["para3"]
            para4 = self.original_settings[name]["para4"]
            self.updated_settings = copy.deepcopy(self.original_settings)
            self.set_input_group_value(para1, para2, para3, para4)
            QMessageBox.critical(self, "参数设置", "已取消修改！")

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
