#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : TranslatorWidget.py.py
# @Author   : jade
# @Date     : 2022/11/3 13:23
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from main import Ui_MainWindow

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # #  翻译家
        self.trans = QTranslator()
        #
        # # 连接到槽函数
        self.BtnCh.clicked.connect(self.select_English)
        self.BtnEn.clicked.connect(self.select_Chinese)

    def select_Chinese(self):
        print("切换成中文")
        self.trans.load('zh_CN')
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)

    def select_English(self):
        print("切换成英文")

        _app = QApplication.instance()
        _app.removeTranslator(self.trans)
        self.retranslateUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
