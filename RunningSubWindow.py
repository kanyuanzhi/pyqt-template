# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RunningSubWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RunningSubWindow(object):
    def setupUi(self, RunningSubWindow):
        RunningSubWindow.setObjectName("RunningSubWindow")
        RunningSubWindow.resize(801, 571)
        self.groupBox = QtWidgets.QGroupBox(RunningSubWindow)
        self.groupBox.setGeometry(QtCore.QRect(20, 370, 141, 171))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.pushButtonLoadSetting = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonLoadSetting.setGeometry(QtCore.QRect(0, 30, 141, 32))
        self.pushButtonLoadSetting.setObjectName("pushButtonLoadSetting")
        self.labelLoadedSetting = QtWidgets.QLabel(self.groupBox)
        self.labelLoadedSetting.setGeometry(QtCore.QRect(10, 60, 119, 21))
        self.labelLoadedSetting.setObjectName("labelLoadedSetting")
        self.pushButtonStart = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonStart.setGeometry(QtCore.QRect(0, 130, 141, 32))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.pushButtonStart_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonStart_2.setGeometry(QtCore.QRect(0, 90, 141, 32))
        self.pushButtonStart_2.setObjectName("pushButtonStart_2")
        self.groupBox_2 = QtWidgets.QGroupBox(RunningSubWindow)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 370, 421, 171))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_progress = QtWidgets.QLabel(self.groupBox_2)
        self.label_progress.setGeometry(QtCore.QRect(370, 140, 41, 21))
        self.label_progress.setObjectName("label_progress")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(80, 140, 271, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 60, 21))
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 60, 231, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
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
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.groupBox_3 = QtWidgets.QGroupBox(RunningSubWindow)
        self.groupBox_3.setGeometry(QtCore.QRect(640, 370, 141, 171))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 141, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(4)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.groupBox_4 = QtWidgets.QGroupBox(RunningSubWindow)
        self.groupBox_4.setGeometry(QtCore.QRect(19, 9, 761, 351))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(0, 30, 761, 331))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(RunningSubWindow)
        QtCore.QMetaObject.connectSlotsByName(RunningSubWindow)

    def retranslateUi(self, RunningSubWindow):
        _translate = QtCore.QCoreApplication.translate
        RunningSubWindow.setWindowTitle(_translate("RunningSubWindow", "Form"))
        self.groupBox.setTitle(_translate("RunningSubWindow", "????????????"))
        self.pushButtonLoadSetting.setText(_translate("RunningSubWindow", "????????????"))
        self.labelLoadedSetting.setText(_translate("RunningSubWindow", "????????????"))
        self.pushButtonStart.setText(_translate("RunningSubWindow", "????????????"))
        self.pushButtonStart_2.setText(_translate("RunningSubWindow", "????????????"))
        self.groupBox_2.setTitle(_translate("RunningSubWindow", "????????????"))
        self.label_progress.setText(_translate("RunningSubWindow", "0%"))
        self.label_2.setText(_translate("RunningSubWindow", "???????????????"))
        self.label_4.setText(_translate("RunningSubWindow", "????????????"))
        self.label_3.setText(_translate("RunningSubWindow", "???????????????"))
        self.groupBox_3.setTitle(_translate("RunningSubWindow", "????????????"))
        self.groupBox_4.setTitle(_translate("RunningSubWindow", "????????????"))
