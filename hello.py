# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from newWindow import Ui_newWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(304, 207)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/coronavirus.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btClick = QtWidgets.QPushButton(self.centralwidget)
        self.btClick.setGeometry(QtCore.QRect(100, 30, 101, 41))
        self.btClick.setObjectName("btClick")

        self.btClick.clicked.connect(self.bt_click)
        
        self.btOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btOpen.setGeometry(QtCore.QRect(80, 90, 141, 51))
        self.btOpen.setObjectName("btOpen")

        self.btOpen.clicked.connect(self.bt_open)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 304, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hello App"))
        self.btClick.setText(_translate("MainWindow", "Click me!"))
        self.btOpen.setText(_translate("MainWindow", "Open new window"))

    def bt_click(self):
        print("Button clicked!!")

    def bt_open(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_newWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

