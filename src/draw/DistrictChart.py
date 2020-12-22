#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description: 绘制地区统计图
 @File: districtChart.py
 @Author: WEI.ZHOU
 @Date: 2020-12-19 12:25:14
 @Version: V1.0
 @Others:  Running test instructions
"""
import os
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from commons.SaveFile import saveCSVByRegion
from commons.Constant import const
from commons.GetCOVIDData import findRegionDataList


def countryDataByRegion(data, region):
    """
    绘制地区各城市柱状图（确诊、死亡、治愈、新增）
    :param data: 全部疫情数据
    :param region: 区域名称 如：四川
    :return:
    """
    regionDataList = findRegionDataList(data, region)
    # 绘制柱状图
    plt.figure(figsize=[10, 6])
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 1.绘制确诊数据
    p1 = plt.subplot(221)
    names = regionDataList[1].keys()
    nums = regionDataList[1].values()
    plt.bar(names, nums, width=0.3, color='green')
    # 设置标题
    plt.xlabel("地区")
    plt.ylabel(regionDataList[0] + "确诊人数", rotation=90)
    plt.xticks(list(names), rotation=-60, size=8)
    # 显示数字
    for a, b in zip(list(names), list(nums)):
        plt.text(a, b, b, ha='center', va='bottom', size=6)
    plt.sca(p1)

    # 2.绘制新增确诊数据
    p2 = plt.subplot(222)
    names = regionDataList[5].keys()
    nums = regionDataList[5].values()
    plt.bar(names, nums, width=0.3, color='yellow')
    plt.xlabel("地区")
    plt.ylabel(regionDataList[0] + "新增确诊人数", rotation=90)
    plt.xticks(list(names), rotation=-60, size=8)
    # 显示数字
    for a, b in zip(list(names), list(nums)):
        plt.text(a, b, b, ha='center', va='bottom', size=6)
    plt.sca(p2)

    # 3.绘制死亡数据
    p3 = plt.subplot(223)
    names = regionDataList[3].keys()
    nums = regionDataList[3].values()
    plt.bar(names, nums, width=0.3, color='blue')
    plt.xlabel("地区")
    plt.ylabel(regionDataList[0] + "死亡人数", rotation=90)
    plt.xticks(list(names), rotation=-60, size=8)
    for a, b in zip(list(names), list(nums)):
        plt.text(a, b, b, ha='center', va='bottom', size=6)
    plt.sca(p3)

    # 4.绘制治愈数据
    p4 = plt.subplot(224)
    names = regionDataList[4].keys()
    nums = regionDataList[4].values()
    plt.bar(names, nums, width=0.3, color='red')
    plt.xlabel("地区")
    plt.ylabel(regionDataList[0] + "治愈人数", rotation=90)
    plt.xticks(list(names), rotation=-60, size=8)
    for a, b in zip(list(names), list(nums)):
        plt.text(a, b, b, ha='center', va='bottom', size=6)
    plt.sca(p4)
    plt.show()
    pass


def drawChartByRegion(data, region):
    """
    绘制地区城市统计柱状图
    :param data: 全部疫情数据
    :param region: 区域名称 如：四川
    :return:
    """
    n = const.SAVE_CSV_PATH + time.strftime("%Y-%m-%d") + "-" + region + "-all.csv"
    if not os.path.exists(n):
        saveCSVByRegion(findRegionDataList(data, region))
    data = pd.read_csv(n)
    # 设置窗口
    fig, ax = plt.subplots(1, 1)
    # 设置绘图风格及字体
    sns.set_style("whitegrid", {'font.sans-serif': ['simhei', 'Arial']})
    # 绘制柱状图
    g = sns.barplot(x="province", y="confirm", data=data, ax=ax,
                    palette=sns.color_palette("hls", 8))
    # 在柱状图上显示数字
    i = 0
    for index, b in zip(list(data['province']), list(data['confirm'])):
        g.text(i + 0.05, b + 0.05, b, color="black", ha="center", va='bottom', size=6)
        i = i + 1
    # 设置Axes的标题
    ax.set_title(region + '疫情最新情况')
    # 设置坐标轴文字方向
    ax.set_xticklabels(ax.get_xticklabels(), rotation=-60)
    # 设置坐标轴刻度的字体大小
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    plt.show()
    pass
