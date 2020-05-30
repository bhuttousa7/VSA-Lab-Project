# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Similarity.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import os

import re

import nltk
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog, QMainWindow
import nltk

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


import copy
import numpy as np
import matplotlib
import matplotlib.pylab as plt
import matplotlib.pyplot as plt1

from plot import Ui_MainWindow3
from plot2 import Ui_MainWindow4

matplotlib.use('QT5Agg')
from matplotlib.figure import Figure


features = ['print', 'pandas', 'pd', 'import']

ngram_value = 1


class Ui_MainWindow2(object):

    def newwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3(self.lst,features)
        self.ui.setup(self.window)
        self.window.show()

    def newwindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow4()
        self.ui.setup(self.window)
        self.window.show()

    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 110, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 170, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 561, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 120, 400, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 180, 400, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 310, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 310, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(910, 40, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")


        MainWindow.setCentralWidget(self.centralwidget)



        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)


    def buttonaction(self):
        self.file = QFileDialog.getOpenFileName(None, "Open File 1", "", "Python files (*.py)")
        path = self.file[0]
        self.pathFile1 = os.path.basename(path)
        self.label_2.setText("File 1 : " + self.pathFile1)

    def buttonaction2(self):
        self.file = QFileDialog.getOpenFileName(None, "Open File 2 ", '/home/', "Python files (*.py)")
        path = self.file[0]
        self.pathFile2 = os.path.basename(path)
        self.label_3.setText("File 2 : " + self.pathFile2)

    def read_file_n_gram(self, file_path):
        try:
            with open(file_path) as f:
                s = ''
                for line in f.readlines():
                    s = s + line
                return s
        except Exception as e:
            print(e.__str__)

    def normalize(self, lines):
        replaceLines = lines
        normalizedLines = ''
        for line in replaceLines.split('\n'):
            s = ''
            for word in line.split(' '):
                if word not in features:
                    line = line.replace(word, '')
            normalizedLines += line
        return normalizedLines

    def assign_value(self, vector):
        vcopy = copy.deepcopy(self.feature_vector)
        for vec in vcopy:
            if vec in vector:
                vcopy[vec] = vector[vec]
        return vcopy

    def similarityAlgorithm(self):

        file1 = self.read_file_n_gram(self.pathFile1)

        file2 = self.read_file_n_gram(self.pathFile2)

        FILE1 = self.normalize(file1)
        FILE2 = self.normalize(file2)

        tk_words1 = nltk.word_tokenize(FILE1)
        tk_words2 = nltk.word_tokenize(FILE2)

        self.feature_vector = {}
        fv = nltk.ngrams(features, ngram_value)
        for f in fv:
            self.feature_vector[f] = 0

        ngram1 = nltk.ngrams(tk_words1, ngram_value)
        ngram2 = nltk.ngrams(tk_words2, ngram_value)

        freq_file1 = nltk.FreqDist(ngram1)
        freq_file2 = nltk.FreqDist(ngram2)

        f1 = self.assign_value(freq_file1)
        f2 = self.assign_value(freq_file2)
        self.df1 = pd.DataFrame([f1])
        df2 = pd.DataFrame([f2])



        res = cosine_similarity(self.df1.values, df2.values)
        print("Cosine Similarity:", float(res))
        self.label_5.setText(str(float(res)))
        #self.df1.plot(kind='bar', x='BLOC', y='LOC')
        self.lst=[]
        self.lst1=[]


        for key in f1.keys():
            self.lst.append(f1.get(key))
            # cleanString = re.sub('\W+', '', f1.keys())

        for key in f2.keys():
            self.lst1.append(f2.get(key))
            # cleanString = re.sub('\W+', '', f1.keys())

        names = []
        for i in range(len(features)):
            names.append(features[i])
        print(names)

        values = self.lst
        values1=self.lst1
        plt1.figure(figsize=(13, 6))

        plt1.subplot(131)
        plt1.bar(names, values)
        plt1.subplot(132)
        plt1.bar(names, values1)




        plt1.suptitle('Categorical Plotting of Both Files ')
        plt1.show()

        self.newwindow()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open File 1 "))
        self.pushButton_2.setText(_translate("MainWindow", "Open File 2"))
        self.label.setText(_translate("MainWindow", "Similarity Using Cosine and Feature Matrix"))
        self.label_4.setText(_translate("MainWindow", "Cosine Similarity: "))
        self.pushButton_3.setText(_translate("MainWindow", "RUN "))

        self.pushButton.clicked.connect(self.buttonaction)

        self.pushButton_2.clicked.connect(self.buttonaction2)
        self.pushButton_3.clicked.connect(self.similarityAlgorithm)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setup(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
