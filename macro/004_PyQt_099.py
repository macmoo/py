import sys
from PyQt5.QtWidgets import *

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
win = MyWin()
win.show()
app.exec_()