# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# import mysql.connector

# conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="user_db")
# cur = conn.cursor()


# def get_by_acc(name):
#     try:
#         sql = "SELECT * FROM account WHERE user =%s"
#
#         cur.execute(sql, (name,))
#         rs = cur.fetchone()
#         if not rs:
#             return None
#         else:
#             return rs
#     except:
#         conn.rollback()


acc = {'user': 'admin', 'pass': 'admin', 'name': 'DO HA DUC HUY'}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 362)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 361, 151))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.bt_cancel = QtWidgets.QPushButton(self.groupBox)
        self.bt_cancel.setGeometry(QtCore.QRect(160, 110, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_cancel.setFont(font)
        self.bt_cancel.setObjectName("bt_cancel")
        self.bt_cancel.clicked.connect(self.clear)
        self.bt_login = QtWidgets.QPushButton(self.groupBox)
        self.bt_login.setGeometry(QtCore.QRect(250, 110, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_login.setFont(font)
        self.bt_login.setObjectName("bt_login")
        self.bt_login.clicked.connect(self.login_check)
        self.txtUser = QtWidgets.QLineEdit(self.groupBox)
        self.txtUser.setGeometry(QtCore.QRect(120, 20, 201, 31))
        self.txtUser.setObjectName("txtUser")
        self.txtPass = QtWidgets.QLineEdit(self.groupBox)
        self.txtPass.setGeometry(QtCore.QRect(120, 60, 201, 31))
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setObjectName("txtPass")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 180, 361, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lbResult = QtWidgets.QLabel(self.groupBox_2)
        self.lbResult.setGeometry(QtCore.QRect(30, 40, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.lbResult.setFont(font)
        self.lbResult.setText("")
        self.lbResult.setObjectName("lbResult")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 290, 91, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.bt_cancel.setText(_translate("MainWindow", "Cancel"))
        self.bt_login.setText(_translate("MainWindow", "Login"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Infomation"))

    # def login_check(self):
        # db = get_by_acc(self.txtUser.text())
        # if not db:
        #     rs = "Username or password incorrect"
        # else:
        #     for row in db:
        #         if self.txtPass.text() == row[2]:
        #             rs = row[3]
        #     rs = "Account do not exits"
        # if self.txtUser.text() == acc["user"] and self.txtPass.text() == acc["pass"]:
        #     rs = "Hello " + acc['name']
        #     self.progressBar.setValue(100)
        # else:
        #     rs = "Account do not exits"
        # self.lbResult.setText(rs)

    def login_check(self):
        rs = "Account do not exits"
        f = open("db.txt", "r")
        for x in f:
            user, pwd, name = x.split("%")
            if self.txtUser.text() == user and self.txtPass.text() == pwd:
                rs = "Hello " + name
                self.progressBar.setValue(100)
        self.lbResult.setText(rs)

    def clear(self):
        self.txtUser.setText("")
        self.txtPass.setText("")
        self.lbResult.setText("")
        rs = "Account do not exits"
        f = open("db.txt", "r")
        print("User\tPass\tName")
        for x in f:
            a, b, c = x.split("%")
            print("%s\t%s\t%s" % (a, b, c))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

