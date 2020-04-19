# -*- coding: utf-8 -*-

# created by Phoenix.Wang 2020/01/18
# Function: Quectel LTE fastboot flash update and serial port communication

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QComboBox,QLineEdit
from PyQt5.QtCore import pyqtSignal,QTimer
import sys,os,serial,time,re,subprocess,logging
import xml.etree.ElementTree as ET
import serial.tools.list_ports

class Ui_FastbootFlashMainWin(object):
    def setupUi(self, FastbootFlashMainWin):
        FastbootFlashMainWin.setObjectName("FastbootFlashMainWin")
        FastbootFlashMainWin.resize(500, 430)
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
        # serial list
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
        # Baud rate setup
        self.comboBox_baudrate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_baudrate.setObjectName("comboBox_2")
        self.horizontalLayout_3.addWidget(self.comboBox_baudrate)
        self.comboBox_baudrate.setEditable(True)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
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
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_clear.setMaximumSize(QtCore.QSize(50, 20))
        self.pushButton_clear.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.checkBox_autoUpdate = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_autoUpdate.setObjectName("checkBox_autoUpdate")
        self.horizontalLayout.addWidget(self.checkBox_autoUpdate)
        self.checkBox_debugMode = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_debugMode.setObjectName("checkBox_autoUpdate")
        self.horizontalLayout.addWidget(self.checkBox_debugMode)
        self.checkBox_ShowTime = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_ShowTime.setObjectName("checkBox_autoUpdate")
        self.horizontalLayout.addWidget(self.checkBox_ShowTime)
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
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_choseAll = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_choseAll.setObjectName("checkBox_choseAll")
        self.gridLayout.addWidget(self.checkBox_choseAll, 0, 0, 1, 2)
        self.checkBox_command1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_command1.setText("")
        self.checkBox_command1.setObjectName("checkBox_command1")
        self.gridLayout.addWidget(self.checkBox_command1, 1, 0, 1, 1)
        self.lineEdit_command1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command1.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_command1.setObjectName("lineEdit_command1")
        self.gridLayout.addWidget(self.lineEdit_command1, 1, 1, 1, 1)
        self.pushButton_command1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_command1.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_command1.setObjectName("pushButton_command1")
        self.gridLayout.addWidget(self.pushButton_command1, 1, 2, 1, 1)
        self.checkBox_command2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_command2.setText("")
        self.checkBox_command2.setObjectName("checkBox_command2")
        self.gridLayout.addWidget(self.checkBox_command2, 2, 0, 1, 1)
        self.lineEdit_command2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command2.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_command2.setObjectName("lineEdit_command2")
        self.gridLayout.addWidget(self.lineEdit_command2, 2, 1, 1, 1)
        self.pushButton_command2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_command2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_command2.setObjectName("pushButton_command2")
        self.gridLayout.addWidget(self.pushButton_command2, 2, 2, 1, 1)
        self.checkBox_command3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_command3.setText("")
        self.checkBox_command3.setObjectName("checkBox_command3")
        self.gridLayout.addWidget(self.checkBox_command3, 3, 0, 1, 1)
        self.lineEdit_command3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command3.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_command3.setObjectName("lineEdit_command3")
        self.gridLayout.addWidget(self.lineEdit_command3, 3, 1, 1, 1)
        self.pushButton_command3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_command3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_command3.setObjectName("pushButton_command3")
        self.gridLayout.addWidget(self.pushButton_command3, 3, 2, 1, 1)
        self.checkBox_command4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_command4.setText("")
        self.checkBox_command4.setObjectName("checkBox_command4")
        self.gridLayout.addWidget(self.checkBox_command4, 4, 0, 1, 1)
        self.lineEdit_command4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command4.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_command4.setObjectName("lineEdit_command4")
        self.gridLayout.addWidget(self.lineEdit_command4, 4, 1, 1, 1)
        self.pushButton_command4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_command4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_command4.setObjectName("pushButton_command4")
        self.gridLayout.addWidget(self.pushButton_command4, 4, 2, 1, 1)
        self.checkBox_command5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_command5.setText("")
        self.checkBox_command5.setObjectName("checkBox_command5")
        self.gridLayout.addWidget(self.checkBox_command5, 5, 0, 1, 1)
        self.lineEdit_command5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command5.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_command5.setObjectName("lineEdit_command5")
        self.gridLayout.addWidget(self.lineEdit_command5, 5, 1, 1, 1)
        self.pushButton_command5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_command5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_command5.setObjectName("pushButton_command5")
        self.gridLayout.addWidget(self.pushButton_command5, 5, 2, 1, 1)
        self.checkBox_command6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_command6.setText("")
        self.checkBox_command6.setObjectName("checkBox_command6")
        self.gridLayout.addWidget(self.checkBox_command6, 6, 0, 1, 1)
        self.lineEdit_command6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command6.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_command6.setObjectName("lineEdit_command6")
        self.gridLayout.addWidget(self.lineEdit_command6, 6, 1, 1, 1)
        self.pushButton_command6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_command6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_command6.setObjectName("pushButton_command6")
        self.gridLayout.addWidget(self.pushButton_command6, 6, 2, 1, 1)
        self.checkBox_command7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_command7.setText("")
        self.checkBox_command7.setObjectName("checkBox_command7")
        self.gridLayout.addWidget(self.checkBox_command7, 7, 0, 1, 1)
        self.lineEdit_command7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command7.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_command7.setObjectName("lineEdit_command7")
        self.gridLayout.addWidget(self.lineEdit_command7, 7, 1, 1, 1)
        self.pushButton_command7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_command7.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_command7.setObjectName("pushButton_command7")
        self.gridLayout.addWidget(self.pushButton_command7, 7, 2, 1, 1)
        self.checkBox_command8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_command8.setText("")
        self.checkBox_command8.setObjectName("checkBox_command8")
        self.gridLayout.addWidget(self.checkBox_command8, 8, 0, 1, 1)
        self.lineEdit_command8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command8.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_command8.setObjectName("lineEdit_command8")
        self.gridLayout.addWidget(self.lineEdit_command8, 8, 1, 1, 1)
        self.pushButton_command8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_command8.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_command8.setObjectName("pushButton_command8")
        self.gridLayout.addWidget(self.pushButton_command8, 8, 2, 1, 1)
        self.checkBox_command9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_command9.setText("")
        self.checkBox_command9.setObjectName("checkBox_command9")
        self.gridLayout.addWidget(self.checkBox_command9, 9, 0, 1, 1)
        self.lineEdit_command9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command9.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_command9.setObjectName("lineEdit_command9")
        self.gridLayout.addWidget(self.lineEdit_command9, 9, 1, 1, 1)
        self.pushButton_command9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_command9.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_command9.setObjectName("pushButton_command9")
        self.gridLayout.addWidget(self.pushButton_command9, 9, 2, 1, 1)
        self.checkBox_command10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_command10.setText("")
        self.checkBox_command10.setObjectName("checkBox_command10")
        self.gridLayout.addWidget(self.checkBox_command10, 10, 0, 1, 1)
        self.lineEdit_command10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command10.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_command10.setObjectName("lineEdit_command10")
        self.gridLayout.addWidget(self.lineEdit_command10, 10, 1, 1, 1)
        self.pushButton_command10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_command10.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_command10.setObjectName("pushButton_command10")
        self.gridLayout.addWidget(self.pushButton_command10, 10, 2, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setText("")
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 11, 0, 1, 1)
        self.lineEdit_saveLog = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_saveLog.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_saveLog.setObjectName("lineEdit_saveLog")
        self.gridLayout.addWidget(self.lineEdit_saveLog, 11, 1, 1, 1)
        self.pushButton_saveLog = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_saveLog.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_saveLog.setMaximumSize(QtCore.QSize(0, 16777215))
        self.pushButton_saveLog.setObjectName("pushButton_saveLog")
        self.gridLayout.addWidget(self.pushButton_saveLog, 11, 2, 1, 1)
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
        self.pushButton_clear.setText(_translate("FastbootFlashMainWin","clear"))
        self.label.setText(_translate("FastbootFlashMainWin", "log"))
        self.label_2.setText(_translate("FastbootFlashMainWin", "升级次数："))
        self.checkBox_ShowTime.setText(_translate("FastbootFlashMainWin", "show time"))
        self.checkBox_debugMode.setText(_translate("FastbootFlashMainWin", "debug"))
        self.checkBox_autoUpdate.setText(_translate("FastbootFlashMainWin", "自动升级"))
        self.label_6.setText(_translate("FastbootFlashMainWin", "升级："))
        self.pushButton_5.setText(_translate("FastbootFlashMainWin", "开始"))
        self.pushButton_4.setText(_translate("FastbootFlashMainWin", "发送"))
        self.pushButton_4.setShortcut(_translate("FastbootFlashMainWin", "Return"))
        self.checkBox_choseAll.setText(_translate("FastbootFlashMainWin", "全选"))
        self.checkBox_command1.setText(_translate("FastbootFlashMainWin", "1"))
        self.checkBox_command2.setText(_translate("FastbootFlashMainWin", "2"))
        self.checkBox_command3.setText(_translate("FastbootFlashMainWin", "3"))
        self.checkBox_command4.setText(_translate("FastbootFlashMainWin", "4"))
        self.checkBox_command5.setText(_translate("FastbootFlashMainWin", "5"))
        self.checkBox_command6.setText(_translate("FastbootFlashMainWin", "6"))
        self.checkBox_command7.setText(_translate("FastbootFlashMainWin", "7"))
        self.checkBox_command8.setText(_translate("FastbootFlashMainWin", "8"))
        self.checkBox_command9.setText(_translate("FastbootFlashMainWin", "9"))
        self.checkBox_command10.setText(_translate("FastbootFlashMainWin", "10"))
        self.pushButton_command1.setText(_translate("FastbootFlashMainWin", "1"))
        self.pushButton_command2.setText(_translate("FastbootFlashMainWin", "2"))
        self.pushButton_command3.setText(_translate("FastbootFlashMainWin", "3"))
        self.pushButton_command4.setText(_translate("FastbootFlashMainWin", "4"))
        self.pushButton_command5.setText(_translate("FastbootFlashMainWin", "5"))
        self.pushButton_command6.setText(_translate("FastbootFlashMainWin", "6"))
        self.pushButton_command7.setText(_translate("FastbootFlashMainWin", "7"))
        self.pushButton_command8.setText(_translate("FastbootFlashMainWin", "8"))
        self.pushButton_command9.setText(_translate("FastbootFlashMainWin", "9"))
        self.pushButton_command10.setText(_translate("FastbootFlashMainWin", "10"))
        self.pushButton_saveLog.setText(_translate("FastbootFlashMainWin", "Save Log"))

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

    def getPaserKey(self, QueryID, qtype):
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
                if QueryID.strip() != '' and QueryID in respBuffer2 and qtype.strip() != '' and qtype in respBuffer2:
                    ikeyIndex = int(respBuffer2.find('ikey='))
                    echoIndex = int(respBuffer2.find('+ echo'))
                    reayKeyStr = respBuffer2[ikeyIndex + 5:echoIndex]
                    #print(QueryID + ':' + reayKeyStr)
                    break
                self.opener.close()
        except Exception:
            reayKeyStr = ""
        return reayKeyStr

    def createPwd(self, QueryID, qtype):
        self.loginJenkins()
        url = 'http://192.168.10.11:8080/job/query_key/build '
        data = {
            'json': '{"parameter": [{"name": "qversion", "value": "v1.0"}, {"name": "ID", "value": "'+QueryID+'"},{"name": "qtype", "value": "'+qtype+'"}], "statusCode": "303", "redirectTo": "."}'
            }
        post_data = urllib.parse.urlencode(data).encode('utf-8')
        req = request.Request(url, headers=self.headers, data=post_data)
        self.opener.open(req)
        self.opener.close()

