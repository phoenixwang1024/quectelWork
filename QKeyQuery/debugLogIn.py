from PyQt5.QtCore import QTimer
import serial


class debugLogin():
    def open_port(self):
        try:
            self.ser = serial.Serial("COM27", 115200, bytesize=8, parity='N', timeout=0.8, xonxoff=False,
                                     rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
            self.timer.start(2)
            if self.ser.isOpen():
                print(self.comName + '打开成功')
        except:
            print("端口被占用，请检查后重试")
            self.timer.stop()
            self.ser.close()
        pass

    def send_data(self, data):
        # self.pushButton_QueryWithCom.setText("查询中")
        command = data + '\r\n'
        atCommand = command.encode('utf-8')
        self.ser.write(atCommand)

    # timer = QTimer()


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
            return at_result

            # 获取到text光标
            textCursor = self.textBrowser.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.textBrowser.setTextCursor(textCursor)
        else:
            pass

if __name__ == "__main__":
    debug = debugLogin()
    debug.open_port()
    # 定时器接收数据

    a = timer.timeout.connect(debug.data_receive)
    for item in a:
        i = item.decode('utf-8')
        print(i.readline())

