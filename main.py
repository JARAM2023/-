import sys
import gptcmt
from PyQt5.QtWidgets import *
from PyQt5 import uic
import dotenv

form_class = uic.loadUiType("HelloWorld.ui")[0]

class MyApp(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 버튼과 연결s
        self.btn_cmt.clicked.connect(self.printCommentingCode)

        # 수평 레이아웃 생성
        layout = QHBoxLayout()
        layout.addWidget(self.code_before)
        layout.addWidget(self.btn_cmt)
        layout.addWidget(self.code_cmt)

        # 중앙 위젯에 수평 레이아웃 설정
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def printCommentingCode(self):
        txt = self.code_before.toPlainText()
        if txt != "":
            cmtcode = gptcmt.generate_comment(txt)
            self.code_cmt.setPlainText(cmtcode)
        else:
            pass

if __name__ == '__main__':
    dotenv.load_dotenv()
    app = QApplication(sys.argv)
    app.setApplicationName('Commenting on the code')
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())




