# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 04_calculate_datetime_difference.py
@Project            : T005_Date_Time_Process
@CreateTime         : 2025/8/10 10:51
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 10:51 
@Version            : 1.0
@Description        : None
"""

import datetime


def calculate_datetime_difference(datetime1, datetime2):
    """计算两个 datetime 对象的时间差，返回 timedelta 对象."""
    return datetime2 - datetime1


# 示例
datetime1 = datetime.datetime(2022, 9, 26)
datetime2 = datetime.datetime(2023, 10, 27)
time_difference = calculate_datetime_difference(datetime1, datetime2)
print(f"时间差: {time_difference}")  # 例如: 1 day, 0:00:00
