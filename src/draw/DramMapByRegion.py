#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description: 绘制地区各城市地图
 @File: DramMapByRegion.py
 @Author: WEI.ZHOU
 @Date: 2020-12-19 13:47:52
 @Version: V1.0
 @Others:  Running test instructions
"""
import os
import time
import webbrowser

import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts

from commons.GetCOVIDData import findRegionDataList
from commons.SaveFile import saveCSVByRegion
from commons.Constant import const


def dramMapByRegion(data, region):
    """
    绘制地区地图页面
    :param data:
    :param region:
    :return:
    """
    n = const.SAVE_CSV_PATH + time.strftime("%Y-%m-%d") + "-" + region + "-all.csv"
    if not os.path.exists(n):
        saveCSVByRegion(findRegionDataList(data, region))
    data = pd.read_csv(n)
    list_data_region = zip(list(data['province']), list(data['confirm']))
    region_data = list(list_data_region)
    map_region_disease_dis(region_data, region).render(const.SAVE_MAP_PATH + region + '疫情地图.html')
    webbrowser.open(
        "file:\\\\\\" + os.path.abspath(os.path.dirname(os.getcwd())) +
        "\\src\\file\\map\\" + region + '疫情地图.html')
    pass


def map_region_disease_dis(region_data, region) -> Map:
    c = (
        Map(init_opts=opts.InitOpts(width='2000px',height="1000px")).add(region, region_data, region).set_series_opts(
            label_opts=opts.LabelOpts(is_show=True, formatter='{b}\n{c}例')).set_global_opts(
            title_opts=opts.TitleOpts(title= region + '新型冠状病毒疫情地图（确诊数）'),
            visualmap_opts=opts.VisualMapOpts(is_show=True,
                                              split_number=6,
                                              is_piecewise=True,  # 是否为分段型
                                              pos_top='center',
                                              pieces=[{'min': 50},
                                                      {'min': 30, 'max': 49}, {'min': 20, 'max': 29},
                                                      {'min': 10, 'max': 19}, {'min': 1, 'max': 9},
                                                      {'value': 0, "label": '无确诊病例', "color":
                                                          'green'}],
                                              ), ))

    return c
