import sys
import json
from PyQt5.QtWidgets import (QMessageBox, QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QMainWindow)


class routeQWidget(QWidget):

    def __init__(self, wd):
        super().__init__()
        self.wd = wd
        self.initUI()

    def initUI(self):
        self.ipBuutton = QPushButton('生成')
        self.appendBuutton = QPushButton('追加')
        self.ipBuutton.clicked.connect(self.buttonClicked)
        self.appendBuutton.clicked.connect(self.buttonClicked)

        self.iface = QLabel('iface')
        self.ip = QLabel('dest')
        self.mask = QLabel('mask')
        self.gw = QLabel('gw')

        self.ipEdit = QLineEdit()
        self.maskEdit = QLineEdit()
        self.gwEdit = QLineEdit()
        self.ifaceEdit = QLineEdit()

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.iface, 1, 0)
        self.grid.addWidget(self.ifaceEdit, 1, 1)

        self.grid.addWidget(self.ip, 2, 0)
        self.grid.addWidget(self.ipEdit, 2, 1)

        self.grid.addWidget(self.ipBuutton, 1, 2)
        self.grid.addWidget(self.appendBuutton, 2, 2)

        self.grid.addWidget(self.mask, 3, 0)
        self.grid.addWidget(self.maskEdit, 3, 1)

        self.grid.addWidget(self.gw, 4, 0)
        self.grid.addWidget(self.gwEdit, 4, 1)
        self.grid.addWidget(self.wd.showtext, 5, 0, 1, 3)
        self.setLayout(self.grid)

    def operator(self, type):
        data = {}
        if self.ipEdit.text().__len__() == 0:
            QMessageBox.warning(self, '警告', "dest格式不正确")
            return
        elif self.maskEdit.text().__len__() == 0:
            QMessageBox.warning(self, '警告', "mask格式不正确")
            return
        elif self.gwEdit.text().__len__() == 0:
            QMessageBox.warning(self, '警告', "gw格式不正确")
            return
        elif self.ifaceEdit.text().__len__() == 0:
            QMessageBox.warning(self, '警告', "iface格式不正确")
            return
        else:
            data["ip"] = self.ipEdit.text()
            data["mask"] = self.maskEdit.text()
            data["gw"] = self.gwEdit.text()
            data2 = json.dumps(
                data, sort_keys=False, indent=4, separators=(',', ': '))
            if type == 0:
                self.wd.showtext.clear()
                self.wd.showtext.setText(self.ifaceEdit.text()+": " + data2)
            else:
                self.wd.showtext.append(self.ifaceEdit.text()+": " + data2)

    def buttonClicked(self):
        sender = self.sender()
        if sender == self.ipBuutton:
            self.operator(0)
        elif sender == self.appendBuutton:
            self.operator(1)
