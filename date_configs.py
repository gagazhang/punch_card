#!/usr/bin python3
# -*- coding: utf-8 -*-

'''
日期的配置文件，
'''

# 不卡的日期，一般情况下，如果是工作日：周一到周五，需要检查今天是否是不打卡的日期
no_punch_card_dates = [
    '2018-04-25'
]


# 打卡的日期列表，一般是如果是周末，但是需要打卡
need_punch_card_dates = [
    '2018-04-28'
]

if __name__ == "__main__":
    print("date_configs")