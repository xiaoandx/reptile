#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description:  自定义异常类集合
 @File: CommonsException.py
 @Author: WEI.ZHOU
 @Date: 2020-12-21 13:28:22
 @Version: V1.0
 @Others:  Running test instructions
"""
class inputException(Exception):
    """
    输入编号超过范围异常，
    key：用户输入的具体编号
    """
    def __init__(self, key):
        self.key = key

    def __str__(self):
        print("input No. " + str(self.key) + " error！！！ 1-6")
