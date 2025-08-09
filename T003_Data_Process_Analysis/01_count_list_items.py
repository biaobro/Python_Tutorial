# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 01_count_list_items.py
@Project            : T003_Data_Process_Analysis
@CreateTime         : 2025/8/8 23:05
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 23:05 
@Version            : 1.0
@Description        : None
"""
from collections import Counter


def count_list_items(data_list):
    """统计列表中每个元素出现的次数，返回字典."""
    return Counter(data_list)


# 示例
my_list = ['a', 'b', 'a', 'c', 'b', 'b']
counts = count_list_items(my_list)
print(f"元素计数: {counts}")  # Counter({'b': 3, 'a': 2, 'c': 1})
