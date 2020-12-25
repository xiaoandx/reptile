#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description: Python新闻信息抓取
 @File: GetJournalism.py
 @Author: WEI.ZHOU
 @Date: 2020-12-19 14:46:36
 @Version: V1.0
 @Others:  Running test instructions
"""
import requests
import time
from bs4 import BeautifulSoup
from lxml import html

from .Constant import const

startTime = time.time()

def requestDom(url):
    """
    request 请求判断
    :param url: 请求地址
    :return:    请求数据
    """
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
    except requests.RequestException:
        return None
    pass

def spider_html_info(url,f):
    """
    解析网页中的文字数据保存在C_class.txt文件中
    :param url: 请求地址
    :param f:   保存数据的文件对象
    :return:    下一次爬取数据的页面地址
    """
    try:
        response = requests.get(url=url).text
        text_html = html.fromstring(response)

        # 获取下一页链接,先其他元素获取一页链接，保证程序的强壮性
        next_url = "http://www.chinanpo.gov.cn" + text_html.xpath('/html/body/div[2]/div/ul[1]/li[2]/a[2]/@href')[0]
        # 爬取文本
        text_list = text_html.xpath('//*[@id="fontinfo"]//text()')

        article_text = "".join(text_list).replace('\r\n', '').replace("\xa0", "").replace("\t", "")

        f.write(article_text + '\n')
    except:
        pass

    return next_url

def getPointURL():
    url = const.REQUEST_WORD_POINT_URL
    htmlObj = requestDom(url)
    soup = BeautifulSoup(htmlObj, "lxml")
    return soup.find_all("li")[0].find('a').get('href')[6:12]
    pass

def getHotWords(saveTxtDataURL):
    """
    爬取中国社会组织公共服务平台热点词汇数据
    :param saveTxtDataURL:  爬取词汇数据保存地址
    :return:
    """
    f = open(saveTxtDataURL, 'a', encoding="utf-8")
    pointURL = "http://www.chinanpo.gov.cn/1944/"+getPointURL()+"/index.html"
    for i in range(0, 16):
        print("正在爬取第{}篇 {}：".format((i+1), pointURL))
        pointURL = spider_html_info(pointURL, f)

    endTime = time.time()
    useTime = (endTime - startTime) / 60
    print("该次所获的信息一共使用%s分钟" % useTime)
    f.close()
    pass


