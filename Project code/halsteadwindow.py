# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'halsteadwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from tkinter.filedialog import askopenfilename

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os

from math import log2
import pandas as pd
import openpyxl
import sys

import os, os.path


class Ui_MainWindow1(object):
    def buttonaction(self):
        self.file = QFileDialog.getOpenFileName(None, "Window name", "", "Python files (*.py)")
        path = self.file[0]
        self.pathIs = os.path.basename(path)
        self.label_2.setText("File Name : " + self.pathIs)

    def returnpath(self):
        return self.pathIs

    # print(self.file)
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(776, 941)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 20, 161, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(580, 20, 161, 41))
        self.pushButton1.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 0, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 170, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 80, 400, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 230, 277, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(340, 230, 277, 621))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_22.setObjectName("label_22")
        self.verticalLayout_2.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_2.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_2.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_2.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_27.setObjectName("label_27")
        self.verticalLayout_2.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_2.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_29.setObjectName("label_29")
        self.verticalLayout_2.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(85, 170, 255);")
        self.label_30.setObjectName("label_30")
        self.verticalLayout_2.addWidget(self.label_30)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #
    # def openFileNameDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
    #                                               "All Files (*);;Python Files (*.py)", options=options)
    #     if fileName:
    #         print(fileName)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Healstead Details", "Healstead Details"))
        self.pushButton.setText(_translate("MainWindow", "Please Select File"))
        self.pushButton1.setText(_translate("MainWindow", "RUN"))

        self.pushButton1.clicked.connect(self.healstead_details)

        self.label.setText(_translate("MainWindow", "Halstead Details"))
        self.label_2.setText(_translate("MainWindow", "File Name:"))
        self.label_3.setText(_translate("MainWindow", "Total Lines:"))
        self.label_11.setText(_translate("MainWindow", "Blank Lines:"))
        self.label_5.setText(_translate("MainWindow", "Comment Lines:"))
        self.label_12.setText(_translate("MainWindow", "Code Lines:"))
        self.label_9.setText(_translate("MainWindow", "N (Halstead Program Length):"))
        self.label_8.setText(_translate("MainWindow", "n (Halstead Vocabulary):"))
        self.label_7.setText(_translate("MainWindow", "V (Program Volume):"))
        self.label_10.setText(_translate("MainWindow", "D (Program Difficulty):"))
        self.label_6.setText(_translate("MainWindow", "E (Programming Effort):"))
        self.label_14.setText(_translate("MainWindow", "L (Language level):"))
        self.label_4.setText(_translate("MainWindow", "I (Intelligence Content):"))
        self.label_13.setText(_translate("MainWindow", "T (Programming time):"))
        self.label_15.setText(_translate("MainWindow", "N^ (Estimated program length):"))
        self.label_16.setText(_translate("MainWindow", "L^ (Estimated language level):"))
        # self.label_17.setText(_translate("MainWindow", self.lineCount))

        # self.label_18.setText(_translate("MainWindow", "0"))
        # self.label_19.setText(_translate("MainWindow", "0"))
        # self.label_20.setText(_translate("MainWindow", "0"))
        # self.label_21.setText(_translate("MainWindow", "0"))
        # self.label_22.setText(_translate("MainWindow", "0"))
        # self.label_23.setText(_translate("MainWindow", "0"))
        # self.label_24.setText(_translate("MainWindow", "0"))
        # self.label_25.setText(_translate("MainWindow", "0"))
        # self.label_26.setText(_translate("MainWindow", "0"))
        # self.label_27.setText(_translate("MainWindow", "0"))
        # self.label_28.setText(_translate("MainWindow", "0"))
        # self.label_29.setText(_translate("MainWindow", "0"))
        # self.label_30.setText(_translate("MainWindow", "0"))

        self.fileName = ""
        # print(self.fileName)
        self.pushButton.clicked.connect(self.buttonaction)

    def healstead_details(self):

        symbolofComment = "#"

        operatorsFileName = "operators"
        programFileName = self.pathIs
        #print(programFileName)

        operators = {}
        operands = {}

        with open(operatorsFileName) as f:
            for op in f:
                operators[op.replace('\n', '')] = 0

        isAllowed = True

        with open(programFileName) as f:
            for line in f:
                line = line.strip("\n").strip(' ')

                if (line.startswith("/*")):
                    isAllowed = False

                if ((not line.startswith("//")) and isAllowed == True and (not line.startswith('#'))):
                    for key in operators.keys():
                        operators[key] = operators[key] + line.count(key)
                        line = line.replace(key, ' ')
                    for key in line.split():
                        if key in operands:
                            operands[key] = operands[key] + 1
                        else:
                            operands[key] = 1

                if (line.endswith("*/")):
                    isAllowed = True

        n1, N1, n2, N2 = 0, 0, 0, 0

        #print("OPERATORS:\n")
        for key in operators:
            if (operators[key] > 0):
                if (key not in ")}]"):
                    n1, N1 = n1 + 1, N1 + operators[key]
                    #print("{} = {}".format(key, operators[key]))

        #print("\nOPERANDS\n")
        for key in operands.keys():
            if (operands[key] > 0):
                n2, N2 = n2 + 1, N2 + operands[key]
                #print("{} = {}".format(key, operands[key]))

        val = {"N": N1 + N2, "n": n1 + n2, "V": (N1 + N2) * log2(n1 + n2), "D": n1 * N2 / 2 / n2}
        val['E'] = val['D'] * val['V']
        val['L'] = val['V'] / val['D'] / val['D']
        val['I'] = val['V'] / val['D']
        val['T'] = val['E'] / (18)
        val['N^'] = n1 * log2(n1) + n2 * log2(n2)
        val['L^'] = 2 * n2 / N2 / n1

        unit = {'V': 'bits', 'T': 'seconds'}
        name = {'N': 'Halstead Program Length', 'n': 'Halstead Vocabulary', 'V': 'Program Volume',
                'D': 'Program Difficulty',
                'E': 'Programming Effort', 'L': 'Language level', 'I': 'Intelligence Content', 'T': 'Programming time',
                'N^': 'Estimated program length', 'L^': 'Estimated language level'}

        #print("\nThe various values are: ")
        # for key in val.keys():
        #     print("{} ({}) = {} {}".format(key, name[key], val[key], unit[key] if key in unit else ''))

        acceptableFileExtensions = programFileName
        if not acceptableFileExtensions:
            print('Please pass at least one file extension as an argument.')
            quit()

        currentDir = os.getcwd()

        # filesToCheck = []
        # for root, _, files in os.walk(currentDir):
        #     for f in files:
        #         fullpath = os.path.join(root, f)
        #         if '.git' not in fullpath:
        #             for extension in acceptableFileExtensions:
        #             	if fullpath.endswith(extension):
        # #                     filesToCheck.append(fullpath)
        #
        # if not filesToCheck:
        #     print ('No files found.')
        #     quit()

        lineCount = 0
        totalBlankLineCount = 0
        totalCommentLineCount = 0

        #print('')
        #print('Filename\tlines\tblank lines\tcomment lines\tcode lines')

        with open(programFileName) as f:

            fileLineCount = 0
            fileBlankLineCount = 0
            fileCommentLineCount = 0

            for line in f:
                lineCount += 1
                fileLineCount += 1
                lineWithoutWhitespace = line.strip()
                if not lineWithoutWhitespace:
                    totalBlankLineCount += 1
                    fileBlankLineCount += 1
                elif lineWithoutWhitespace.startswith(symbolofComment):
                    totalCommentLineCount += 1
                    fileCommentLineCount += 1

        #     print(os.path.basename(programFileName) + \
        #           "\t\t" + str(fileLineCount) + \
        #           "\t\t" + str(fileBlankLineCount) + \
        #           "\t\t\t" + str(fileCommentLineCount) + \
        #           "\t\t\t\t" + str(fileLineCount - fileBlankLineCount - fileCommentLineCount))
        #
        # print('')
        # print('Totals')
        # print('--------------------')
        # print('Lines:         ' + str(lineCount))
        # print('Blank lines:   ' + str(totalBlankLineCount))
        # print('Comment lines: ' + str(totalCommentLineCount))
        codelines = lineCount - totalBlankLineCount - totalCommentLineCount
        # print('Code lines:    ' + str(codelines))

        self.label_17.setText(str(lineCount))

        self.label_18.setText(str(totalBlankLineCount))

        self.label_19.setText(str(totalCommentLineCount))

        self.label_20.setText(str(codelines))

        self.label_21.setText(str(val.get("N")))

        self.label_22.setText(str(val.get("n")))

        self.label_23.setText(str(val.get("V"))+" bits")

        self.label_24.setText(str(val.get("D")))

        self.label_25.setText(str(val.get("E")))

        self.label_26.setText(str(val.get("L")))

        self.label_27.setText(str(val.get("I")))

        self.label_28.setText(str(val.get("T"))+" seconds")

        self.label_29.setText(str(val.get("N^")))

        self.label_30.setText(str(val.get("L^")))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
