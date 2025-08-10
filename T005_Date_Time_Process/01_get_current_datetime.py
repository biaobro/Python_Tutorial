# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 01_get_current_datetime.py
@Project            : T005_Date_Time_Process
@CreateTime         : 2025/8/10 10:49
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 10:49 
@Version            : 1.0
@Description        : None
"""

import datetime


def get_current_datetime():
    """获取当前日期和时间，返回 datetime 对象."""
    return datetime.datetime.now()


# 示例
current_datetime = get_current_datetime()
print(f"当前日期时间: {current_datetime}")
