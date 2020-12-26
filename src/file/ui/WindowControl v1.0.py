#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description: 疫情统计窗口运行主函数
 @File: WindowControl.py
 @Author: WEI.ZHOU
 @Date: 2020-12-24 10:33:31
 @Version: V1.0
 @Others:  Running test instructions
"""
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from commons.Constant import const
from commons.GetCOVIDData import getCountryData
from draw.DistrictChart import countryDataByRegion, drawChartByRegion
from draw.DramMapByRegion import dramMapByRegion
from draw.DrawRegionalComparisonHistogram import drawChartColumn
from draw.StatisticalHighFrequencyWord import dramMapHotWords


def runCountryDataByRegion():
    countryDataByRegion(countryData, region)
    pass


def runDrawChartByRegion():
    drawChartByRegion(countryData, region)
    pass


def runDrawChartColumn():
    drawChartColumn(countryData, region)
    pass


def getApp():
    return QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(682, 340)
        MainWindow.setWindowIcon(QIcon(const.WINDOW_ICO_PATH))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 20, 664, 27))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 70, 661, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 210, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 150, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 150, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 210, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 270, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 270, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "疫情爬虫及可视化项目"))
        self.label.setText(_translate("MainWindow", "Python 地区(四川)疫情爬虫与新闻高频词云可视化项目"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "项目提供以下功能，点击功能按钮进行运行"))
        self.pushButton.setText(_translate("MainWindow", " 绘制地区各城市分类柱状图"))
        self.pushButton.setStyleSheet('''
            color:white;
	        background-color: black;
	        text-align: center;
	        border-radius:5px
        ''')
        self.pushButton.clicked.connect(runCountryDataByRegion)
        self.pushButton_2.setText(_translate("MainWindow", "绘制地区各城市疫情对比柱状图"))
        self.pushButton_2.clicked.connect(runDrawChartColumn)
        self.pushButton_3.setText(_translate("MainWindow", "绘制地区各城市感染总数柱状图"))
        self.pushButton_3.clicked.connect(runDrawChartByRegion)
        self.pushButton_4.setText(_translate("MainWindow", "绘制地区疫情统计地图"))
        self.pushButton_4.clicked.connect(self.runDramMapByRegion)
        self.pushButton_5.setText(_translate("MainWindow", "绘制疫情热门词汇展示"))
        self.pushButton_5.clicked.connect(self.runDramMapHotWords)
        self.pushButton_6.setText(_translate("MainWindow", "退出项目"))
        self.pushButton_6.clicked.connect(QCoreApplication.instance().quit)
        pass

    def runDramMapByRegion(self):
        dramMapByRegion(countryData, region)
        self.plainTextEdit.setPlainText("生成成功，前往 {}文件夹下查看网页地图".format(const.SAVE_MAP_PATH))
        pass

    def runDramMapHotWords(self):
        dramMapHotWords(const.SAVE_TXT_PATH)
        self.plainTextEdit.setPlainText("生成成功，前往 {}文件夹下查看词云地图".format(const.SAVE_MAP_PATH))
        pass


if __name__ == "__main__":
    countryData = getCountryData(const.REQUEST_URL)
    region = '四川'
    app = getApp()
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
