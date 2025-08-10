# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 05_get_date_components.py
@Project            : T005_Date_Time_Process
@CreateTime         : 2025/8/10 10:52
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 10:52 
@Version            : 1.0
@Description        : None
"""

import datetime


def get_date_components(datetime_obj):
    """获取 datetime 对象的年份、月份、日."""
    return {
        'year': datetime_obj.year,
        'month': datetime_obj.month,
        'day': datetime_obj.day
    }


# 示例
now = datetime.datetime.now()
date_components = get_date_components(now)
print(f"日期组件: {date_components}")  # 例如: {'year': 2023, 'month': 10, 'day': 27}
