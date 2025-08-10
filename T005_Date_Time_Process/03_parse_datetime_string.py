# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 03_parse_datetime_string.py
@Project            : T005_Date_Time_Process
@CreateTime         : 2025/8/10 10:51
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 10:51 
@Version            : 1.0
@Description        : None
"""

import datetime


def parse_datetime_string(datetime_string, format_string="%Y-%m-%d %H:%M:%S"):
    """将字符串解析为 datetime 对象."""
    try:
        return datetime.datetime.strptime(datetime_string, format_string)
    except ValueError:
        return "日期时间字符串格式错误"


# 示例
date_string = "2023-10-27 10:30:00"
parsed_datetime = parse_datetime_string(date_string)
print(f"解析后的 datetime 对象: {parsed_datetime}")
