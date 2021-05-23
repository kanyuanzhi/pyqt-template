# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 131, 171))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 131, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 380, 391, 171))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 50, 231, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textBrowserCurrentResult = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowserCurrentResult.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserCurrentResult.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserCurrentResult.setAcceptRichText(True)
        self.textBrowserCurrentResult.setObjectName("textBrowserCurrentResult")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textBrowserCurrentResult)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textBrowserTotalResult = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowserTotalResult.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserTotalResult.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserTotalResult.setObjectName("textBrowserTotalResult")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textBrowserTotalResult)
        self.label_progress = QtWidgets.QLabel(self.groupBox_2)
        self.label_progress.setGeometry(QtCore.QRect(350, 140, 41, 21))
        self.label_progress.setObjectName("label_progress")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(80, 140, 251, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 60, 21))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 490, 131, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_current_user = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_current_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_user.setObjectName("label_current_user")
        self.verticalLayout_2.addWidget(self.label_current_user)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAddUser = QtWidgets.QAction(MainWindow)
        self.actionAddUser.setObjectName("actionAddUser")
        self.actionUpdatePassword = QtWidgets.QAction(MainWindow)
        self.actionUpdatePassword.setObjectName("actionUpdatePassword")
        self.menu.addAction(self.actionAddUser)
        self.menu.addAction(self.actionUpdatePassword)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "基本操作"))
        self.pushButton_2.setText(_translate("MainWindow", "参数设置"))
        self.pushButton.setText(_translate("MainWindow", "开始运行"))
        self.groupBox_2.setTitle(_translate("MainWindow", "运行结果"))
        self.label_3.setText(_translate("MainWindow", "当前结果："))
        self.label_4.setText(_translate("MainWindow", "总结果："))
        self.label_progress.setText(_translate("MainWindow", "0%"))
        self.label_2.setText(_translate("MainWindow", "处理进度："))
        self.label.setText(_translate("MainWindow", "当前登录用户："))
        self.label_current_user.setText(_translate("MainWindow", "用户名"))
        self.menu.setTitle(_translate("MainWindow", "用户管理"))
        self.actionAddUser.setText(_translate("MainWindow", "添加用户"))
        self.actionUpdatePassword.setText(_translate("MainWindow", "修改密码"))
