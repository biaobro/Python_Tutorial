# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 06_get_time_components.py
@Project            : T005_Date_Time_Process
@CreateTime         : 2025/8/10 10:53
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 10:53 
@Version            : 1.0
@Description        : None
"""

import datetime


def get_time_components(datetime_obj):
    """获取 datetime 对象的小时、分钟、秒."""
    return {
        'hour': datetime_obj.hour,
        'minute': datetime_obj.minute,
        'second': datetime_obj.second
    }


# 示例
now = datetime.datetime.now()
time_components = get_time_components(now)
print(f"时间组件: {time_components}")  # 例如: {'hour': 10, 'minute': 45, 'second': 30}
