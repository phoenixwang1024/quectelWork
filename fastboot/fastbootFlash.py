# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fastbootFlash.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QComboBox
import sys,os, time
import os,serial,datetime,time,requests,re,subprocess
import xml.etree.ElementTree as ET
import serial.tools.list_ports
from PyQt5.QtCore import pyqtSignal
import logging


class Ui_FastbootFlashMainWin(object):
    def setupUi(self, FastbootFlashMainWin):
        FastbootFlashMainWin.setObjectName("FastbootFlashMainWin")
        FastbootFlashMainWin.resize(531, 394)
        self.centralwidget = QtWidgets.QWidget(FastbootFlashMainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fileOpenFun1)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 231, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.fileOpenFun2)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 231, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 130, 331, 141))
        self.textBrowser.setObjectName("textBrowser")


        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 290, 75, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.functionStart)

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
        self.spinBox.valueChanged.connect(self.spinBoxValueChange)

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
        self.widget.setGeometry(QtCore.QRect(10, 10, 123, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox = MyComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEditable(True)

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

    def fileOpenFun1(self):
        self.versionDir1 = QFileDialog.getExistingDirectory(self,"选取文件夹",)#起始路径
        self.lineEdit.setText(self.versionDir1)


        # print(self.versionDir1,type(self.versionDir1))

    def fileOpenFun2(self):
        self.versionDir2 = QFileDialog.getExistingDirectory(self, "选取文件夹2", )  # 起始路径
        self.lineEdit_2.setText(self.versionDir2)

        # print(self.versionDir2, type(self.versionDir2))

    def spinBoxValueChange(self):
        self.updateCount = int(self.spinBox.value())

    def printf(self, mypstr):
        # 自定义类print函数, 借用c语言
        # printf
        # Mypstr：是待显示的字符串
        self.textBrowser.append(mypstr)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    def functionStart(self):


        # self.SPN = 'com'+ self.comboBox.value
        self.baudRate = 115200

        # self.makeBat(self, self.versionDir1)
        # self.makeBat(self, self.versionDir2)
        # self.printf("[input:%Y-%m-%d %H:%M:%S]:Worked Finished!\r\n")
        # self.printf('[input:%Y-%m-%d %H:%M:%S]:')
        self.pushButton_5.setText("升级完成！")
        #  获取xml文件路劲和要生成的bat文件名称
        # def getPath(self ):
        #     global batName
        #     global filePath
        #     global dirPath
        #     global execBatFlag
        #     while True:
        #         dirPath = input('输入版本包路径，或者把包文件夹拖到此处：>>> ')
        #         filePath = dirPath + r'\update\partition_nand.xml'
        #         updateDir =  dirPath + r'\update'
        #         if os.path.isdir(updateDir):
        #             if not os.path.exists(filePath):
        #                 print('未找到partition.xml文件，请确保路径是否正确并重试！\n')
        #             else:
        #                 break
        #         else:
        #             print('请确保输入路径为文件夹，而不是文件！')
        #
        #     # batNameInput = input('输bat名称,不带.bat后缀,缺省将以版本名称命名:>>> ')
        #     # if batNameInput == '':
        #     version = os.path.split(dirPath)[1]
        #     batName = version + '_flash.bat'
        #     # else:
        #     #     batName = batNameInput + '.bat'

    def makeBat(self, filePath, batName):
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

        fbat.write('\r\nfastboot reboot\r\npause')
        fbat.close()
        print(' bat文件生成成功，文件路径: ', os.path.abspath(batName))

    def fastbootFlashUpdate(self, countTarget=10, autoUpdateFlag=1):
        count = 0
        while autoUpdateFlag:
            pass

    def queryKey(self):

        ADBid = self.excuteCommand("AT+QADBKEY?", 1, 1)
        print("adb query ID: %s" % ADBid)
        if adbKey:
            url1 = 'http://192.168.10.11:8080/job/query_key/build?delay=0sec'
            reResult = 1

            global header
            # cookie = r'htmlAudioNotificationsEnabled=false; jenkins-timestamper-offset=-28800000; screenResolution=1920x1080; JSESSIONID.50763f5b=node0eed4ricnv1bc14enhx3mdkt4l937.node0'
            header = {
                'Connection': 'keep-alive',
                # 'Cookie': cookie,
                'Host': '192.168.10.11:8080',
                'Origin': 'http://192.168.10.11:8080',
                'Referer': 'http://192.168.10.11:8080/job/query_key/build?delay=0sec',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            }

            formData = {}
            json = '{"parameter": [{"name": "qversion", "value": "' + qversion + '"}, {"name": "ID", "value": "' + adbKey + '"}, {"name": "qtype", "value": "' + qtype + '"}], "statusCode": "303", "redirectTo": "."}'
            formData['json'] = json
            formData['Submit'] = 'Build'
            # response1 = requests.post(url1, headers=header, data=formData)    #  发送adb key查询密码

            buildHistoryUrl = 'http://192.168.10.11:8080/job/query_key/buildHistory/all'
            response3 = requests.session.get(buildHistoryUrl, headers=header)
            idRegex = re.compile(
                '<a update-parent-class=".build-row" href="/job/query_key/([\d]*)/" class="tip model-link inside build-link display-name">')
            # print('History request: ', response3.text)
            currentID = re.findall(idRegex, response3.text)[0]
            print('current: ', currentID)

            while reResult:
                url2 = 'http://192.168.10.11:8080/job/query_key/' + currentID + '/console'
                response2 = requests.get(url2, headers=header)
                # print(response2.status_code)
                # print(response2.text)
                adbRegex1 = re.compile('\+\+ sh genkey.sh v1.0 ([\d]+)')
                match_adb_key = re.findall(adbRegex1, response2.text)
                # print(match_adb_key)
                if match_adb_key[0] == adbKey:
                    adbRegex2 = re.compile(r'您所查询的密钥为：(.*)')
                    result = re.findall(adbRegex2, response2.text)
                    debug_key = result[1]
                    print('Key: ', debug_key)
                    reResult = 0
                    return debug_key
                else:
                    currentID = str(int(currentID) - 1)
        else:
            debug_key = 'quectel123'
            return debug_key

    def serialOpen(self, SPN, baudRate):
        global serPort
        try:
            serPort = serial.Serial(SPN, baudRate, bytesize=8, parity='N', stopbits=1, timeout=1)
            checkPort = serPort.isOpen()
            if checkPort:
                serPort.close()
                serPort = serial.Serial(SPN, baudRate, bytesize=8, parity='N', timeout=1, xonxoff=False,
                                        rtscts=False,
                                        write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
                serOut = serPort.read(size=1024)
                string_AT_R = serOut.decode(encoding="utf-8", errors="strict")
                string_AT_R_array = string_AT_R.split('\r\n')
                for i in string_AT_R_array:
                    print(time.strftime("[serial:%Y-%m-%d %H:%M:%S]:", time.localtime()) + i + "\r\n")
        except serial.serialutil.SerialException as e:
            print("Error happens: ", e)
            serPort.close()

    def excuteCommand(self, command, adbFlag=1, adbkeyFlag=0):
        global adbKey
        atCommand = command.encode('utf-8')
        serPort.write(atCommand)
        #  串口执行AT指令，funcFlag默认1，会返回上报信息
        if adbFlag == 1:
            commandStr = time.strftime("[input:%Y-%m-%d %H:%M:%S]:", time.localtime()) + command.replace('\r\n', '')
            self.printf(commandStr)
            serOut = serPort.read(size=1024)
            string_AT_R = serOut.decode(encoding="utf-8", errors="strict")
            string_AT_R_array = string_AT_R.split('\r\n')
            for i in string_AT_R_array:
                serReadstr = time.strftime("[response:%Y-%m-%d %H:%M:%S]:", time.localtime()) + i + "\r\n"
                self.printf(serReadstr)
                if adbkeyFlag:
                    adbKeyRegex = re.compile('\+QADBKEY: ([\d]*)')
                    adbKeyResult = re.findall(adbKeyRegex, i)
                    if adbKeyResult:
                        adbKey = adbKeyResult[0]
                        return adbKey



class MyComboBox(QComboBox):
    popupAboutToBeShown = pyqtSignal()
    def showPopup(self):
        self.popupAboutToBeShown.emit()

        def get_port_list(self):
            try:
                port_list = list(serial.tools.list_ports.comports())
                for port in port_list:
                    yield str(port)
            except Exception as e:
                logging.error("获取接入的所有串口设备出错\n 错误信息："+str(e))

            port_list = self.get_port_list(self)

    # def mousePressEvent(self, QMouseEvent) #这个是重写鼠标点击事件
        # self.popupAboutToBeShow.emit()
    # def showPopup(self):
    #     self.popupAboutToBeShown.emit() #发送信号



class MainWin(QMainWindow,Ui_FastbootFlashMainWin):
    def __init__(self, parent = None):
        super(MainWin, self).__init__(parent)
        self.setupUi(self)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWin()
    mainWin.show()
    sys.exit(app.exec_())

