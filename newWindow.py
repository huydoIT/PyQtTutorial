# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newWindow(object):
    def setupUi(self, newWindow):
        newWindow.setObjectName("newWindow")
        newWindow.resize(471, 132)
        self.centralwidget = QtWidgets.QWidget(newWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        newWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(newWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 21))
        self.menubar.setObjectName("menubar")
        newWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(newWindow)
        self.statusbar.setObjectName("statusbar")
        newWindow.setStatusBar(self.statusbar)

        self.retranslateUi(newWindow)
        QtCore.QMetaObject.connectSlotsByName(newWindow)

    def retranslateUi(self, newWindow):
        _translate = QtCore.QCoreApplication.translate
        newWindow.setWindowTitle(_translate("newWindow", "New Window"))
        self.label.setText(_translate("newWindow", "The new windows called"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newWindow = QtWidgets.QMainWindow()
    ui = Ui_newWindow()
    ui.setupUi(newWindow)
    newWindow.show()
    sys.exit(app.exec_())

