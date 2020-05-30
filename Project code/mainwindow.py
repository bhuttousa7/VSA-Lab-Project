# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Similaritywindow import Ui_MainWindow2
from halsteadwindow import *

class Ui_MainWindow(object):
    def newwindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setup(self.window)
        self.window.show()

    def cosWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setup(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 357)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(98, 187, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.halsteadbtn = QtWidgets.QPushButton(self.centralwidget)
        self.halsteadbtn.setGeometry(QtCore.QRect(80, 80, 161, 61))
        self.halsteadbtn.setStyleSheet("background-color: rgb(102, 104, 255);\n"
"border-radius: 15px\n"
"")
        self.halsteadbtn.setObjectName("halsteadbtn")
        self.halsteadbtn.clicked.connect(self.newwindow)
        self.cosbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cosbtn.setGeometry(QtCore.QRect(330, 80, 171, 61))
        self.cosbtn.setStyleSheet("background-color: rgb(102, 104, 255);\n"
"border-radius: 15px\n"
"")
        self.cosbtn.setObjectName("cosbtn")

        self.cosbtn.clicked.connect(self.cosWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.halsteadbtn.setText(_translate("MainWindow", "Halstead "))
        self.cosbtn.setText(_translate("MainWindow", "Cosine and Feature Window"))
        self.label.setText(_translate("MainWindow", "Please Select a method to view"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
