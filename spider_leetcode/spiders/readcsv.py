#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by LJ on 2019-02-28
import datetime
import json
import os


def getSubmissionUrlsFromUserAddress(path):
    """
    :param path:
    :return: eg: https://leetcode.com/api/user_submission_calendar/uwi/
    """
    module_path = os.path.dirname(__file__)
    s = set()
    with open(module_path + path, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.split(',')[1]
            splitResult = line[8:].split("/")
            domain = splitResult[0]
            username = splitResult[1]
            if username in s:
                print(username)
            s.add(username)
    print(len(s))

path = "/leetcode-address.csv"

# getSubmissionUrlsFromUserAddress(path)
