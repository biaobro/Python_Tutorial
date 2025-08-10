# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 08_timestamp_to_datetime.py
@Project            : T005_Date_Time_Process
@CreateTime         : 2025/8/10 10:55
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 10:55 
@Version            : 1.0
@Description        : None
"""

import datetime
import time


def timestamp_to_datetime(timestamp):
    """将时间戳转换为 datetime 对象."""
    return datetime.datetime.fromtimestamp(timestamp)


# 示例
timestamp_value = time.time()
datetime_from_timestamp = timestamp_to_datetime(timestamp_value)
print(f"时间戳转换为 datetime 对象: {datetime_from_timestamp}")
