# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadSettingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadSettingWindow(object):
    def setupUi(self, LoadSettingWindow):
        LoadSettingWindow.setObjectName("LoadSettingWindow")
        LoadSettingWindow.resize(426, 199)
        self.horizontalLayoutWidget = QtWidgets.QWidget(LoadSettingWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 150, 228, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonConfirm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.horizontalLayout.addWidget(self.pushButtonConfirm)
        self.pushButtonCancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(LoadSettingWindow)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 40, 251, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_2.addWidget(self.label_1)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)

        self.retranslateUi(LoadSettingWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadSettingWindow)

    def retranslateUi(self, LoadSettingWindow):
        _translate = QtCore.QCoreApplication.translate
        LoadSettingWindow.setWindowTitle(_translate("LoadSettingWindow", "加载参数界面"))
        self.pushButtonConfirm.setText(_translate("LoadSettingWindow", "确定"))
        self.pushButtonCancel.setText(_translate("LoadSettingWindow", "取消"))
        self.label_1.setText(_translate("LoadSettingWindow", "请选择参数类型："))
