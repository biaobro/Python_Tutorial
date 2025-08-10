# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 02_format_datetime.py
@Project            : T005_Date_Time_Process
@CreateTime         : 2025/8/10 10:50
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 10:50 
@Version            : 1.0
@Description        : None
"""

import datetime


def format_datetime(datetime_obj, format_string="%Y-%m-%d %H:%M:%S"):
    """将 datetime 对象格式化为字符串."""
    return datetime_obj.strftime(format_string)


# 示例
now = datetime.datetime.now()
formatted_datetime = format_datetime(now)
print(f"格式化后的日期时间: {formatted_datetime}")  # 例如: 2023-10-27 10:30:45
