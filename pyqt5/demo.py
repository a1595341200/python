#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import ip
import route
from PyQt5.QtWidgets import (
    QTextEdit, QAction, QMenu, QMainWindow, QApplication)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('配置')
        self.routeAct = QAction('route', self)
        self.ipAct = QAction('ip', self)
        fileMenu.addAction(self.ipAct)
        fileMenu.addAction(self.routeAct)
        self.ipAct.triggered.connect(self.AcrClicked)
        self.routeAct.triggered.connect(self.AcrClicked)

        self.showtext = QTextEdit()
        self.statusBar()
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Review')
        self.show()

    def AcrClicked(self):
        sender = self.sender()
        if sender == self.ipAct:
            w = ip.ipQWidget(self)
            self.setCentralWidget(w)
        elif sender == self.routeAct:
            pass
            w = route.routeQWidget(self)
            self.setCentralWidget(w)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
