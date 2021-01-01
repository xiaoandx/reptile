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
 @Version: V1.7
 @Others:  Running test instructions
            v1.7.0 说明
                1. 修改窗口GUI布局，限定窗口的指定大侠不可以放大；添加页面内容，使其丰富
                2. 添加按钮样式，按钮全部修改样式为黑底白字
                3. 添加小组成员，添加小组成员的头像
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
    """
        绘制四川各城市分类柱状图 按钮绑定函数
    """
    countryDataByRegion(countryData, region)
    pass


def runDrawChartByRegion():
    """
        绘制四川各城市感染总数柱状图 按钮绑定函数
    """
    drawChartByRegion(countryData, region)
    pass


def runDrawChartColumn():
    """
        绘制四川各城市疫情对比柱状图 按钮绑定函数
    """
    drawChartColumn(countryData, region)
    pass


def getApp():
    """
        获取窗口对象
    """
    return QApplication(sys.argv)


class Ui_MainWindow(object):
    """
        1.可视化GUI窗口创建与布局设置类\n
        2.setipUi设置窗口布局及按钮样式\n
        3.retranslateUi设置窗口中组件的属性（Text、clicked等）\n
        4.runDramMapByRegion运行生成疫情统计地图方法(与对应按钮绑定，点击才运行)\n
        5.runDramMapHotWords运行生成疫新闻高频词云方法(与对应按钮绑定，点击才运行)\n
    """

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(965, 793)
        MainWindow.setStyleSheet("")
        MainWindow.setWindowIcon(QIcon(const.WINDOW_ICO_PATH))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 691, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(150, 120, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color:red;\n"
                                         "background-color: #fff;\n"
                                         "font-size:18px;\n"
                                         "text-align: center;\n"
                                         "boder:0;\n"
                                         "padding-top:6px")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 200, 301, 41))
        self.pushButton.setStyleSheet("color:white;\n"
                                      "background-color: black;\n"
                                      "font-size:20px;\n"
                                      "text-align: left;\n"
                                      "padding-left:5px;\n"
                                      "border-radius:5px;")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 190, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-size:15px;\n"
                                   "line-height: 10em;\n"
                                   "padding-top:10px;")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 290, 301, 41))
        self.pushButton_2.setStyleSheet("color:white;\n"
                                        "background-color: black;\n"
                                        "font-size:20px;\n"
                                        "text-align: left;\n"
                                        "padding-left:5px;\n"
                                        "border-radius:5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 280, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-size:15px;\n"
                                   "line-height: 10em;\n"
                                   "padding-top:10px;")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 380, 301, 41))
        self.pushButton_3.setStyleSheet("color:white;\n"
                                        "background-color: black;\n"
                                        "font-size:20px;\n"
                                        "text-align: left;\n"
                                        "padding-left:5px;\n"
                                        "border-radius:5px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 370, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-size:15px;\n"
                                   "line-height: 10em;\n"
                                   "padding-top:10px;")
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 470, 301, 41))
        self.pushButton_4.setStyleSheet("color:white;\n"
                                        "background-color: black;\n"
                                        "font-size:20px;\n"
                                        "text-align: left;\n"
                                        "padding-left:5px;\n"
                                        "border-radius:5px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 560, 301, 41))
        self.pushButton_5.setStyleSheet("color:white;\n"
                                        "background-color: black;\n"
                                        "font-size:20px;\n"
                                        "text-align: left;\n"
                                        "padding-left:5px;\n"
                                        "border-radius:5px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 460, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-size:15px;\n"
                                   "line-height: 10em;\n"
                                   "padding-top:10px;")
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 550, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font-size:15px;\n"
                                   "line-height: 10em;\n"
                                   "padding-top:10px;")
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setObjectName("label_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 650, 301, 41))
        self.pushButton_6.setStyleSheet("color:white;\n"
                                        "background-color: black;\n"
                                        "font-size:20px;\n"
                                        "text-align: left;\n"
                                        "padding-left:5px;\n"
                                        "border-radius:5px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 660, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(740, 30, 221, 721))
        self.widget.setObjectName("widget")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(60, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(50, 70, 121, 131))
        self.toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton.setStyleSheet("border:none;")
        # zw
        icon = QtGui.QIcon()
        # lmr
        icon2 = QtGui.QIcon()
        # yx
        icon3 = QtGui.QIcon()
        # lsl
        icon4 = QtGui.QIcon()
        # dpc
        icon5 = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("file/img/ico/zw.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("file/img/ico/zw.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("file/img/ico/yx.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("file/img/ico/lsl.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("file/img/ico/dpc.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(100, 100))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.widget)
        self.toolButton_2.setGeometry(QtCore.QRect(50, 200, 121, 131))
        self.toolButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_2.setStyleSheet("border:none;")
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.widget)
        self.toolButton_3.setGeometry(QtCore.QRect(50, 330, 121, 131))
        self.toolButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_3.setStyleSheet("border:none;")
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.widget)
        self.toolButton_4.setGeometry(QtCore.QRect(50, 460, 121, 131))
        self.toolButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_4.setStyleSheet("border:none;")
        self.toolButton_4.setIcon(icon4)
        self.toolButton_4.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.widget)
        self.toolButton_5.setGeometry(QtCore.QRect(50, 590, 121, 131))
        self.toolButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_5.setStyleSheet("border:none;")
        self.toolButton_5.setIcon(icon5)
        self.toolButton_5.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_5.setObjectName("toolButton_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(180, 740, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
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
        self.label_2.setText(_translate("MainWindow", "提示信息："))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "项目提供以下功能，点击左边黑色功能按钮运行"))
        self.pushButton.setText(_translate("MainWindow", "绘制四川各城市分类柱状图"))
        self.pushButton.clicked.connect(runCountryDataByRegion)
        self.label_3.setText(_translate("MainWindow", "统计显示四川疫情各地区累计确诊人数、死亡人数\n"
                                                      "新增确诊、治愈人数柱状图"))
        self.pushButton_2.setText(_translate("MainWindow", "绘制四川各城市感染总数柱状图"))
        self.pushButton_2.clicked.connect(runDrawChartByRegion)
        self.label_4.setText(_translate("MainWindow", "统计显示四川疫情各地区累计感染人数柱状图"))
        self.pushButton_3.setText(_translate("MainWindow", "绘制四川各城市疫情对比柱状图"))
        self.pushButton_3.clicked.connect(runDrawChartColumn)
        self.label_5.setText(_translate("MainWindow", "统计显示四川疫情各地区疫情感染人数、死亡人数\n"
                                                      "治愈人数的对比柱状图"))
        self.pushButton_4.setText(_translate("MainWindow", "生成四川疫情感染统计地图"))
        self.pushButton_4.clicked.connect(self.runDramMapByRegion)
        self.pushButton_5.setText(_translate("MainWindow", "生成疫情热点新闻高频词云图"))
        self.pushButton_5.clicked.connect(self.runDramMapHotWords)
        self.label_6.setText(_translate("MainWindow", "爬虫生成四川各地区疫情累计感染人数地图\n"
                                                      "生成后直接打开,或根据提示信息查看"))
        self.label_7.setText(_translate("MainWindow", "爬取分析中国社会组织疫情防控新闻高频词汇\n"
                                                      "并生成词云图，直接打开,或根据提示信息查看"))
        self.pushButton_6.setText(_translate("MainWindow", "退出爬虫可视化GUI项目 quit"))
        self.pushButton_6.clicked.connect(QCoreApplication.instance().quit)
        self.label_8.setText(_translate("MainWindow", "项目开发版本：V1.7.0"))
        self.label_9.setText(_translate("MainWindow", "项目成员"))
        self.toolButton.setText(_translate("MainWindow", "姓名：周巍"))
        self.toolButton_2.setText(_translate("MainWindow", "姓名：刘梦如"))
        self.toolButton_3.setText(_translate("MainWindow", "姓名：杨雪"))
        self.toolButton_4.setText(_translate("MainWindow", "姓名：李世林"))
        self.toolButton_5.setText(_translate("MainWindow", "姓名：丁鹏程"))
        self.label_10.setText(_translate("MainWindow", "MIT License  Copyright (c) 2020 python Project team"))
        pass

    def runDramMapByRegion(self):
        """
            运行生成疫情统计地图方法 按钮绑定事件
        """
        dramMapByRegion(countryData, region)
        self.plainTextEdit.setPlainText("生成成功，前往 {}文件夹下查看网页地图".format(const.SAVE_MAP_PATH))
        pass

    def runDramMapHotWords(self):
        """
            运行新闻高频词云方法 按钮绑定事件
        """
        dramMapHotWords(const.SAVE_TXT_PATH)
        self.plainTextEdit.setPlainText("生成成功，前往 {}文件夹下查看词云地图".format(const.SAVE_MAP_PATH))
        pass


if __name__ == "__main__":
    """
        1.运行项目窗口GUI界面时候需要先获取全国最新的疫情数据\n
        2.数据获取成功后就调用QMainWindow() class 运行窗口
    """
    countryData = getCountryData(const.REQUEST_URL)
    region = '四川'
    app = getApp()
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
