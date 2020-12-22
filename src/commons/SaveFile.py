#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description:  保存疫情爬虫项目数据
 @File: SaveFile.py
 @Author: WEI.ZHOU
 @Date: 2020-12-19 13:13:49
 @Version: V1.0
 @Others:  Running test instructions
"""
# 保存csv地区中各城市对比数据
import os
import time

import jieba

from .Constant import const
from collections import Counter

from .GetJournalism import getHotWords

def saveTxtFileByData(data, Type):
    """
    保存数据为txt
    :param Type:    数据类型；全国 或 地区（四川、广东...）
    :param data:   最新数据Json
    :return:
    """
    filePath = ''
    if Type == const.STATISTICAL_TYPE_COUNTRY:
        filePath = const.SAVE_TXT_PATH + time.strftime("%Y-%m-%d") + '-COVID_19_Chain.txt'
    else:
        filePath = const.SAVE_TXT_PATH + time.strftime("%Y-%m-%d") + '-COVID_19_REGION.txt'

    with open(filePath, 'a+', encoding="utf-8") as f:
        if Type == const.STATISTICAL_TYPE_COUNTRY:
            f.write(data + '\n')
        else:
            for i in range(len(data)):
                f.write(data[i])
    f.close()
    pass

def saveCSVByRegion(regionDataList):
    """
    保存地区各城市疫情汇总为csv文件
    :param regionDataList:  地区疫情统计汇总
    :return:
    """
    names = list(regionDataList[1].keys())
    num1 = list(regionDataList[1].values())
    num2 = list(regionDataList[2].values())
    num3 = list(regionDataList[3].values())
    num4 = list(regionDataList[4].values())
    num5 = list(regionDataList[5].values())

    n = const.SAVE_CSV_PATH + time.strftime("%Y-%m-%d") + "-" + regionDataList[0] + "-all.csv"
    fw = open(n, 'w', encoding='utf-8')
    fw.write('province,confirm,dead,heal,new_confirm\n')
    i = 0
    while i < len(names):
        fw.write(names[i] + ',' + str(num1[i]) + ',' + str(num3[i]) + ',' + str(num4[i]) + ',' + str(num5[i]) + '\n')
        i = i + 1
    else:
        print("Over write file!")
    fw.close()


def saveCSVByRegionContrast(regionDataList):
    """
        保存地区各城市疫情对比csv文件
        :param regionDataList:  地区疫情统计汇总
        :return:
        """
    names = list(regionDataList[1].keys())
    num1 = list(regionDataList[1].values())
    num2 = list(regionDataList[2].values())
    num3 = list(regionDataList[3].values())
    num4 = list(regionDataList[4].values())
    num5 = list(regionDataList[5].values())

    n = const.SAVE_CSV_PATH + time.strftime("%Y-%m-%d") + "-" + regionDataList[0] + "-cont.csv"
    fw = open(n, 'w', encoding='utf-8')
    fw.write('province,tpye,data\n')
    i = 0
    while i < len(names):
        fw.write(names[i] + ',confirm,' + str(num1[i]) + '\n')
        fw.write(names[i] + ',dead,' + str(num3[i]) + '\n')
        fw.write(names[i] + ',heal,' + str(num4[i]) + '\n')
        fw.write(names[i] + ',new_confirm,' + str(num5[i]) + '\n')
        i = i + 1
    else:
        print("Over write file!")
    fw.close()
    pass


def saveStatisticalHighFrequencyWord(saveTxtDataURL):
    """
    分析前半个月的疫情热点词汇
    :param saveTxtDataURL:  爬取词汇数据保存地址
    :return: 词汇频率汇总
    """
    saveFxTxtDataURL = const.SAVE_TXT_PATH + time.strftime("%Y-%m-%d") + "-C_class_fenxi.txt"
    all_words = ""
    if not os.path.exists(saveTxtDataURL):
        getHotWords(saveTxtDataURL)

    f = open(saveFxTxtDataURL, 'w', encoding='utf-8')
    for line in open(saveTxtDataURL, encoding='utf-8'):
        line.strip('\n')
        seg_list = jieba.cut(line, cut_all=False)
        cut_words = (" ".join(seg_list))
        f.write(cut_words)
        all_words += cut_words
    else:
        print("save fenxi txt error")
    f.close()

    # 输出结果
    all_words = all_words.split()
    # 词频统计
    c = Counter()
    for x in all_words:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1

    # 输出词频最高的前10个词
    # print('\n词频统计结果：')
    # for (k, v) in c.most_common(10):
    #     print("%s:%d" % (k, v))

    # 存储数据
    name = const.SAVE_CSV_PATH + time.strftime("%Y-%m-%d") + "-fc.csv"
    fw = open(name, 'w', encoding='utf-8')
    i = 1
    for (k, v) in c.most_common(len(c)):
        fw.write(str(i) + ',' + str(k) + ',' + str(v) + '\n')
        i = i + 1
    else:
        print("Over write file!")

    fw.close()
    return c
    pass
