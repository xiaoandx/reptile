#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description: 常量类，定义爬虫项目会使用的常量
 @File: constant.py
 @Author: WEI.ZHOU
 @Date: 2020-12-18 10:41:21
 @Version: V1.0
 @Others:  Running test instructions
"""

class _const:
    """
    常量保存类，如果修改常量将会报异常
    """

    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value


const = _const()

"""
cvs数据表格保存路径
"""
const.SAVE_CSV_PATH = r'./file/csv/'

"""
txt数据表格保存路径
"""
const.SAVE_TXT_PATH = r'./file/txt/'

"""
html地图数据表格保存路径
"""
const.SAVE_MAP_PATH = r'./file/map/'

"""
html地图数据表格保存路径
"""
const.WINDOW_ICO_PATH = r'./file/img/ico/favicon.ico'

"""
数据爬虫URL地址
"""
const.REQUEST_URL = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"

"""
数据爬虫URL地址
"""
const.REQUEST_URL_TIME = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d"

"""
疫情热门词语爬虫网页起点
"""
const.REQUEST_WORD_POINT_URL = "http://www.chinanpo.gov.cn/1944/index.html"

"""
疫情热门词语爬虫网页结束
"""
const.REQUEST_WORD_END_URL = "http://www.chinanpo.gov.cn/1944/126006/nextindex.html"

"""
请求header
"""
const.REQUEST_HEADERS = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 ('
                                       'KHTML, like Gecko)'
                                       'Chrome/78.0.3904.108 Mobile Safari/537.36 '
                         }
"""
统计类型 1 省份
"""
const.STATISTICAL_TYPE_REGION = 1

"""
统计类型 0 全国
"""
const.STATISTICAL_TYPE_COUNTRY = 0
