#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by LJ on 2019-02-28
import time
import os

if __name__ == '__main__':
    while True:
        os.system("scrapy crawl submission")
        os.system("scrapy crawl userInfo")
        # 休眠一小时
        time.sleep(60 * 60)
