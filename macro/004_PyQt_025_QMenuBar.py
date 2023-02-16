import sys
from PyQt5.QtWidgets import *

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000,400,400,300)

        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)

        # file menu
        self.newAction  = QAction("New")
        self.quitAction = QAction("Quit")
        self.quitAction.triggered.connect(self.close)

        # help menu
        self.docAction = QAction("Documentation")
        self.releaseACtion = QAction("Release Notes")
        self.licenseAction = 



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWin()
    win.show()
    app.exec_()

 # https://wikidocs.net/89416