

def excuteCommand(command,funcFlag=0):
    global adbKey
    atCommand = command.encode('utf-8')
    serPort.write(atCommand)

    if funcFlag == 1:
        #print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()) + command.replace('\r\n',''))
        serOut = serPort.read(size=1024)
        string_AT_R = serOut.decode(encoding="UTF-8", errors="strict")
        string_AT_R_array = string_AT_R.split('\r\n')
        for i in string_AT_R_array:
            print(time.strftime("[%Y-%m-%d %H:%M:%S]:", time.localtime()) + i + "\n")
            adbKeyRegex = re.compile(r'QADBKEY: ([\d]*)')
            adbKeyResult = re.findall(adbKeyRegex, i)
            if adbKeyResult:
                adbKey = adbKeyResult[0]
                return adbKey


#  查询debug密码，默认adb，可配置：qtyp='console'
def query_key(adbKey, qversion='v1.0', qtype='adb'):
    if adbKey:
        url1 = 'http://192.168.10.11:8080/job/query_key/build?delay=0sec'
        reResult = 1

        global header
        cookie = r'htmlAudioNotificationsEnabled=false; jenkins-timestamper-offset=-28800000; screenResolution=1920x1080; JSESSIONID.50763f5b=node0eed4ricnv1bc14enhx3mdkt4l937.node0'
        header={
            'Connection': 'keep-alive',
            'Cookie': cookie,
            'Host': '192.168.10.11:8080',
            'Origin': 'http://192.168.10.11:8080',
            'Referer': 'http://192.168.10.11:8080/job/query_key/build?delay=0sec',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        }

        formData = {}
        json = '{"parameter": [{"name": "qversion", "value": "'+ qversion + '"}, {"name": "ID", "value": "' + adbKey + '"}, {"name": "qtype", "value": "'+ qtype + '"}], "statusCode": "303", "redirectTo": "."}'
        formData['json'] = json
        formData['Submit'] = 'Build'
        #response1 = requests.post(url1, headers=header, data=formData)    #  发送adb key查询密码

        buildHistoryUrl = 'http://192.168.10.11:8080/job/query_key/buildHistory/all'
        response3 = requests.get(buildHistoryUrl, headers=header)
        idRegex = re.compile('<a update-parent-class=".build-row" href="/job/query_key/([\d]*)/" class="tip model-link inside build-link display-name">')
        #print('History request: ', response3.text)
        currentID = re.findall(idRegex, response3.text)[0]
        print('current: ', currentID)

        while reResult:
            url2 = 'http://192.168.10.11:8080/job/query_key/' + currentID + '/console'
            response2 = requests.get(url2, headers = header)
            #print(response2.status_code)
            #print(response2.text)
            adbRegex1 = re.compile('\+\+ sh genkey.sh v1.0 ([\d]+)')
            match_adb_key = re.findall(adbRegex1, response2.text)
            #print(match_adb_key)
            if match_adb_key[0] == adbKey:
                adbRegex2 = re.compile(r'您所查询的密钥为：(.*)')
                result = re.findall(adbRegex2, response2.text)
                debug_key = result[1]
                print('Key: ', debug_key)
                reResult = 0
                return debug_key
            else:
                currentID =str(int(currentID)-1)
    else:
        debug_key = 'quectel123'
        return debug_key


# 初始化函数
def preparation():
    excuteCommand("ATE1V1\r\n", 0)
    excuteCommand("AT+CMEE=1\r\n", 0)
    excuteCommand('AT+QURCCFG="URCPORT","uart1"\r\n', 0)
    excuteCommand("AT&W\r\n", 0)
