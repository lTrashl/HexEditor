# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from useMainWindow import useMainWindow
from test import unitTest

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = useMainWindow()
ui.setupUi(MainWindow)
ui.SetMainActions(app)

print(sys.argv)

if len(sys.argv) > 1:  # это самотестирование!
    test = unitTest()
    ui.ShowDialog = False
    ui.defaultrow = 5
    ui.value = "0x0000"
    test.run(ui)
else:
    ui.ShowDialog = True
    ui.defaultrow = -1
    ui.value = ""

    MainWindow.show()
    print("starting")
    code = app.exec_()
    sys.exit(code)
