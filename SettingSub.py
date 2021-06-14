import copy
import json
import sys

from functools import wraps

from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QButtonGroup

from AddSetting import AddSettingWindow
from SettingSubWindow import Ui_SettingSubWindow

from DBDriver import DBDriver
from UpdateSettingName import UpdateSettingNameWindow


# todo: 添加数据库中无参数类型的相关处理
class SettingSubWindow(QWidget, Ui_SettingSubWindow):
    """
    参数设置子窗口
    功能：添加、修改、删除、导出程序运行所需参数
    """

    def __init__(self):
        super(SettingSubWindow, self).__init__()
        self.setupUi(self)

        self.db_driver = None  # 数据库驱动

        self.add_setting_window = AddSettingWindow()  # "添加新参数类型"子窗口

        # 接收从"添加新参数类型"子窗口传回的name_values信号，该信号包括新参数类型名称和初始化的参数值
        self.add_setting_window.name_values.connect(self.append_setting_in_combo)

        self.update_setting_name_window = UpdateSettingNameWindow()  # "修改参数类型名称"子窗口

        # 接收从"修改参数类型名称"子窗口传回的new_name信号，该信号包括新参数类型名称
        self.update_setting_name_window.new_name.connect(self.update_setting_name_in_combo)

        self.original_settings = {}  # 原始的参数设置组成的字典，格式：
        # {"name":{
        #   "name":"",
        #   "para1":"",
        #   "para2":"",
        #   "para3":"",
        #   "para4":"",
        #   ...},
        #  "name":{...},
        #  ...}
        self.updated_settings = {}  # 更新后的参数设置组成的字典，格式同上

        # pyqt中的QButton是互斥的，同一界面中只能有一个QButton被选中，因此需要将多个QButton分为不同组
        self.buttonGroupPara3 = QButtonGroup(self)  # 参数3单选按钮组
        self.buttonGroupPara3.addButton(self.InputPara3True, 1)  # 参数3的1状态
        self.buttonGroupPara3.addButton(self.InputPara3False, 2)  # 参数3的2状态

        self.buttonGroupPara4 = QButtonGroup(self)  # 参数3单选按钮组
        self.buttonGroupPara4.addButton(self.InputPara4Algo1, 1)  # 参数4的1状态
        self.buttonGroupPara4.addButton(self.InputPara4Algo2, 2)  # 参数4的2状态
        self.buttonGroupPara4.addButton(self.InputPara4Algo3, 3)  # 参数4的3状态

        self.comboBox.activated.connect(self.combo_box_select_handle)  # 选择参数类型的下拉列表
        self.pushButtonSaveCurrent.clicked.connect(self.save_current)  # 保存当前修改按钮
        self.pushButtoSaveAll.clicked.connect(self.save_all)  # 保存所有修改按钮
        self.pushButtonCancelCurrent.clicked.connect(self.cancel_current)  # 取消当前修改按钮
        self.pushButtonCancelAll.clicked.connect(self.cancel_all)  # 取消所有修改按钮
        self.pushButtonAddSetting.clicked.connect(self.add_setting_window.show)  # 添加新参数类型按钮
        self.pushButtonUpdateName.clicked.connect(self.show_update_setting_name)  # 更新参数类型名称按钮
        self.pushButtonDeleteSetting.clicked.connect(self.remove_setting)  # 删除当前参数类型按钮
        self.pushButtonImportSettings.clicked.connect(self.import_settings)  # 导出所有参数按钮

        #  监听参数改变
        self.InputPara1.valueChanged.connect(self.para1_changed_handle)  # 参数1输入框变化
        self.InputPara2.valueChanged.connect(self.para2_changed_handle)  # 参数2输入框变化
        self.buttonGroupPara3.buttonClicked.connect(self.para3_changed_handle)  # 参数3单选按钮组变化
        self.buttonGroupPara4.buttonClicked.connect(self.para4_changed_handle)  # 参数4单选按钮组变化

    def init_settings(self):
        """
        初始化参数设置页面
        包括从数据库中读取参数、在页面中刷新显示
        Returns:

        """
        self.original_settings = self.db_driver.get_all_settings()  # 从数据库读取所有参数
        self.updated_settings = copy.deepcopy(self.original_settings)  # 深拷贝，避免修改参数时影响初始参数，供"取消所有参数修改"功能用
        self.comboBox.clear()  # 清空参数类型下拉列表
        for key in self.original_settings:  # 填补下拉列表
            self.comboBox.addItem(key)

        # 参数类型下拉列表初始化时会自动选中列表第一项，此时调用combo_box_select_handle函数完成参数输入框的填充
        self.combo_box_select_handle()

    def set_input_group_value(self, para1, para2, para3, para4):
        """
        设置参数输入框的显示值
        Args:
            para1: 参数1
            para2: 参数2
            para3: 参数3
            para4: 参数4

        Returns:

        """
        self.InputPara1.setValue(para1)
        self.InputPara2.setValue(para2)
        self.buttonGroupPara3.button(para3).setChecked(True)
        self.buttonGroupPara4.button(para4).setChecked(True)

    def combo_box_select_handle(self):
        """
        参数类型下拉列表被选中时的处理函数
        从更新后的参数中读取各参数的值，再调用set_input_group_value函数填到各参数输入框中
        Returns:

        """
        para1 = self.updated_settings[self.comboBox.currentText()]["para1"]
        para2 = self.updated_settings[self.comboBox.currentText()]["para2"]
        para3 = self.updated_settings[self.comboBox.currentText()]["para3"]
        para4 = self.updated_settings[self.comboBox.currentText()]["para4"]
        self.set_input_group_value(para1, para2, para3, para4)

    def para_changed_wrapper(para_changed_handle):
        """
        修饰器
        当参数输入框的值发生变化时，调用对应参数的槽函数，然后再经过此修饰器，修改"更新的参数设置"字典
        """

        @wraps(para_changed_handle)
        def wrapper(self):
            para_name, para_value = para_changed_handle(self)
            name = self.comboBox.currentText()
            self.updated_settings[name][para_name] = para_value

        return wrapper

    @para_changed_wrapper
    def para1_changed_handle(self):
        """
        参数1发生变化时的槽函数
        Returns:
            para_name:参数名
            para_value:参数值

        """
        para_name = "para1"
        para_value = self.InputPara1.value()
        return para_name, para_value

    @para_changed_wrapper
    def para2_changed_handle(self):
        """
        参数2发生变化时的槽函数
        Returns:
            para_name:参数名
            para_value:参数值

        """
        para_name = "para2"
        para_value = self.InputPara2.value()
        return para_name, para_value

    @para_changed_wrapper
    def para3_changed_handle(self):
        """
        参数3发生变化时的槽函数
        Returns:
            para_name:参数名
            para_value:参数值

        """
        para_name = "para3"
        para_value = self.buttonGroupPara3.checkedId()
        return para_name, para_value

    @para_changed_wrapper
    def para4_changed_handle(self):
        """
        参数4发生变化时的槽函数
        Returns:
            para_name:参数名
            para_value:参数值

        """
        para_name = "para4"
        para_value = self.buttonGroupPara4.checkedId()
        return para_name, para_value

    def save_current(self):
        """
        保存当前参数设置
        Returns:

        """
        name = self.comboBox.currentText()
        para1 = self.updated_settings[name]["para1"]
        para2 = self.updated_settings[name]["para2"]
        para3 = self.updated_settings[name]["para3"]
        para4 = self.updated_settings[name]["para4"]
        # "para1", "para2", "para3", "para4", "name" 顺序不能错
        updated_setting = [para1, para2, para3, para4, name]
        self.db_driver.update_one_setting(updated_setting)
        self.original_settings = copy.deepcopy(self.updated_settings)
        QMessageBox.critical(self, "参数设置", "已保存当前{}修改！".format(name))

    def save_all(self):
        """
        保存所有参数设置
        Returns:

        """
        # updated_settings格式：[[para1, para2, para3, name], [para1, para2, para3, name], ... ]，与self.updated_setting不同
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
        """
        取消当前参数修改
        重置当前参数输入框，并将"更新后的参数设置"字典中的当前参数类型的值恢复到"原始参数设置"字典对应参数类型的值
        Returns:

        """
        reply = QMessageBox.question(self, "参数设置", "都否取消当前修改？", QMessageBox.Yes | QMessageBox.No)
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
        """
        取消所有参数修改
        重置当前参数输入框，并将"更新后的参数设置"字典恢复到"原始参数设置"字典
        Returns:

        """
        reply = QMessageBox.question(self, "参数设置", "都否取消所有修改？", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            name = self.comboBox.currentText()
            para1 = self.original_settings[name]["para1"]
            para2 = self.original_settings[name]["para2"]
            para3 = self.original_settings[name]["para3"]
            para4 = self.original_settings[name]["para4"]
            self.updated_settings = copy.deepcopy(self.original_settings)
            self.set_input_group_value(para1, para2, para3, para4)
            QMessageBox.critical(self, "参数设置", "已取消修改！")

    def append_setting_in_combo(self, name_values):
        """
        向参数类型下拉列表中添加新的选项
        添加新的参数类型后会调用此函数
        Args:
            name_values: 从添加新参数类型子界面中接收的信号，包括新添加的参数类型名称与各参数初始化值组成的数组，
                         格式：[name, [para1_value, para2_value, ...]]

        Returns:

        """
        [name, default_values] = name_values
        self.comboBox.addItem(name)
        keys = ["para1", "para2", "para3", "para4"]
        self.original_settings[name] = dict(zip(keys, default_values))
        self.original_settings[name]["name"] = name
        self.updated_settings[name] = copy.deepcopy(self.original_settings[name])
        self.comboBox.setCurrentIndex(self.comboBox.count() - 1)  # 添加新参数类型后参数类型下拉列表自动跳转至该新增的选项
        self.set_input_group_value(*default_values)

    def show_update_setting_name(self):
        """
        显示修改参数类型名称子界面
        Returns:

        """
        self.update_setting_name_window.set_current_name(self.comboBox.currentText())  # 设置子界面中显示的当前参数名称
        self.update_setting_name_window.show()

    def update_setting_name_in_combo(self, new_name):
        """
        在参数类型下拉列表中更新修改后的参数类型名称
        Args:
            new_name: 从修改参数类型名称子界面中接收的信号，包括新的参数类型名称

        Returns:

        """
        current_name = self.comboBox.currentText()
        self.comboBox.setItemText(self.comboBox.currentIndex(), new_name)  # 在参数类型下拉列表中将原类型名称修改为新类型名称

        # 修改原始的参数设置字典与更新后的参数设置字典，以新参数名称为新键、原参数名称对应的值为新值，组成新的字典条目，再删除原有参数名称与对应的值
        self.original_settings[new_name] = copy.deepcopy(self.original_settings[current_name])
        self.original_settings.pop(current_name)
        self.updated_settings[new_name] = copy.deepcopy(self.updated_settings[current_name])
        self.updated_settings.pop(current_name)

    def remove_setting(self):
        """
        删除当前参数类型
        Returns:

        """
        reply = QMessageBox.question(self, "参数设置", "都否删除当前参数类型？", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            current_name = self.comboBox.currentText()
            self.db_driver.remove_setting(current_name)  # 在数据库中删除该参数类型
            self.init_settings()  # 重新初始化界面中的参数设置

    def import_settings(self):
        """
        导出当前参数设置
        Returns:

        """
        reply = QMessageBox.question(self, "参数设置", "导出前请确认保存已修改的配置！\n是否导出参数配置？", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            with open("settings.txt", "w") as tf:
                json.dump(self.updated_settings, tf)

    def set_db_driver(self, db_driver):
        """
        设置sqlite数据库驱动
        Args:
            db_driver: sqlite数据库驱动

        Returns:

        """
        self.db_driver = db_driver
        self.add_setting_window.set_db_driver(db_driver)
        self.update_setting_name_window.set_db_driver(db_driver)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    setting_sub_window = SettingSubWindow()
    db_driver = DBDriver("project")  # 新建sqlite数据库驱动
    setting_sub_window.set_db_driver(db_driver)  # 在参数设置子窗口程序中安装sqlite数据库驱动
    setting_sub_window.init_settings()
    setting_sub_window.show()
    sys.exit(app.exec_())
