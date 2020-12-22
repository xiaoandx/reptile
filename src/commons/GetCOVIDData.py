#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description: 爬虫获取疫情数据方法集合
 @File: GetCOVIDData.py
 @Author: WEI.ZHOU
 @Date: 2020-12-19 13:04:06
 @Version: V1.0
 @Others:  Running test instructions
"""
import json
import time
import requests
from datetime import datetime
from .Constant import const

def getCountryData(REQUEST_URL):
    """
    获取全部疫情数据
    :param REQUEST_URL: 请求地址
    :return:
    """
    url = const.REQUEST_URL_TIME % int(time.time() * 1000)
    return json.loads(requests.get(url=url).json()['data'])
    pass

def findRegionDataList(data, region):
    """
    查询指定地区疫情汇总数据
    :param region:  地区名字
    :param data:    具体地区疫情数据
    :return:
    """
    data = data['areaTree'][0]['children']
    for i in data:
        if region == i['name']:
            regionData = i
            break

    # 显示湖北省数据
    res = regionData['children']
    # for item in res:
    #     print(item)
    # else:
    #     print("\n")

    # 解析确诊数据
    total_data = {}
    for item in regionData['children']:
        if item['name'] not in total_data:
            total_data.update({item['name'] + "市": item['total']['confirm']})

    # 解析疑似数据
    total_suspect_data = {}
    for item in regionData['children']:
        if item['name'] not in total_suspect_data:
            total_suspect_data.update({item['name']: item['total']['suspect']})

    # 解析死亡数据
    total_dead_data = {}
    for item in regionData['children']:
        if item['name'] not in total_dead_data:
            total_dead_data.update({item['name']: item['total']['dead']})

    # 解析治愈数据
    total_heal_data = {}
    for item in regionData['children']:
        if item['name'] not in total_heal_data:
            total_heal_data.update({item['name']: item['total']['heal']})

    # 解析新增确诊数据
    total_new_data = {}
    for item in regionData['children']:
        if item['name'] not in total_new_data:
            total_new_data.update({item['name']: item['today']['confirm']})

    regionDataList = [region, total_data, total_suspect_data, total_dead_data, total_heal_data, total_new_data]
    return regionDataList

def getData(REQUEST_URL, REQUEST_HEADERS):
    """
    爬虫请求数据
    :param REQUEST_URL: 爬虫数据URL
    :param REQUEST_HEADERS: 模拟浏览器请求header
    :return:    全包含国疫情数据json对象
    """
    r = requests.get(REQUEST_URL, REQUEST_HEADERS)
    res = json.loads(r.text)
    data = json.loads(res['data'])
    return data
    pass

def findDataByChain(COVID_ChainData):
    """
    获取中国全国疫情统计数据json
    :param COVID_ChainData: 全国疫情数据
    :return:    国家最新的统计数据Json
    """
    dataList = [
        '截至时间：' + str(COVID_ChainData['lastUpdateTime']) + '\n'
        '全国确诊人数：' + str(COVID_ChainData['chinaTotal']['confirm']) + '\n'
        '今日新增确诊：' + str(COVID_ChainData['chinaAdd']['confirm']) + '\n'
        '全国疑似：' + str(COVID_ChainData['chinaTotal']['suspect']) + '\n'
        '今日新增疑似：' + str(COVID_ChainData['chinaAdd']['suspect']) + '\n'
        '全国治愈：' + str(COVID_ChainData['chinaTotal']['heal']) + '\n'
        '今日新增治愈：' + str(COVID_ChainData['chinaAdd']['heal']) + '\n'
        '全国死亡：' + str(COVID_ChainData['chinaTotal']['dead']) + '\n'
        '今日新增死亡：' + str(COVID_ChainData['chinaAdd']['dead']) + '\n'
    ]
    return ''.join(dataList)
    pass

def findDataByRegion(data, region):
    """
    查询地区疫情数据json
    :param data:    地区疫情json数据
    :param region:  地区名称
    :return:    对应查询地区的最新疫情数据
    """
    res_data = []
    data = data['areaTree'][0]['children']
    path = region
    for i in data:
        if path in i['name']:
            for item in i['children']:
                list_city = [
                    '地区: ' + str(item['name']) + '\n'
                    ' 确诊人数：' + str(item['total']['confirm']),
                    ' 新增确诊：' + str(item['today']['confirm']),
                    ' 治愈：' + str(item['total']['heal']),
                    ' 死亡：' + str(item['total']['dead']) + '\n'
                ]
                res_city = ''.join(list_city)
                res_data.append(res_city)
    return res_data
    pass

