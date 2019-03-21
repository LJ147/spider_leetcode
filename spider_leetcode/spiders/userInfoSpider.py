#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by LJ on 2019-02-28
<<<<<<< HEAD
import json
import os
import time

import requests
import scrapy
from spider_leetcode.items import CheckDayInfo
=======
import os
import time

import scrapy
from spider_leetcode.items import UserInfo, CheckDayInfo
>>>>>>> 1bf39f3cb5cf8354eb15b74c689b0724598ff67c


class UerInfoSpider(scrapy.Spider):
    name = "userInfo"
<<<<<<< HEAD

    def start_requests(self):
        urls = json.loads(
            requests.get("https://group.hellogod.cn/api/member/getMemberAddressList", params={'status': 0}).text)
        for url in urls:
            username = url[8:].split("/")[1]
            url = url.strip()
            time.sleep(2)
=======
    path = "/leetcode-address.csv"

    def getUserAddressFrom(self, path):
        module_path = os.path.dirname(__file__)
        urls = []
        with open(module_path + path, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                url = line.split(',')[1]
                urls.append(url)
        return urls

    def start_requests(self):
        urls = self.getUserAddressFrom(self.path)
        for url in urls:
            username = url[8:].split("/")[1]
            url = url.strip()
>>>>>>> 1bf39f3cb5cf8354eb15b74c689b0724598ff67c
            yield scrapy.Request(url=url, callback=self.parse, meta={'username': username, 'url': url})

    def parse(self, response):
        userInfo = CheckDayInfo()
        userInfo['address'] = response.meta['url']
        userInfo['checkDate'] = time.strftime("%Y-%m-%d", time.localtime())
        userInfo['username'] = response.meta['username']
        if "leetcode-cn" in response.meta['url']:
            userInfo['avatar'] = \
                response.xpath('//*[@id="base_content"]/div/div/div[1]/div[1]/div[2]/img/@src').extract()[0]
        else:
            userInfo['avatar'] = \
                response.xpath('//*[@id="base_content"]/div/div/div[1]/div[1]/div[2]/img/@src').extract()[0]

        userInfo['solvedQuestion'] = \
            response.xpath('//*[@id="base_content"]/div/div/div[1]/div[3]/ul/li[1]/span/text()').extract()[
                0].strip().split(
                " ")[0]
        userInfo['acceptedSubmission'] = \
            response.xpath('//*[@id="base_content"]/div/div/div[1]/div[3]/ul/li[2]/span/text()').extract()[
                0].strip().split(
                " ")[0]
        userInfo['acceptanceRate'] = \
            response.xpath('//*[@id="base_content"]/div/div/div[1]/div[3]/ul/li[3]/span/text()').extract()[
                0].strip().split(
                " ")[0]

        userInfo['website'] = ""
        yield userInfo
