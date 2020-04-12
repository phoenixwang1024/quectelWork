import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class spindemo(QWidget):
    def __init__(self,parent=None):
        super(spindemo, self).__init__(parent)
        #设置标题与初始大小
        self.setWindowTitle('SpinBox 例子')
        self.resize(300,100)

        #垂直布局
        layout=QVBoxLayout()

        #创建按钮并设置居中
        self.l1=QLabel('current value')
        self.l1.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.l1)

        #创建计数器，并添加控件，数值改变时发射信号触发绑定事件
        self.sp=QSpinBox()
        layout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.Valuechange)


        self.setLayout(layout)

    def Valuechange(self):
        #显示当前计数器地数值
        self.l1.setText('current value:'+str(self.sp.value()))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=spindemo()
    ex.show()
    sys.exit(app.exec_())