# import Qt
# class myPlianTextEdit(QtWidgets.QPlainTextEdit):
#     def __init__(self, parent):
#         QtWidgets.QPlainTextEdit.__init__(self)
#         self.parent = parent
#     def  keyPressEvent(self, event):
#         QtWidgets.QPlainTextEdit.keyPressEvent(self, event)
#         if event.key() == Qt.key_Return:
#

class MainWin(QMainWindow,Ui_FastbootFlashMainWin):
    def __init__(self, parent = None):
        super(MainWin, self).__init__(parent)
        self.setupUi(self)
        # init baud rate combobox and set default value to 115200
        self.author = 'Phoenix.Wang'
        self.mail = 'Phoenix.Wang@quectel.com'
        self.createTime = '2020-04-18 Friday'
        self.version = 'v1.1'
        self.comboBox_baudrate.setCurrentText("115200")
        baudRateL = ['115200','4800', '9600', '19200', '38400', '57600',  '230400', '460800', '921600']
        self.comboBox_baudrate.addItems(baudRateL)
        self.qtype = 'adb'
        self.plainTextEdit.setHidden(True)
        self.pushButton_4.setHidden(True)
        self.checkBox_ShowTime.setChecked(True)
        self.timer = QTimer(self)
        # self.plainTextEdit.Key_Enter.clicked.connect(self.sendData)
        self.timer.timeout.connect(self.data_receive)
        self.checkBox_choseAll.setChecked(True)
        self.checkBox_command1.setChecked(True)
        self.checkBox_command2.setChecked(True)
        self.checkBox_command3.setChecked(True)
        self.checkBox_command4.setChecked(True)
        self.checkBox_command5.setChecked(True)
        self.checkBox_command6.setChecked(True)
        self.checkBox_command7.setChecked(True)
        self.checkBox_command8.setChecked(True)
        self.checkBox_command9.setChecked(True)
        self.checkBox_command10.setChecked(True)
        self.checkBox_choseAll.stateChanged.connect(self.chooseAll)
        self.pushButton_command1.clicked.connect(self.pushBtnC1)
        self.pushButton_command2.clicked.connect(self.pushBtnC2)
        self.pushButton_command3.clicked.connect(self.pushBtnC3)
        self.pushButton_command4.clicked.connect(self.pushBtnC4)
        self.pushButton_command5.clicked.connect(self.pushBtnC5)
        self.pushButton_command6.clicked.connect(self.pushBtnC6)
        self.pushButton_command7.clicked.connect(self.pushBtnC7)
        self.pushButton_command8.clicked.connect(self.pushBtnC8)
        self.pushButton_command9.clicked.connect(self.pushBtnC9)
        self.pushButton_command10.clicked.connect(self.pushBtnC10)


        # open verison #1 package
        self.pushButton.clicked.connect(self.fileOpenFun1)

        # open version #2 package
        self.pushButton_2.clicked.connect(self.fileOpenFun2)

        # open serial port
        self.pushButton_3.clicked.connect(self.pushBtn_Open)

        # start
        self.pushButton_5.clicked.connect(self.functionStart)

        # send data
        self.pushButton_4.clicked.connect(self.sendBtnClicked)

        # clear log
        self.pushButton_clear.clicked.connect(self.echoClear)

        # debug mode
        self.checkBox_debugMode.toggled.connect(self.debugMuanulMode)

    # 打印到Text Browser
    def printf(self, mypstr):
        # 自定义类print函数, 借用c语言
        # printf
        # Mypstr：是待显示的字符串
        if self.checkBox_ShowTime.isChecked():
            strToPrint = time.strftime("[%Y-%m-%d %H:%M:%S]:", time.localtime()) + mypstr
        else:
            strToPrint = mypstr
        self.textBrowser.append(strToPrint)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    # 打开串口
    def pushBtn_Open(self):
        self.ser_baudrate = int(self.comboBox_baudrate.currentText())
        self.portStatus =  self.pushButton_3.text()
        comboBobContent = self.comboBox.currentText()
        comRegex = re.compile('(COM\d*).*')
        self.comName = re.findall(comRegex, comboBobContent)[0]
        if self.portStatus == "打开":
            try:
                self.ser = serial.Serial(self.comName, self.ser_baudrate, bytesize=8, parity='N', timeout=0.8, xonxoff=False,rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
                self.comboBox.setEnabled(False)
                self.comboBox_baudrate.setEditable(False)
                if self.ser.isOpen():
                    self.pushButton_3.setText("关闭")
                    mypstr = self.comName + '打开成功。'
                    self.printf(mypstr)
                    self.timer.start(2)
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

    # 打开版本2文件
    def fileOpenFun1(self):
        self.versionDir1 = QFileDialog.getExistingDirectory(self,"选取文件夹",)#起始路径
        filePath1 = self.versionDir1 + r'\update\partition_nand.xml'
        if not os.path.exists(filePath1):
           self.printf('未找到partition.xml文件，请检查！\n')
        else:
            self.lineEdit.setText(self.versionDir1)

    # 打开版本2文件
    def fileOpenFun2(self):
        self.versionDir2 = QFileDialog.getExistingDirectory(self, "选取文件夹2", )  # 起始路径
        # self.lineEdit_2.setText(self.versionDir2)
        filePath2 = self.versionDir2 + r'\update\partition_nand.xml'
        if not os.path.exists(filePath2):
           self.printf('未找到partition.xml文件，请检查！\n')
        else:
            self.lineEdit_2.setText(self.versionDir2)

    # get adb key
    def queryWithID(self):
        key = ''
        self.printf("正在查询历史秘钥！请稍等...")
        try:
            key = paserKeyClass().getPaserKey(self.QueryID, self.qtype)
            # 找不到，再去重新生成
            if key == '':
                self.printf("没有找到历史秘钥！正在重新生成！请稍等...")
                paserKeyClass().createPwd(self.QueryID, self.qtype)
                time.sleep(1)
                key = paserKeyClass().getPaserKey(self.QueryID, self.qtype)
                if key == '':
                    time.sleep(2)
                    key = paserKeyClass().getPaserKey(self.QueryID, self.qtype)
                    if key == '':
                        self.printf("查询秘钥失败，请稍后重试")
                    else:
                        pass
            else:
                self.adbKey = key
                self.printf(self.adbKey)
        except:
            pass

    # 获取自动升级次数
    def spinBoxValueChange(self):
        self.updateCountTarget = int(self.spinBox.value())

    # start btn clicked events
    def fastbootUpdate(self,batNameToExc):
        batName = batNameToExc
        if self.usbCfgAdgFlag:
            self.sendData('at+qadb?')
            self.data_receive()
            self.queryWithID()
            self.sendData('at+qadbkey=' + '"' + self.adbKey + '"')  # adb key
            self.sendData('at+qcfg="usbcfg')
            self.sendData('AT+QCFG="USBCFG",'+ self.usbArg1+ ',' + self.usbArg2 + ',1,1,1,1,1,'+ self.usbArg3 + ','+ self.usbArg4)
            self.sendData('at+cfun=1,1')
            time.sleep(12)
        self.sendData("AT+QFASTBOOT")
        while count < self.updateCountTarget:
            updateN = count+1
            p1 = subprocess.Popen(batName, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)
            out,err = p1.communicate()
            print("std_out:" + out)
            print("std_err:" + err)
            print('returncode' + str(p1.returncode))


    # make a bat file to fastboot flash update by reading nan.xml file of version package
    def makeBat(self, dirPath):
        # self.updateItem = []
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
                                    # flashArr = [a1,a2]
                                    # self.updateItem.append(flashArr)
                                    # print(self.updateItem)
                                    fbat.seek(0, 2)
                                    strToWrite = 'fastboot flash ' + a1 + ' %path%/' + a2 + '\r\n'
                                    fbat.write(strToWrite)

            fbat.write('\r\nfastboot reboot\r\npause')
            fbat.close()
            batNameAbsPath = os.path.abspath(batName)
            mypstr = ' bat文件生成成功，文件路径: ' + batNameAbsPath
            self.printf(mypstr)
            return batNameAbsPath
        else:
            self.printf('未选择版本文件，请选择版本文件')
            return None

    # start fastboot flsh  update process
    def fastbootflashupdate(self):
        pass

    # at+qfastboot, Enter fastboot mode
    def enterFastbootMode(self):
        pass

    # send btn event
    def sendBtnClicked(self):
        command = self.plainTextEdit.toPlainText()
        self.sendData(command)

    def sendData(self,dataToSend):
        try:
            # command = self.plainTextEdit.toPlainText()
            if dataToSend == "version":
                self.printf(self.version)
            elif dataToSend == "author":
                self.printf(self.author)
            elif dataToSend == "createTime":
                self.printf(self.createTime)
            else:
                command = dataToSend + '\r\n'
                serPort = self.ser
                atCommand = command.encode("UTF-8")
                serPort.write(atCommand)
        except:
            pass

    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if num > 0:
            data = self.ser.read(1024)
            num = len(data)
            # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
            dataDecode = data.decode('utf-8').split('\r\n')
            for at_man in dataDecode:
                if at_man:
                    if self.checkBox_autoUpdate.isChecked():
                        adbKeyRegex1 = re.compile('\+QADBKEY: ([\d]{8})')
                        adbKeyResult1 = re.findall(adbKeyRegex1, at_man)
                        if adbKeyResult1:
                            self.QuectelId = adbKeyResult1[0]
                            self.print('Quectel ID: '+ self.QuectelID )
                        usbCfgAdbRegex = re.compile('\+QCFG: "usbcfg",(.*),(.*),\d,\d,\d,\d,\d,(\d),(\d)')
                        usbCfgAdbResult = re.findall(usbCfgAdbRegex, at_man)
                        if usbCfgAdbResult:
                            self.usbArg1 = usbCfgAdbResult[0]
                            self.usbArg2 = usbCfgAdbResult[1]
                            self.usbArg3 = usbCfgAdbResult[2]
                            self.usbArg4 = usbCfgAdbResult[4]
                            if self.usbArg3 == 0:
                                self.usbCfgAdgFlag = 1

                    self.printf(at_man)
                    # 获取到text光标
                    textCursor = self.textBrowser.textCursor()
                    # 滚动到底部
                    textCursor.movePosition(textCursor.End)
                    # 设置光标到text中去
                    self.textBrowser.setTextCursor(textCursor)

    def functionStart(self):
        # try:
        self.usbCfgAdgFlag = 1
        batNameToExc1 = self.makeBat(self.versionDir1)
        batNameToExc2 = self.makeBat(self.versionDir2)
        print(batNameToExc1)
        print(batNameToExc2)
        if self.checkBox_autoUpdate.isChecked():
            self.fastbootUpdate(batNameToExc1)
            self.fastbootUpdate(batNameToExc2)
        self.pushButton_5.setText("重新开始")
        # except:
        #     pass

    # clear echo log
    def echoClear(self):
        self.textBrowser.setText("")

    # get list of command to execute
    def getCommandList(self):
        pass

    # open data send widget
    def debugMuanulMode(self):
        self.plainTextEdit.setPlainText("")
        if self.checkBox_debugMode.isChecked():
            self.plainTextEdit.setHidden(False)
            self.pushButton_4.setHidden(False)
        else:
            self.plainTextEdit.setHidden(True)
            self.pushButton_4.setHidden(True)

    # select all command
    def chooseAll(self):
        if self.checkBox_choseAll.isChecked():
            self.checkBox_command1.setChecked(True)
            self.checkBox_command2.setChecked(True)
            self.checkBox_command3.setChecked(True)
            self.checkBox_command4.setChecked(True)
            self.checkBox_command5.setChecked(True)
            self.checkBox_command6.setChecked(True)
            self.checkBox_command7.setChecked(True)
            self.checkBox_command8.setChecked(True)
            self.checkBox_command9.setChecked(True)
            self.checkBox_command10.setChecked(True)
        else:
            self.checkBox_command1.setChecked(False)
            self.checkBox_command2.setChecked(False)
            self.checkBox_command3.setChecked(False)
            self.checkBox_command4.setChecked(False)
            self.checkBox_command5.setChecked(False)
            self.checkBox_command6.setChecked(False)
            self.checkBox_command7.setChecked(False)
            self.checkBox_command8.setChecked(False)
            self.checkBox_command9.setChecked(False)
            self.checkBox_command10.setChecked(False)

    # pushbtn_command1
    def pushBtnC1(self):
        command = self.lineEdit_command1.text()
        self.sendData(command)

    # pushbtn_command2
    def pushBtnC2(self):
        command = self.lineEdit_command2.text()
        self.sendData(command)

    # pushbtn_command3
    def pushBtnC3(self):
        command = self.lineEdit_command3.text()
        self.sendData(command)

    # pushbtn_command4
    def pushBtnC4(self):
        command = self.lineEdit_command4.text()
        self.sendData(command)

    # pushbtn_command5
    def pushBtnC5(self):
        command = self.lineEdit_command5.text()
        self.sendData(command)

    # pushbtn_command6
    def pushBtnC6(self):
        command = self.lineEdit_command6.text()
        self.sendData(command)

    # pushbtn_command7
    def pushBtnC7(self):
        command = self.lineEdit_command7.text()
        self.sendData(command)

    # pushbtn_command8
    def pushBtnC8(self):
        command = self.lineEdit_command8.text()
        self.sendData(command)

    # pushbtn_command9
    def pushBtnC9(self):
        command = self.lineEdit_command9.text()
        self.sendData(command)

    # pushbtn_command10
    def pushBtnC10(self):
        command = self.lineEdit_command10.text()
        self.sendData(command)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWin()
    mainWin.show()
    sys.exit(app.exec_())

