# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 05_calculate_execution_time.py
@Project            : T006_Utils
@CreateTime         : 2025/8/10 11:18
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 11:18 
@Version            : 1.0
@Description        : None
"""

import time


def calculate_execution_time(func, *args, **kwargs):
    """计算函数运行时间 (秒)."""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, result  # 返回运行时间和函数结果


# 示例函数 (计算平方和)
def sum_of_squares(n):
    return sum([i ** 2 for i in range(n)])


execution_time, result = calculate_execution_time(sum_of_squares, 100000)
print(f"函数运行时间: {execution_time:.4f} 秒, 结果: {result}")
