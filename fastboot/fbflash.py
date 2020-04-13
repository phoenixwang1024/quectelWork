# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:31:51 2019
@author: phoenix.wang
"""
import os,serial,datetime,time,requests,re,subprocess
import xml.etree.ElementTree as ET

class Update(object):

    #  获取xml文件路劲和要生成的bat文件名称
    def getPath( ):
        global batName
        global filePath
        global dirPath
        global execBatFlag
        global updateDir
        while True:
            dirPath = input('输入版本包路径，或者把包文件夹拖到此处：>>> ')
            filePath = dirPath + r'\update\partition_nand.xml'
            updateDir = dirPath + r'\update'
            if os.path.isdir(updateDir):
                if not os.path.exists(filePath):
                    print('未找到partition.xml文件，请确保路径是否正确并重试！\n')
                else:
                    break
            else:
                print('请确保输入路径为文件夹，而不是文件！')

        # batNameInput = input('输bat名称,不带.bat后缀,缺省将以版本名称命名:>>> ')
        # if batNameInput == '':
        version = os.path.split(dirPath)[1]
        batName = version + '_flash.bat'
        # else:
        #     batName = batNameInput + '.bat'

    def makeBat(filePath,batName):
        fbat = open('./'+batName,'w+')

        fbat.write('set path=' + updateDir +'\r\n')
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
                            if a2  == 'appsboot.mbn':
                                continue
                            else:
                                fbat.seek(0, 2)
                                strToWrite = 'fastboot flash ' + a1+ ' %path%\\' + a2 + '\r\n'
                                fbat.write(strToWrite)

        fbat.write('\r\nfastboot reboot\r\npause')
        fbat.close()
        print(' bat文件生成成功，文件路径: ', os.path.abspath(batName))

    def fastbootFlashUpdate(countTarget = 10, autoUpdateFlag = 1):
        count =0
        while autoUpdateFlag:
            pass

    def queryKey():
        try:
            serPort = serial.Serial(SPN, baudRate, bytesize=8, parity='N', stopbits=1, timeout=1)
            checkPort = serPort.isOpen()
            if checkPort:
                serPort.close()
        except serial.serialutil.SerialException as e:
            serPort.close()
        serPort = serial.Serial(SPN, baudRate, bytesize=8, parity='N', timeout=1, xonxoff=False, rtscts=False,write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
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

    def serialOpen(SPN,baudRate):
        global serPort
        try:
            serPort = serial.Serial(SPN, baudRate, bytesize=8, parity='N', stopbits=1, timeout=1)
            checkPort = serPort.isOpen()
            if checkPort:
                serPort.close()
                serPort = serial.Serial(SPN, baudRate, bytesize=8, parity='N', timeout=1, xonxoff=False, rtscts=False,
                                        write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
                serOut = serPort.read(size=1024)
                string_AT_R = serOut.decode(encoding="utf-8", errors="strict")
                string_AT_R_array = string_AT_R.split('\r\n')
                for i in string_AT_R_array:
                    print(time.strftime("[serial:%Y-%m-%d %H:%M:%S]:", time.localtime()) + i + "\r\n")
        except serial.serialutil.SerialException as e:
                print("Error happens: ", e)
                serPort.close()

    def excuteCommand(command,adbFlag=1, adbkeyFlag=0):
        global adbKey
        atCommand = command.encode('utf-8')
        serPort.write(atCommand)
        #  串口执行AT指令，funcFlag默认1，会返回上报信息
        if adbFlag == 1:
            print(time.strftime("[input:%Y-%m-%d %H:%M:%S]:", time.localtime()) + command.replace('\r\n',''))
            serOut = serPort.read(size=1024)
            string_AT_R = serOut.decode(encoding="utf-8", errors="strict")
            string_AT_R_array = string_AT_R.split('\r\n')
            for i in string_AT_R_array:
                print(time.strftime("[response:%Y-%m-%d %H:%M:%S]:", time.localtime()) + i + "\r\n")
                if adbkeyFlag:
                    adbKeyRegex = re.compile('\+QADBKEY: ([\d]*)')
                    adbKeyResult = re.findall(adbKeyRegex, i)
                    if adbKeyResult:
                        adbKey = adbKeyResult[0]
                        return adbKey

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

if __name__ == "__main__":
    # SPN = 'com4'
    # baudRate = 115200
    # serialType = 'uart1'
    # Update.serialOpen(SPN,baudRate)
    # Update.excuteCommand("ate1\r\n")
    # Update.excuteCommand("ati+csub\r\n")
    # adbKey = Update.excuteCommand("at+qadbkey?\r\n", adbFlag=1)
    # adbkeySetCommand = "AT+QADBKEY=" + adbkeyQuery
    # print(adbkeySetCommand)
    # Update.excuteCommand(adbkeySetCommand)
    # print(adbKey)
    Update.getPath()
    Update.makeBat(filePath, batName)
    os.system('pause')
