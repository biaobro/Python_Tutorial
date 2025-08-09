# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 05_sort_dictionary_by_value.py
@Project            : T003_Data_Process_Analysis
@CreateTime         : 2025/8/9 10:15
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:15 
@Version            : 1.0
@Description        : None
"""


def sort_dictionary_by_value(data_dict, reverse=False):
    """按字典的值排序，返回排序后的键值对列表."""
    return sorted(data_dict.items(), key=lambda item: item[1], reverse=reverse)


# 示例
my_dict = {'a': 10, 'c': 1, 'b': 5}
sorted_dict = sort_dictionary_by_value(my_dict)
print(f"按值升序排序: {sorted_dict}")  # [('c', 1), ('b', 5), ('a', 10)]
sorted_dict_desc = sort_dictionary_by_value(my_dict, reverse=True)
print(f"按值降序排序: {sorted_dict_desc}")  # [('a', 10), ('b', 5), ('c', 1)]
