# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 10_add_days_to_date.py
@Project            : T005_Date_Time_Process
@CreateTime         : 2025/8/10 10:57
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 10:57 
@Version            : 1.0
@Description        : None
"""

import datetime


def add_days_to_date(date_obj, days_to_add):
    """给日期增加指定天数."""
    delta = datetime.timedelta(days=days_to_add)
    return date_obj + delta


def subtract_days_from_date(date_obj, days_to_subtract):
    """给日期减少指定天数."""
    delta = datetime.timedelta(days=days_to_subtract)
    return date_obj - delta


# 示例
today = datetime.date.today()
future_date = add_days_to_date(today, 7)  # 7 天后
past_date = subtract_days_from_date(today, 3)  # 3 天前
print(f"7 天后: {future_date}, 3 天前: {past_date}")
