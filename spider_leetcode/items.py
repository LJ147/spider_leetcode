# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item



class CheckDayInfo(Item):

    avatar = Field()
    username = Field()
    address = Field()
    realname = Field()
    website = Field()
    checkDate = Field()
    checkDaysInTheLastYear = Field()
    checked = Field()
    submissionOfToday = Field()
    submissionCount = Field()

    # progress
    solvedQuestion = Field()
    acceptedSubmission = Field()
    acceptanceRate = Field()
