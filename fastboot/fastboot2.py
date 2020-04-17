# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fastboot2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QComboBox
from PyQt5.QtCore import pyqtSignal
import sys,os,serial,datetime,time,requests,re,subprocess,logging, threading
import xml.etree.ElementTree as ET
import serial.tools.list_ports


class Ui_FastbootFlashMainWin(object):
    def setupUi(self, FastbootFlashMainWin):
        FastbootFlashMainWin.setObjectName("FastbootFlashMainWin")
        FastbootFlashMainWin.resize(685, 422)
        self.centralwidget = QtWidgets.QWidget(FastbootFlashMainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(50, 20))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        # 改写ComboBox类，实现点击就刷新串口列表信息
        self.comboBox = ComListComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(220, 20))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")


        self.horizontalLayout_6.addWidget(self.comboBox)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(50, 20))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        baudRateL =  ['4800', '9600', '19200', '38400','57600','115200', '230400', '460800', '921600' ]
        self.comboBox_2.addItems(baudRateL)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setCurrentText("115200")
        self.horizontalLayout_9.addLayout(self.horizontalLayout_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.pushBtn_Open)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fileOpenFun1)
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.fileOpenFun2)
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 100))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.pushButton_5.clicked.connect(self.functionStart)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setMaximumHeight(80)
        self.horizontalLayout_8.addWidget(self.plainTextEdit)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Send_72px_1191826_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_8.addWidget(self.pushButton_4)
        # 点击执行输入框中命令
        self.pushButton_4.clicked.connect(self.excuteCommand)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout.addWidget(self.checkBox_13, 0, 0, 1, 2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 3, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 2, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 4, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 4, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 4, 2, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 5, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 5, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 5, 2, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 6, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 6, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 6, 2, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 7, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 7, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 7, 2, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setText("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 8, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 8, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 8, 2, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setText("")
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 9, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 9, 1, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 9, 2, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setText("")
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 10, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 10, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 10, 2, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setText("")
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 11, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 11, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_13.setMaximumSize(QtCore.QSize(0, 16777215))
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 11, 2, 1, 1)
        self.horizontalLayout_10.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        FastbootFlashMainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FastbootFlashMainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 23))
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
        self.label_3.setText(_translate("FastbootFlashMainWin", "UART1:"))
        self.comboBox.setCurrentText(_translate("FastbootFlashMainWin", "COM"))
        self.label_4.setText(_translate("FastbootFlashMainWin", "BaudRate："))
        self.pushButton_3.setText(_translate("FastbootFlashMainWin", "打开"))
        self.pushButton.setText(_translate("FastbootFlashMainWin", "Update文件1"))
        self.pushButton_2.setText(_translate("FastbootFlashMainWin", "Update文件2"))
        self.label.setText(_translate("FastbootFlashMainWin", "log"))
        self.label_2.setText(_translate("FastbootFlashMainWin", "升级次数："))
        self.checkBox.setText(_translate("FastbootFlashMainWin", "自动升级"))
        self.label_6.setText(_translate("FastbootFlashMainWin", "升级："))
        self.pushButton_5.setText(_translate("FastbootFlashMainWin", "开始"))
        self.pushButton_4.setText(_translate("FastbootFlashMainWin", "发送"))
        self.pushButton_4.setShortcut(_translate("FastbootFlashMainWin", "Return"))
        self.checkBox_13.setText(_translate("FastbootFlashMainWin", "全选"))
        self.pushButton_6.setText(_translate("FastbootFlashMainWin", "1"))
        self.pushButton_7.setText(_translate("FastbootFlashMainWin", "2"))
        self.pushButton_8.setText(_translate("FastbootFlashMainWin", "3"))
        self.pushButton_12.setText(_translate("FastbootFlashMainWin", "4"))
        self.pushButton_11.setText(_translate("FastbootFlashMainWin", "5"))
        self.pushButton_10.setText(_translate("FastbootFlashMainWin", "6"))
        self.pushButton_9.setText(_translate("FastbootFlashMainWin", "7"))
        self.pushButton_16.setText(_translate("FastbootFlashMainWin", "8"))
        self.pushButton_15.setText(_translate("FastbootFlashMainWin", "9"))
        self.pushButton_14.setText(_translate("FastbootFlashMainWin", "10"))
        self.pushButton_13.setText(_translate("FastbootFlashMainWin", "Save Log"))

    def printf(self, mypstr):
        # 自定义类print函数, 借用c语言
        # printf
        # Mypstr：是待显示的字符串
        strToPrint = time.strftime("[%Y-%m-%d %H:%M:%S]:", time.localtime()) + mypstr
        self.textBrowser.append(strToPrint)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    def pushBtn_Open(self):
        self.portStatus =  self.pushButton_3.text()
        # print('portStatus: ',self.portStatus)
        comboBobContent = self.comboBox.currentText()
        comRegex = re.compile('(COM\d*).*')
        self.comName = re.findall(comRegex, comboBobContent)[0]
        if self.portStatus == "打开":
            try:
                self.ser = serial.Serial(self.comName, 115200, bytesize=8, parity='N', timeout=0.8, xonxoff=False,rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
                self.comboBox.setEnabled(False)
                self.comboBox_2.setEditable(False)
                if self.ser.isOpen():
                    self.pushButton_3.setText("关闭")
                    mypstr = self.comName + '打开成功。'
                    self.printf(mypstr)
                    # try:
                    #     while self.ser.isOpen():
                    #         at_port_data = self.ser.read(size=1024)
                    #         if at_port_data:
                    #             string_ser_R = at_port_data.decode(encoding="utf-8", errors="strict")
                    #             string_ser_R_array = string_ser_R.split('\r\n')
                    #             for i in string_ser_R_array:
                    #                 serReadstr = '[O]' + i + "\r\n"
                    #                 self.printf(serReadstr)
                    #         else:
                    #             pass
                    # except:
                    #     pass
                else:
                    pass
            except:
                self.printf('串口被占用，请检查后重新打开。')

        if self.portStatus == '关闭':
            try:
                self.ser.close()
                self.comboBox.setEnabled(True)
                self.pushButton_3.setText("打开")
                myStrToPrint =  self.comName + '关闭成功。'
                self.printf(myStrToPrint)
            # except serial.serialutil.SerialException as e:
            #     myStrToPrint = time.strftime("[app:%Y-%m-%d %H:%M:%S]:",time.localtime()) + self.comName + '打开失败，失败原因：' + str(e)
            #     self.printf(myStrToPrint)
            except:
                pass

    def fileOpenFun1(self):
        self.versionDir1 = QFileDialog.getExistingDirectory(self,"选取文件夹",)#起始路径
        filePath1 = self.versionDir1 + r'\update\partition_nand.xml'
        if not os.path.exists(filePath1):
           self.printf('未找到partition.xml文件，请检查！\n')
        else:
            self.lineEdit.setText(self.versionDir1)

    def fileOpenFun2(self):
        self.versionDir2 = QFileDialog.getExistingDirectory(self, "选取文件夹2", )  # 起始路径
        # self.lineEdit_2.setText(self.versionDir2)
        filePath2 = self.versionDir2 + r'\update\partition_nand.xml'
        if not os.path.exists(filePath2):
           self.printf('未找到partition.xml文件，请检查！\n')
        else:
            self.lineEdit_2.setText(self.versionDir2)

    def spinBoxValueChange(self):
        self.updateCountTarget = int(self.spinBox.value())

    def updateStart(self,batNameToExc):
        batName = batNameToExc
        if self.checkBox.isChecked():
            count = 0
            while count < self.updateCountTarget:

                updateN = count+1
                self.printf('第'+ str(updateN)+'次升级开始...')
                self.printf('目标版本：')
                self.excuteCommand('at+qadbkey="m1mBBzfiF8sCd8e"')
                self.excuteCommand('AT+QCFG="USBCFG",0x2C7C,0x0125,1,1,1,1,1,1,0')
                self.excuteCommand('at+cfun=1,1')
                time.sleep(8)
                self.excuteCommand("AT+QFASTBOOT")
                p1 = subprocess.Popen(batName, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)
                out,err = p1.communicate()
                print("std_out:" + out)
                print("std_err:" + err)
                print('returncode' + str(p1.returncode))
        else:
            self.printf('完成，未进行升级')

    def makeBat(self, dirPath):
        if dirPath:
            version = os.path.split(dirPath)[1]
            batName = version + '_flash.bat'
            filePath = dirPath + r'\update\partition_nand.xml'
            fbat = open('./' + batName, 'w+')

            fbat.write('set path=' + dirPath + '/update\r\n')
            tree = ET.parse(filePath)
            root = tree.getroot()

            for child in root:
                for partition in child:
                    if partition.tag == 'partition':
                        for item in partition:
                            if item.tag == 'name':
                                a1 = item.text[2:].lower()
                            if item.tag == 'img_name':
                                a2 = item.text
                                if a2 == 'appsboot.mbn':
                                    continue
                                else:
                                    fbat.seek(0, 2)
                                    strToWrite = 'fastboot flash ' + a1 + ' %path%/' + a2 + '\r\n'
                                    fbat.write(strToWrite)
                                    # if self.fbUpdateFlag == 1:
                                    #     fcommand = 'fastboot flash' + a1 + self.versionDir1 + '\update' + a2
                                    #     p1 = subprocess.Popen(fcommand)
                                    #     mpstr=p1.returncode
                                    #     self.printf(mpstr)

            fbat.write('\r\nfastboot reboot\r\npause')
            fbat.close()
            batNameAbsPath = os.path.abspath(batName)
            mypstr = ' bat文件生成成功，文件路径: ' + batNameAbsPath
            self.printf(mypstr)
            return batNameAbsPath
        else:
            self.printf('未选择版本文件，请选择版本文件')
            return None


    def excuteCommand(self, command, adbFlag=1, adbkeyFlag=0):

        try:
            #self.printf('窗口内容：'+ self.plainTextEdit.toPlainText())
            command = self.plainTextEdit.toPlainText()+ '\r\n'
            #self.printf("command:"+ command)
            serPort = self.ser
            atCommand = command.encode("UTF-8")
            serPort.write(atCommand)
            #  串口执行AT指令后打印出来
            #commandStr = '[I]'+ command.replace('\r\n', '')
            #self.printf(commandStr)
            while 1:
                # ============================读取AT端口写AT指令的回显start===============================
                UART_port_data = serPort.read(size=10240)
                UART_data_result = UART_port_data.decode(encoding="utf-8", errors="strict")
                at_result = UART_data_result.split('\r\n')
                for at_man in at_result:
                    if at_man:
                        self.printf('[O]:' + at_man)
                        # self.RIStatus = self.ser.getRI()
                        # print(self.RIStatus)
                if re.search("OK",at_result ) or re.search(".*\:/#",at_result):
                    break
        except:
            pass


    def functionStart(self):
        try:
            batNameToExc1 = self.makeBat(self.versionDir1)
            batNameToExc2 = self.makeBat(self.versionDir2)
            self.updateStart(batNameToExc1)
            self.updateStart(batNameToExc2)
            self.pushButton_5.setText("重新开始")
        except:
            pass

class ComListComboBox(QComboBox):
    popupAboutToBeShown = pyqtSignal()

    def __init__(self, parent = None):
        super(ComListComboBox,self).__init__(parent)

    # 重写showPopup函数
    def showPopup(self):
        # 先清空原有的选项
        self.clear()
        self.insertItem(0, "COM")
        index = 1
        # 获取接入的所有串口信息，插入combobox的选项中
        portlist = self.get_port_list(self)
        if portlist is not None:
            for i in portlist:
                self.insertItem(index, i)
                index += 1
        QComboBox.showPopup(self)   # 弹出选项框

    @staticmethod
    # 获取接入的所有串口号
    def get_port_list(self):
        try:
            port_list = list(serial.tools.list_ports.comports())
            for port in port_list:
                yield str(port)
        except Exception as e:
            logging.error("获取接入的所有串口设备出错！\n错误信息："+str(e))

class paserKeyClass():

    def __init__(self):
        self.cookie = http.cookiejar.CookieJar()
        self.headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0'}
        self.opener = request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie))

    def loginJenkins(self):
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
        data = {'j_username': 'st_merge1',
                'j_password': '123456',
                'from': '',
                'Submit': 'Sign+in',
                'remember_me': 'on'}
        post_data = urllib.parse.urlencode(data).encode('utf-8')
        # 设置请求头
        # 登录时表单提交到的地址（用开发者工具可以看到）
        login_url = 'http://192.168.10.11:8080/j_acegi_security_check'
        # 构造登录请求
        req = request.Request(login_url, headers=self.headers, data=post_data)
        # 构造cookie
        # 由cookie构造opener
        # 登录后才能访问的网页
        self.opener.open(req)

    def getPaserKey(self, queryId, qtype):
        self.loginJenkins()
        url = 'http://192.168.10.11:8080/job/query_key/'
        # 构造访问请求
        req = request.Request(url, headers=self.headers)
        resp = self.opener.open(req)
        respBuffer = resp.read().decode('utf-8')
        succerssStr = re.search(r'最近成功的构建\s\(#\d+\)', respBuffer).group()
        newIndex = int(re.search(r'\d+', succerssStr).group())
        reayKeyStr = ""
        endIndex = 10
        if newIndex > 610:
            endIndex = newIndex - 600
        try:
            for i in range(newIndex, endIndex, -1):
                ur2 = 'http://192.168.10.11:8080/job/query_key/' + str(i) + '/consoleText'
                req2 = request.Request(ur2, headers=self.headers)
                resp2 = self.opener.open(req2)
                respBuffer2 = resp2.read().decode('utf-8')
                if queryId.strip() != '' and queryId in respBuffer2 and qtype.strip() != '' and qtype in respBuffer2:
                    ikeyIndex = int(respBuffer2.find('ikey='))
                    echoIndex = int(respBuffer2.find('+ echo'))
                    reayKeyStr = respBuffer2[ikeyIndex + 5:echoIndex]
                    #print(queryId + ':' + reayKeyStr)
                    break
                self.opener.close()
        except Exception:
            reayKeyStr = ""
        return reayKeyStr

    def createPwd(self, queryId, qtype):
        self.loginJenkins()
        url = 'http://192.168.10.11:8080/job/query_key/build '
        data = {
            'json': '{"parameter": [{"name": "qversion", "value": "v1.0"}, {"name": "ID", "value": "'+queryId+'"},{"name": "qtype", "value": "'+qtype+'"}], "statusCode": "303", "redirectTo": "."}'
            }
        post_data = urllib.parse.urlencode(data).encode('utf-8')
        req = request.Request(url, headers=self.headers, data=post_data)
        self.opener.open(req)
        self.opener.close()

class MainWin(QMainWindow,Ui_FastbootFlashMainWin):
    def __init__(self, parent = None):
        super(MainWin, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWin()
    mainWin.show()
    sys.exit(app.exec_())

