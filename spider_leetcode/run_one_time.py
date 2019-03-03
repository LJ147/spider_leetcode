#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by LJ on 2019-03-02
from scrapy import cmdline

if __name__ == '__main__':
    # os.system("scrapy crawl submission")
    # time.sleep(60 * 60)

    cmdline.execute("scrapy crawl submission".split())
    cmdline.execute("scrapy crawl userInfo".split())


