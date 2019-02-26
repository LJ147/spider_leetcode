#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by LJ on 2019-02-24
import os

import scrapy
import json

import requests
import time


class SubmissionSpider(scrapy.Spider):
    # 名称，启动方式 scrapy crawl submission
    name = "submission"
    checkDay = '2019-02-26'
    # 总人数
    totalUserCount = 0
    # 打卡人数
    checkNumber = 0
    # 序号
    count = 0
    # 用户submission地址
    submissonUrls = []
    # 用户输入路径
    userAddressCsv = "/leetcode-address.csv"

    def datetime2Timestamp(self, dt):
        time.strptime(dt, '%Y-%m-%d %H:%M:%S')
        s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
        return int(s)

    def userHasSubmissionOnDay(self, submission, day):
        """
        :param submission: 用户submission数据
        :param day: 查卡日期，eg：'2019-02-24'
        :return:
        """
        if submission != None:
            possibleUnixTime = [self.datetime2Timestamp(day + " 08:00:00"), self.datetime2Timestamp(day + " 16:00:00")]
            for i in possibleUnixTime:
                if str(i) in submission:
                    return True
        return False

    def getSubmissionUrlsFromUserAddress(self, path):
        """
        :param path:
        :return: eg: https://leetcode.com/api/user_submission_calendar/uwi/
        """
        module_path = os.path.dirname(__file__)

        with open(module_path + path, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.split(',')[1]
                splitResult = line[8:].split("/")
                domain = splitResult[0]
                username = splitResult[1]
                submissionUrl = "https://" + domain + "/api/user_submission_calendar/" + username
                self.submissonUrls.append(submissionUrl)

    def start_requests(self):
        self.getSubmissionUrlsFromUserAddress(self.userAddressCsv)
        for url in self.submissonUrls:
            username = url.split('/')[-1]
            yield scrapy.Request(url=url, callback=self.parse_submission, dont_filter=True, meta={'username': username})

    def parse_submission(self, response):
        username = response.meta['username']
        self.count += 1
        submissions = json.loads(response.text)
        if self.userHasSubmissionOnDay(submissions, self.checkDay):
            self.checkNumber += 1
            print("序号：%d，时间：%s，用户 %s %s" % (self.count, self.checkDay, username, "已打卡"))
        else:
            print("序号：%d，时间：%s，用户 %s %s" % (self.count, self.checkDay, username, "缺卡"))
        if self.count == len(self.submissonUrls):
            print("时间：%s，人数总计： %d，打卡人数：  %d " % (self.checkDay, len(self.submissonUrls), self.checkNumber))
