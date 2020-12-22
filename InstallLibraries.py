#!/user/xiaoandx/ python
# -*- coding: UTF-8 -*-
"""
 Copyright (c) 2020 WEI.ZHOU. All rights reserved.
 The following code snippets are only used for circulation and cannot be used for business.
 If the code is used, no consent is required, but the author has nothing to do with any problems and
 -consequences.

 In case of code problems, feedback can be made through the following email address.
                         <xiaoandx@gmail.com>

 @Description: 运行安装 Python四川疫情爬虫可视化统计项目 需要的库
 @File: InstallLibraries.py
 @Author: WEI.ZHOU
 @Date: 2020-12-19 14:29:44
 @Version: V1.0
 @Others:  Running test instructions
"""
import os


def installLib():
    try:
        os.system("pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/")
    except:
        print("Failed Somehow")
    pass


if __name__ == '__main__':
    installLib()
