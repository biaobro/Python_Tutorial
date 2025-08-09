# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 04_reverse_dictionary.py
@Project            : T003_Data_Process_Analysis
@CreateTime         : 2025/8/8 23:10
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 23:10 
@Version            : 1.0
@Description        : None
"""


def reverse_dictionary(data_dict):
    """反转字典的键值对."""
    return {v: k for k, v in data_dict.items()}


# 示例
my_dict = {'name': 'Alice', 'age': 30}
reversed_dict = reverse_dictionary(my_dict)
print(f"反转后的字典: {reversed_dict}")  # {'Alice': 'name', 30: 'age'}
