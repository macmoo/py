import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import * # icon

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 윈도우 타이틀
        self.setWindowTitle("My PyQT v1.0")
        # 윈도우 사이즈
        self.setGeometry(300, 300, 400, 400)
        # 타이틀바 아이콘
        # not working
        self.setWindowIcon(QIcon("icon02.png"))
 
print(sys.argv)

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()


# https://wikidocs.net/70844