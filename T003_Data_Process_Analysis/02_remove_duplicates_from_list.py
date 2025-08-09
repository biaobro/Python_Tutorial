# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 02_remove_duplicates_from_list.py
@Project            : T003_Data_Process_Analysis
@CreateTime         : 2025/8/8 23:08
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 23:08 
@Version            : 1.0
@Description        : None
"""


def remove_duplicates_from_list(data_list):
    """去除列表中的重复元素，保持顺序."""
    return list(dict.fromkeys(data_list))  # 利用字典的键唯一性


# 示例
my_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = remove_duplicates_from_list(my_list)
print(f"去重后的列表: {unique_list}")  # [1, 2, 3, 4, 5]
