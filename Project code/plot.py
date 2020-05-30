# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QBarCategoryAxis, QChartView, QPercentBarSeries, QBarSet, QPieSlice, QPieSeries
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class Ui_MainWindow3(object):

    def __init__(self,list1,features1):
        self.lst=list1
        self.features=features1


    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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

        #
        #print(self.dataframe1['import'])

        series = QPieSeries()
        series.append(self.features[0], self.lst[0])
        series.append(self.features[1], self.lst[1])
        series.append(self.features[2], self.lst[2])
        series.append(self.features[3], self.lst[3])


        # adding slice
        # slice = QPieSlice()
        # slice = series.slices()[2]
        # slice.setExploded(True)
        # slice.setLabelVisible(True)
        # slice.setPen(QPen(Qt.darkGreen, 2))
        # slice.setBrush(Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart of File 1")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        MainWindow.setCentralWidget(chartview)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
