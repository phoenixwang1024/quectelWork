# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QQuery_1.0.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
import sys,os,serial,logging
import serial.tools.list_ports
import sys,re,time
import urllib.request
import http.cookiejar
from urllib import request
from PyQt5.QtWidgets import *
import pyperclip

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_QuectelID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_QuectelID.setObjectName("lineEdit_QuectelID")
        self.gridLayout.addWidget(self.lineEdit_QuectelID, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.radioButton_adb = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_adb.setChecked(False)
        self.radioButton_adb.setObjectName("radioButton_adb")
        self.gridLayout.addWidget(self.radioButton_adb, 2, 0, 1, 1)
        self.radioButton_Console = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_Console.setChecked(True)
        self.radioButton_Console.setObjectName("radioButton_Console")

        self.gridLayout.addWidget(self.radioButton_Console, 2, 1, 1, 1)
        self.pushButton_QueryWithCom = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_QueryWithCom.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_QueryWithCom.setObjectName("pushButton_QueryWithCom")

        self.gridLayout.addWidget(self.pushButton_QueryWithCom, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_QueryWithID = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_QueryWithID.setObjectName("pushButton_QueryWithID")

        self.gridLayout.addWidget(self.pushButton_QueryWithID, 1, 2, 1, 1)
        self.comboBox_comList = ComListComboBox(self.centralwidget)
        self.comboBox_comList.setEditable(True)
        self.comboBox_comList.setMaximumSize(QtCore.QSize(500, 16777215))
        self.comboBox_comList.setObjectName("comboBox_comList")
        self.gridLayout.addWidget(self.comboBox_comList, 0, 1, 1, 1)
        self.pushButton_Copy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Copy.setObjectName("pushButton_Copy")
        self.gridLayout.addWidget(self.pushButton_Copy, 2, 2, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 1, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QQury"))
        self.label.setText(_translate("MainWindow", "Port:"))
        self.radioButton_adb.setText(_translate("MainWindow", "adb"))
        self.radioButton_Console.setText(_translate("MainWindow", "console"))
        self.pushButton_QueryWithCom.setText(_translate("MainWindow", "串口查询"))
        self.label_2.setText(_translate("MainWindow", "Quectel ID:"))
        self.pushButton_QueryWithID.setText(_translate("MainWindow", "ID查询"))
        self.pushButton_Copy.setText(_translate("MainWindow", "复制"))
        self.label_3.setText(_translate("MainWindow", "查询空间Port请选择debug口  "))
        self.checkBox.setText(_translate("MainWindow", "压力空间查询"))



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

class ComListComboBox(QComboBox):
    popupAboutToBeShown = pyqtSignal()

    def __init__(self, parent=None):
        super(ComListComboBox, self).__init__(parent)

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
        QComboBox.showPopup(self)  # 弹出选项框

    @staticmethod
    # 获取接入的所有串口号
    def get_port_list(self):
        try:
            port_list = list(serial.tools.list_ports.comports())
            for port in port_list:
                yield str(port)
        except Exception as e:
            logging.error("获取接入的所有串口设备出错！\n错误信息：" + str(e))

from PyQt5.QtCore import QTimer

class MainWin(QMainWindow,Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWin, self).__init__(parent)

        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)

        self.qtype = 'console'
        self.setupUi(self)
        self.radioButton_Console.toggled.connect(lambda: self.btnstate(self.radioButton_Console))
        self.pushButton_QueryWithCom.clicked.connect(self.queryWithCom)
        self.pushButton_QueryWithID.clicked.connect(self.queryWithID)
        self.pushButton_Copy.clicked.connect(self.copy)

    def printf(self, mypstr):
        # 自定义类print函数, 借用c语言
        # printf
        # Mypstr：是待显示的字符串
        strToPrint =  mypstr
        self.textBrowser.append(strToPrint)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    def queryWithID(self):
        self.comboBox_comList.setEnabled(False)
        self.queryId = self.lineEdit_QuectelID.text()
        self.key = ''
        if self.queryId.strip() != '' and re.match(r'\d{8}', self.queryId):
           # 先去遍历历史生成的秘钥
            self.textBrowser.setText("正在帮您查询历史秘钥！请稍等...")
            try:
                self.key = paserKeyClass().getPaserKey(self.queryId, self.qtype)
                # 找不到，再去重新生成
                if self.key == '':
                    self.textBrowser.setText("没有找到历史秘钥！正在帮您重新生成！请稍等...请不要关闭窗口！！！！！")
                    paserKeyClass().createPwd(self.queryId, self.qtype)
                    time.sleep(1)
                    self.key = paserKeyClass().getPaserKey(self.queryId, self.qtype)
                if self.key == '':
                    time.sleep(2)
                    self.key = paserKeyClass().getPaserKey(self.queryId, self.qtype)
                    if self.key == '':
                        self.textBrowser.setText("暂时未查到密钥！后续优化获取的方法！")
                    else:
                        pass
                else:
                    self.textBrowser.setText('')
                    self.comboBox_comList.setEnabled(True)
                    if self.checkBox.isChecked():
                        commandCehckSize = 'cd /&& du -d1 \r\n'.encode('UTF-8')
                        self.ser.write(commandCehckSize)
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
                            if re.search(".*\:/#", at_result):
                                break
                    self.printf(self.key)
                    self.port_close()
            except:
                self.port_close()
                pass
        else:
            self.comboBox_comList.setEnabled(True)
            self.textBrowser.setText("请检查输入内容是否满足8位数ID")

    def openPort(self):
        pass

    def queryWithCom(self):
        self.lineEdit_QuectelID.setText('')
        self.textBrowser.setText('')
        self.portStatus = self.pushButton_QueryWithCom.text()
        # print('portStatus: ',self.portStatus)
        comboBobContent = self.comboBox_comList.currentText()
        comRegex = re.compile('(COM\d*).*')
        self.comName = re.findall(comRegex, comboBobContent)[0]
        try:
            self.ser = serial.Serial(self.comName, 115200, bytesize=8, parity='N', timeout=0.8, xonxoff=False,
                                     rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
            self.timer.start(2)
            if self.ser.isOpen():
                if not self.checkBox.isChecked():
                    self.printf(self.comName + '打开成功')
                    # self.pushButton_QueryWithCom.setText("查询中")
                    command = "AT+QADBKEY?"+'\r\n'
                    atCommand = command.encode('utf-8')
                    self.ser.write(atCommand)
                else:
                    self.queryWithID()
        except:
            self.textBrowser.setText("端口被占用，请检查后重试")
            self.port_close()
            pass
        while self.checkBox.isChecked():
            if self.key:
                self.debugLogIn()

    def copy(self):
        # print(str(self.textBrowser.toPlainText()))
        self.textToCopy = pyperclip.copy(str(self.textBrowser.toPlainText()))

    def debugLogIn(self):
        self.sendData('root')
        while 1:
            data = self.ser.read(1024)
            data_decode = data.decode(encoding="utf-8", errors="strict")
            # data_result = data_decode.split('\r\n')
            print(data_result)
            if re.search('Password: ',data_decode):
                self.sendData(self.key)
                while 1:
                    dataRes2 = self.ser.read(1024)
                    dataRes2_decode =  dataRes2.decode(encoding="utf-8",errors="strict")
                    if re.search('root@mdm9607-perf:~# ', dataRes2_decode):
                        self.sendData('cd /&& du -d1')
                        print('login and check size:')
                        break
            elif re.search('.*mdm9607-perf login:.*', data_result):
                # if at_man == "mdm9607-perf login:":
                self.sendData('root')
                dataRes1 = self.ser.read(1024)
                data1_decode = dataRes1.decode(encoding="utf-8", errors="strict")
                if re.search('.*Password:.*'):
                    self.sendData(self.lineEdit_QuectelID.text())
                    break


    # 接收数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
            if num > 0:
                self.comboBox_comList.setEnabled(False)
        except:
            self.port_close()
            return None
        if num > 0:
            data = self.ser.read(1024)
            num = len(data)
            UART_data_result = data.decode(encoding="utf-8", errors="strict")
            at_result = UART_data_result.split('\r\n')
            for at_man in at_result:
                if at_man:
                    adbKeyRegex1 = re.compile('\+QADBKEY: ([\d]{8})')
                    adbKeyRegex2 = re.compile(' quectel-ID : ([\d]{8})')
                    adbKeyResult1 = re.findall(adbKeyRegex1, at_man)
                    adbKeyResult2 = re.findall(adbKeyRegex2, at_man)
                    if adbKeyResult1:
                        self.QuectelId = adbKeyResult1[0]
                        self.lineEdit_QuectelID.setText(self.QuectelId)
                        self.queryWithID()
                        break
                    elif adbKeyResult2:
                        self.QuectelId = adbKeyResult2[0]
                        self.lineEdit_QuectelID.setText(self.QuectelId)
                        self.queryWithID()
                        break
                    else:
                        if self.ser.isOpen():
                            # self.pushButton_QueryWithCom.setText("查询中")
                            command = "root" + '\r\n'
                            atCommand = command.encode('utf-8')
                            self.ser.write(atCommand)
                            time.sleep(3)
                            data = self.ser.read(1024)
                            num = len(data)
                            UART_data_result = data.decode(encoding="utf-8", errors="strict")
                            at_result = UART_data_result.split('\r\n')
                            for at_man in at_result:
                                if at_man:
                                    adbKeyRegex1 = re.compile('\+QADBKEY: ([\d]{8})')
                                    adbKeyRegex2 = re.compile(' quectel-ID : ([\d]{8})')
                                    adbKeyResult1 = re.findall(adbKeyRegex1, at_man)
                                    adbKeyResult2 = re.findall(adbKeyRegex2, at_man)
                                    if adbKeyResult1:
                                        self.QuectelId = adbKeyResult1[0]
                                        self.lineEdit_QuectelID.setText(self.QuectelId)
                                        self.queryWithID()
                                        break
                                    elif adbKeyResult2:
                                        self.QuectelId = adbKeyResult2[0]
                                        self.lineEdit_QuectelID.setText(self.QuectelId)
                                        self.queryWithID()
                                        break

            # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
            # self.textBrowser.insertPlainText(data.decode('iso-8859-1'))

            # 获取到text光标
            textCursor = self.textBrowser.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.textBrowser.setTextCursor(textCursor)
        else:
            pass

    def getKey(self):

        try:
            num = self.ser.inWaiting()
            if num>0:
                self.comboBox_comList.setEnabled(False)
        except:
            self.port_close()
            return None
        if num > 0:
            data = self.ser.read(1024)
            num = len(data)
            UART_data_result = data.decode(encoding="utf-8", errors="strict")
            at_result = UART_data_result.split('\r\n')
            for at_man in at_result:
                if at_man:
                    adbKeyRegex1 = re.compile('\+QADBKEY: ([\d]{8})')
                    adbKeyRegex2 = re.compile(' quectel-ID : ([\d]{8})')
                    adbKeyResult1 = re.findall(adbKeyRegex1, at_man)
                    adbKeyResult2 = re.findall(adbKeyRegex2, at_man)
                    if adbKeyResult1:
                        self.QuectelId = adbKeyResult1[0]
                        self.lineEdit_QuectelID.setText(self.QuectelId)
                        self.queryWithID()
                        break
                    elif adbKeyResult2:
                        self.QuectelId = adbKeyResult2[0]
                        self.lineEdit_QuectelID.setText(self.QuectelId)
                        self.queryWithID()
                        break
                    else:
                        if self.ser.isOpen():
                            # self.pushButton_QueryWithCom.setText("查询中")
                            command = "root" + '\r\n'
                            atCommand = command.encode('utf-8')
                            self.ser.write(atCommand)
                            time.sleep(3)
                            data = self.ser.read(1024)
                            num = len(data)
                            UART_data_result = data.decode(encoding="utf-8", errors="strict")
                            at_result = UART_data_result.split('\r\n')
                            for at_man in at_result:
                                if at_man:
                                    adbKeyRegex1 = re.compile('\+QADBKEY: ([\d]{8})')
                                    adbKeyRegex2 = re.compile(' quectel-ID : ([\d]{8})')
                                    adbKeyResult1 = re.findall(adbKeyRegex1, at_man)
                                    adbKeyResult2 = re.findall(adbKeyRegex2, at_man)
                                    if adbKeyResult1:
                                        self.QuectelId = adbKeyResult1[0]
                                        self.lineEdit_QuectelID.setText(self.QuectelId)
                                        self.queryWithID()
                                        break
                                    elif adbKeyResult2:
                                        self.QuectelId = adbKeyResult2[0]
                                        self.lineEdit_QuectelID.setText(self.QuectelId)
                                        self.queryWithID()
                                        break


            # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
            # self.textBrowser.insertPlainText(data.decode('iso-8859-1'))

            # 获取到text光标
            textCursor = self.textBrowser.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.textBrowser.setTextCursor(textCursor)
        else:
            pass

    def port_close(self):
        self.timer.stop()
        try:
            self.ser.close()
        except:
            pass
        self.pushButton_QueryWithCom.setEnabled(True)
        self.pushButton_QueryWithID.setEnabled(True)
        self.comboBox_comList.setEnabled(True)
        # 接收数据和发送数据数目置零
        # self.data_num_received = 0
        # self.lineEdit.setText(str(self.data_num_received))
        # self.data_num_sended = 0
        # self.lineEdit_2.setText(str(self.data_num_sended))
        # self.formGroupBox1.setTitle("串口状态（已关闭）")

    def putPlainText(self,text):
        self.text.setPlainText(text)
        if self.lineEdit.text().strip() != '' and re.match(r'\d{8}', self.lineEdit.text()):
            if self.getStatus == 0:
                self.button.setText("请等待！")
                self.button.setDisabled(True)
            else:
                self.button.setText("点击查询")
                self.button.setDisabled(False)
                self.getStatus = 0
        QApplication.processEvents();

    def btnstate(self, btn):
        if btn.text() == 'adb' and btn.isChecked() == True:
            self.qtype = 'adb'
        if btn.text() == "console" and btn.isChecked() == True:
            self.qtype = 'console'

    def sendData(self,dataToSend):
        try:
            command = dataToSend + '\r\n'
            serPort = self.ser
            atCommand = command.encode("UTF-8")
            serPort.write(atCommand)
        except:
            pass

if __name__ =="__main__":
    app = QApplication(sys.argv)
    QueryMaiaWin = MainWin()
    QueryMaiaWin.show()
    sys.exit(app.exec())