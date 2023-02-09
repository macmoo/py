import sys
from PyQt5.QtWidgets import *

print(sys.argv)
# => ['d:/200.dev/201.src/20.python/py/macro/0209_04_PyQt.py']

app = QApplication(sys.argv)
win = QWidget()
win.show()
app.exec_()


# https://wikidocs.net/119616
# READ
