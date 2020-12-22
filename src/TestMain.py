#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description: 疫情统计主函数
 @File: TestMain.py
 @Author: WEI.ZHOU
 @Date: 2020-12-18 10:33:31
 @Version: V1.0
 @Others:  Running test instructions
"""
import json
import time
import requests

from commons.GetCOVIDData import getCountryData, getData, findDataByChain, findDataByRegion
from commons.Constant import const
from commons.SaveFile import saveTxtFileByData
from commons.CommonsException import inputException
from draw.DramMapByRegion import dramMapByRegion
from draw.DrawRegionalComparisonHistogram import drawChartColumn
from draw.DistrictChart import countryDataByRegion, findRegionDataList, saveCSVByRegion, drawChartByRegion
from draw.StatisticalHighFrequencyWord import DramMapHotWords


def main():
    # 爬虫获取全国所有疫情数据（中国、各省份）的感染、死亡、新增.....等数据
    # COVID_ChainData = getData(const.REQUEST_URL, const.REQUEST_HEADERS)
    #
    # 查询统计中国疫情数据（感染、死亡、新增.....）
    # chainData = findDataByChain(COVID_ChainData)
    # 保存统计中国疫情数据完成到txt文件中
    # saveTxtFileByData(chainData, const.STATISTICAL_TYPE_COUNTRY)
    #
    # 查询统计地区(如：四川)疫情数据（感染、死亡、新增.....）
    # regionData = findDataByRegion(COVID_ChainData, '四川')
    # 保存统计地区(如：四川)疫情数据完成到txt文件中
    # saveTxtFileByData(regionData, const.STATISTICAL_TYPE_REGION)

    # 四川省疫情绘图统计
    # countryData = getCountryData(const.REQUEST_URL)

    # 绘制地区各城市分类柱状图（确诊、死亡、治愈、新增）
    # countryDataByRegion(countryData, '四川')

    # 绘制地区各城市感染总数柱状图
    # drawChartByRegion(countryData, '四川')

    # 绘制地区各城市疫情对比柱状图
    # drawChartColumn(countryData, '四川')

    # 绘制地区疫情统计地图
    # dramMapByRegion(countryData, '四川')

    # 绘制疫情热门词汇展示
    # DramMapHotWords(const.SAVE_TXT_WORD_PATH, const.REQUEST_WORD_POINT_URL)
    pass


def viewMenu():
    """
    项目运行提示菜单
    """
    print("项目提供以下功能，输入对应编号进行运行\n\n")
    print("1. 绘制地区各城市分类柱状图（确诊、死亡、治愈、新增）")
    print("2. 绘制地区各城市感染总数柱状图")
    print("3. 绘制地区各城市疫情对比柱状图")
    print("4. 绘制地区疫情统计地图")
    print("5. 绘制疫情热门词汇展示")
    print("6. 退出项目\n\n")
    pass


def menu(countryData):
    """
    输入系统功能编号 运行对应功能
    1 -> 绘制地区各城市分类柱状图（确诊、死亡、治愈、新增）
    2 -> 绘制地区各城市感染总数柱状图
    3 -> 绘制地区各城市疫情对比柱状图
    4 -> 绘制地区疫情统计地图
    5 -> 绘制疫情热门词汇展示
    :param countryData: 全国疫情数据
    :return:
    """
    status = True
    print('=' * 20 + "Python 地区(四川)疫情爬虫与新闻高频词云可视化项目" + '=' * 20 + "\n\n")
    while status:
        viewMenu()
        number = int(input("输入项目对应功能编号选择运行功能："))
        if 1 == number:
            countryDataByRegion(countryData, '四川')
        elif 2 == number:
            drawChartByRegion(countryData, '四川')
        elif 3 == number:
            drawChartColumn(countryData, '四川')
        elif 4 == number:
            dramMapByRegion(countryData, '四川')
            print("\n\n生成成功，前往 {}文件夹下查看网页地图\n\n".format(const.SAVE_MAP_PATH))
        elif 5 == number:
            DramMapHotWords(const.SAVE_TXT_PATH)
            print("\n\n生成成功，前往 {}文件夹下查看词云地图\n\n".format(const.SAVE_MAP_PATH))
        elif 6 == number:
            status = False
        else:
            print("\ninput number error!!! 1-6\n")
            # raise inputException(number)
    pass


if __name__ == '__main__':
    countryData = getCountryData(const.REQUEST_URL)
    menu(countryData)
