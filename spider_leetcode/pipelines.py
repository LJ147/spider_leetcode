# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import time

import pymysql.cursors
from twisted.enterprise import adbapi
from spider_leetcode.settings import MYSQL_HOST, MYSQL_DBNAME, MYSQL_PASSWD, MYSQL_PORT, MYSQL_USER
from spider_leetcode import settings
import pymysql


class CheckPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        updateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if spider.name == "submission":

            self.cursor.execute("""select * from CheckDayInfo where username = %s and date = %s""", (item['username'],
                                                                                                     item['checkDate']))
            ret = self.cursor.fetchone()
            if ret:
                self.cursor.execute(
                    """update CheckDayInfo set  checked = %s, updateTime = %s where username = %s and date = %s""",
                    (
                        item['checked'],
                        updateTime,
                        item['username'],
                        item['checkDate']
                    ))

            else:
                self.cursor.execute(
                    "insert into  CheckDayInfo(infoId,username, date,checked,updateTime) values(%s,%s, %s, %s,%s)",
                    (
                        None, item['username'], item['checkDate'], item['checked'],
                        updateTime))


        elif spider.name == "userInfo":
            self.cursor.execute("""select * from CheckDayInfo where username = %s and date = %s""", (item['username'],
                                                                                                     item['checkDate']))
            ret = self.cursor.fetchone()
            if ret:
                self.cursor.execute(
                    """update CheckDayInfo set  updateTime = %s, address = %s, avatar = %s, solvedQuestion = %s, acceptedSubmission = %s, acceptanceRate = %s, website = %s where username = %s and date = %s""",
                    (updateTime,
                     item['address'],
                     item['avatar'],
                     item['solvedQuestion'],
                     item['acceptedSubmission'],
                     item['acceptanceRate'],
                     item['website'],
                     item['username'],
                     item['checkDate']
                     ))
        self.connect.commit()

