from ast import Try
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QGridLayout, QComboBox, QLineEdit, QTextEdit
import sys
import os
import subprocess
import threading


def cmd(line):
    res = subprocess.getoutput(line)
    print(res)
    return res


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Test')
        grid = QGridLayout()
        self.resize(800, 600)
        self.button = QPushButton('Test', self)
        self.button.clicked.connect(self.button_clicked)
        self.button2 = QPushButton('Test2', self)
        self.button2.clicked.connect(self.button_clicked2)
        self.line = QLineEdit(self)
        self.lab = QTextEdit()
        self.combo = QComboBox()
        self.combo.activated.connect(self.combo_activated)
        grid.addWidget(self.line, 1, 0, 1, 2)
        grid.addWidget(self.button, 2, 0)
        grid.addWidget(self.button2, 2, 1)
        grid.addWidget(self.lab, 3, 0, 1, 2)
        grid.addWidget(self.combo, 4, 0, 1, 2)
        self.setLayout(grid)

    def ls(self):
        self.lab.setText(cmd('ls ' + self.line.text() + ' -la'))

    def button_clicked(self):
        self.ls()
        # t = threading.Thread(target=self.ls)
        # t.start()

    def button_clicked2(self):
        self.combo.clear()
        list = []
        for l in os.listdir(self.line.text()):
            self.combo.addItem(l)
            list.append(l)
        self.lab.setText('\n'.join(list))

    def combo_activated(self):
        self.lab.setText(cmd("file " + self.line.text() +
                         "/" + self.combo.currentText()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Test()
    test.show()
    app.exec_()
