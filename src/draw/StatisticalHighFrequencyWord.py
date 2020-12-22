#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description: 绘制疫情高频词生成对应的疫情词云图
 @File: StatisticalHighFrequencyWord.py
 @Author: WEI.ZHOU
 @Date: 2020-12-19 15:49:11
 @Version: V1.0
 @Others:  Running test instructions
"""
import time

from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

from commons.Constant import const
from commons.SaveFile import saveStatisticalHighFrequencyWord


def DramMapHotWords(saveTxtDataURL):
    """
    解析词频绘制集合，并生成对应的疫情词云图
    :param saveTxtDataURL:
    :return:
    """
    saveTxtDataURL = const.SAVE_TXT_PATH + time.strftime("%Y-%m-%d") + "-C_class.txt"
    c = saveStatisticalHighFrequencyWord(saveTxtDataURL)
    words = []
    for (k, v) in c.most_common(1000):
        words.append((k,v))
    # 生成图
    wordcloud_base(words).render(const.SAVE_MAP_PATH + '十五天内疫情词云图.html')


# 渲染图
def wordcloud_base(words) -> WordCloud:
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 100], shape=SymbolType.ROUND_RECT)
        .set_global_opts(title_opts=opts.TitleOpts(title='十五天内新型冠状病毒疫情词云图'))
    )
    return c


