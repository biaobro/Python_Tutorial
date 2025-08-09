# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 10_group_by_key.py
@Project            : T003_Data_Process_Analysis
@CreateTime         : 2025/8/9 10:19
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:19 
@Version            : 1.0
@Description        : None
"""
import itertools


def group_by_key(data_list, key_func):
    """使用 itertools.groupby 函数根据 key_func 分组数据."""
    sorted_data = sorted(data_list, key=key_func)  # groupby 前需要先排序
    grouped_data = {}
    for key, group in itertools.groupby(sorted_data, key=key_func):
        grouped_data[key] = list(group)  # group 是迭代器，需要转换为 list
    return grouped_data


# 示例
data = [{'city': 'London', 'name': 'Alice'},
        {'city': 'Paris', 'name': 'Bob'},
        {'city': 'London', 'name': 'Charlie'},
        {'city': 'Paris', 'name': 'David'}]

grouped_by_city = group_by_key(data, key_func=lambda x: x['city'])
print(f"按城市分组: {grouped_by_city}")
