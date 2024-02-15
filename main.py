## Ex 5-1. QPushButton.

import sys
import gptcmt
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("HelloWorld.ui")[0]
class MyApp(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #버튼과 연결
        self.btn_cmt.clicked.connect(self.printCommentingCode)


    def printCommentingCode(self):
        txt = self.code_before.toPlainText()
        if(txt != ""):
            cmtcode = gptcmt.generate_comment(txt)
            self.code_cmt.setPlainText(cmtcode)
        else:
            pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Commenting on the code')
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())




