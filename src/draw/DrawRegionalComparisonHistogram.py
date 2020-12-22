#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description: Seaborn绘制地区对比柱状图
 @File: DrawRegionalComparisonHistogram.py
 @Author: WEI.ZHOU
 @Date: 2020-12-19 13:02:51
 @Version: V1.0
 @Others:  Running test instructions
"""
import os
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from commons.GetCOVIDData import findRegionDataList
from commons.SaveFile import saveCSVByRegionContrast
from commons.Constant import const


def drawChartColumn(data, region):
    """
    绘制区域内城市对比柱状图
    :param data: 全部疫情数据
    :param region: 区域名称 如：四川
    :return:
    """
    n = const.SAVE_CSV_PATH + time.strftime("%Y-%m-%d") + "-" + region + "-cont.csv"
    if not os.path.exists(n):
        saveCSVByRegionContrast(findRegionDataList(data, region))
    data = pd.read_csv(n)
    # 设置窗口
    fig, ax = plt.subplots(1, 1)
    print(data['province'])
    # 设置绘图风格及字体
    sns.set_style("whitegrid", {'font.sans-serif': ['simhei', 'Arial']})
    # 绘制柱状图
    g = sns.barplot(x="province", y="data", hue="tpye", data=data, ax=ax,
                    palette=sns.color_palette("hls", 8))
    # 设置Axes的标题
    ax.set_title(region + '疫情最新对比情况')
    # 设置坐标轴文字方向
    ax.set_xticklabels(ax.get_xticklabels(), rotation=-60)
    # 设置坐标轴刻度的字体大小
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    plt.show()
    pass
