from PyQt5.QtWidgets import *
import sys

class winform(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('内置的信号和自定义槽函数示例')
        self.resize(330 , 50)
        btn = QPushButton('关闭', self)
        btn.clicked.connect(self.btn_close)

    def btn_close(self):
        # 自定义槽函数
        print("Hello world~")
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = winform()
    win.show()
    sys.exit(app.exec_())