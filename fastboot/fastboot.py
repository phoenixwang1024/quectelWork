# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fastboot.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FastbootFlashMainWin(object):
    def setupUi(self, FastbootFlashMainWin):
        FastbootFlashMainWin.setObjectName("FastbootFlashMainWin")
        FastbootFlashMainWin.resize(531, 394)
        self.centralwidget = QtWidgets.QWidget(FastbootFlashMainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 231, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 130, 331, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 290, 75, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 110, 54, 12))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 281, 224, 55))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 113, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(360, 30, 156, 306))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_13 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout_2.addWidget(self.checkBox_13)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 3, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 3, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 4, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 4, 1, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 5, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 5, 1, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 6, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 6, 1, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_9.setText("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 7, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 7, 1, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_10.setText("")
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 8, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 8, 1, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_11.setText("")
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 9, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 9, 1, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_12.setText("")
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 10, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 10, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        FastbootFlashMainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FastbootFlashMainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 23))
        self.menubar.setObjectName("menubar")
        FastbootFlashMainWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FastbootFlashMainWin)
        self.statusbar.setObjectName("statusbar")
        FastbootFlashMainWin.setStatusBar(self.statusbar)

        self.retranslateUi(FastbootFlashMainWin)
        QtCore.QMetaObject.connectSlotsByName(FastbootFlashMainWin)

    def retranslateUi(self, FastbootFlashMainWin):
        _translate = QtCore.QCoreApplication.translate
        FastbootFlashMainWin.setWindowTitle(_translate("FastbootFlashMainWin", "FastbootFlashUpdate"))
        self.pushButton.setText(_translate("FastbootFlashMainWin", "文件1"))
        self.pushButton_2.setText(_translate("FastbootFlashMainWin", "文件2"))
        self.pushButton_5.setText(_translate("FastbootFlashMainWin", "开始"))
        self.label.setText(_translate("FastbootFlashMainWin", "log"))
        self.label_2.setText(_translate("FastbootFlashMainWin", "升级次数："))
        self.checkBox.setText(_translate("FastbootFlashMainWin", "自动升级"))
        self.label_6.setText(_translate("FastbootFlashMainWin", "升级："))
        self.label_3.setText(_translate("FastbootFlashMainWin", "UART1:"))
        self.checkBox_13.setText(_translate("FastbootFlashMainWin", "全选"))
