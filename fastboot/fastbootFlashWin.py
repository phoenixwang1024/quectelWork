# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fastbootFlash.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

class Ui_FastbootFlash(object):
    def setupUi(self, FastbootFlash):
        FastbootFlash.setObjectName("FastbootFlash")
        FastbootFlash.resize(370, 342)
        self.centralwidget = QtWidgets.QWidget(FastbootFlash)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 40, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 40, 231, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 90, 331, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 240, 91, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 54, 12))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 270, 221, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 240, 185, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        FastbootFlash.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FastbootFlash)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 23))
        self.menubar.setObjectName("menubar")
        FastbootFlash.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FastbootFlash)
        self.statusbar.setObjectName("statusbar")
        FastbootFlash.setStatusBar(self.statusbar)

        self.retranslateUi(FastbootFlash)
        QtCore.QMetaObject.connectSlotsByName(FastbootFlash)

    def retranslateUi(self, FastbootFlash):
        _translate = QtCore.QCoreApplication.translate
        FastbootFlash.setWindowTitle(_translate("FastbootFlash", "FastbootFlash"))
        self.pushButton.setText(_translate("FastbootFlash", "Update文件1"))
        self.pushButton_2.setText(_translate("FastbootFlash", "Update文件1"))
        self.pushButton_5.setText(_translate("FastbootFlash", "开始"))
        self.label.setText(_translate("FastbootFlash", "log"))
        self.label_2.setText(_translate("FastbootFlash", "升级次数："))
        self.checkBox.setText(_translate("FastbootFlash", "自动升级"))



