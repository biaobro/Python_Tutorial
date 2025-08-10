# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 09_get_month_first_last_day.py
@Project            : T005_Date_Time_Process
@CreateTime         : 2025/8/10 10:56
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 10:56 
@Version            : 1.0
@Description        : None
"""

import datetime
import calendar


def get_month_first_last_day(year, month):
    """获取某年某月的第一天和最后一天."""
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month, calendar.monthrange(year, month)[1])
    return {
        'first_day': first_day,
        'last_day': last_day
    }


# 示例
month_days = get_month_first_last_day(2023, 6)
print(
    f"2023年10月的第一天和最后一天: {month_days}")  # {'first_day': datetime.date(2023, 10, 1), 'last_day': datetime.date(2023, 10, 31)}
