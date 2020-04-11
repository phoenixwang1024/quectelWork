import sys,re,time
import urllib.request
import http.cookiejar
from urllib import request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer

class QcPwdClass(QWidget):

    def __init__(self, parent=None):
        super(QcPwdClass, self).__init__(parent)
        self.qtype = 'adb'
        self.label = QLabel(self)
        self.label.setText("序号")
        self.lineEdit = QLineEdit()
        self.button = QPushButton("点击查询")
        self.text = QTextEdit()
        self.text.setPlainText("请输入8位序号！")

        self._adbButton = QRadioButton("adb")
        self._consoleButton = QRadioButton("console")
        #信号于槽
        self.button.clicked.connect(self.getstr)
        #布局嵌套
        wlayout = QVBoxLayout(self) #全局布局
        hlayout01 = QHBoxLayout() #局部布局
        hlayout02 = QHBoxLayout()  # 局部布局
        vlayout = QVBoxLayout() #局部布局

        hlayout01.addWidget(self.label)
        hlayout01.addWidget(self.lineEdit)

        hlayout02.addWidget(self._adbButton)
        hlayout02.addWidget(self._consoleButton)
        self._adbButton.toggled.connect(lambda: self.btnstate(self._adbButton))
        self._consoleButton.toggled.connect(lambda: self.btnstate(self._consoleButton))
        hlayout02.addWidget(self.button)

        vlayout.addWidget(self.text)

        # 将局部布局加到全局布局中
        wlayout.addLayout(hlayout01)
        wlayout.addLayout(hlayout02)
        wlayout.addLayout(vlayout)

        self._adbButton.setChecked(True)
        #添加标题
        self.setWindowTitle("Debug安全登录")
        self.setGeometry(300, 300, 250, 110)
        # 屏幕中心打开
        self.center()
        #添加图标
        #self.setWindowIcon(QIcon('1.ico'))
        self.timer = QBasicTimer()
        self.step = 9
        self.getStatus=0
    def btnstate(self, btn):
        if btn.text() == 'adb' and btn.isChecked() == True:
            self.qtype = 'adb'
        if btn.text() == "console" and btn.isChecked() == True:
            self.qtype = 'console'


    #槽函数
    def getstr(self):
        queryId = self.lineEdit.text()
        key = ''
        if queryId.strip() != '' and re.match(r'\d{8}', queryId):
           # 先去遍历历史生成的秘钥
            self.putPlainText("正在帮您查询历史秘钥！请稍等！！！")
            key = paserKeyClass().getPaserKey(queryId, self.qtype)
            # 找不到，再去重新生成
            if key == '':
                self.putPlainText("没有找到历史秘钥！正在帮您重新生成！请稍等！！！请不要关闭窗口！！！！！")
                paserKeyClass().createPwd(queryId, self.qtype)
                time.sleep(1)
                key = paserKeyClass().getPaserKey(queryId, self.qtype)
                time.sleep(1)
            if key == '':
                key = '暂时未查到密钥！后续优化获取的方法！'
            self.getStatus = 1
        else:
            key = "请输入8位序号！"
        self.putPlainText(key)



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

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

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


if __name__ =="__main__":
    app = QApplication(sys.argv)
    demo = QcPwdClass()
    demo.show()
    sys.exit(app.exec())