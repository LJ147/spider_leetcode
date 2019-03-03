#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by LJ on 2019-02-28
import time
import os

if __name__ == '__main__':
    while True:
        os.system("scrapy crawl submission")
        os.system("scrapy crawl userInfo")
        # 简单粗暴的定时爬取，搭配 screen 使用
        time.sleep(60 * 60)
