import sys
import gptcmt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFile, QTextStream
from PyQt5 import uic

form_class = uic.loadUiType("HelloWorld.ui")[0]

class MyApp(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 파일 트리 생성
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(''))  # 전체 파일 시스템을 보여주기 위해 루트 인덱스 설정
        self.treeView.setColumnWidth(0, 250)  # 열 너비 조정

        # 버튼과 연결
        self.btn_cmt.clicked.connect(self.printCommentingCode)

        # 파일 선택 이벤트 연결
        self.treeView.selectionModel().selectionChanged.connect(self.loadFileContent)

    def loadFileContent(self):
        selected_index = self.treeView.selectedIndexes()[0]
        file_path = self.model.filePath(selected_index)
        if QFile.exists(file_path):
            file = QFile(file_path)
            file.open(QFile.ReadOnly | QFile.Text)
            stream = QTextStream(file)
            content = stream.readAll()
            self.code_before.setPlainText(content)
            file.close()

    def printCommentingCode(self):
        txt = self.code_before.toPlainText()
        if txt != "":
            cmtcode = gptcmt.generate_comment(txt)
            self.code_cmt.setPlainText(cmtcode)
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('코드에 주석 달기')
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())

