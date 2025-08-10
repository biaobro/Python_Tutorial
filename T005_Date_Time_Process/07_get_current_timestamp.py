# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 07_get_current_timestamp.py
@Project            : T005_Date_Time_Process
@CreateTime         : 2025/8/10 10:54
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 10:54 
@Version            : 1.0
@Description        : None
"""

import time


def get_current_timestamp():
    """获取当前时间戳 (秒)."""
    return time.time()


# 示例
timestamp = get_current_timestamp()
print(f"当前时间戳_10位: {timestamp}")  # 例如: 1698384000.0
