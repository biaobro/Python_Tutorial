# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 09_list_with_index.py
@Project            : T003_Data_Process_Analysis
@CreateTime         : 2025/8/9 10:18
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:18 
@Version            : 1.0
@Description        : None
"""


def list_with_index(data_list):
    """使用 enumerate 函数迭代列表，返回元素和索引的组合列表."""
    indexed_list = []
    for index, item in enumerate(data_list):
        indexed_list.append(f"Index {index}: {item}")
    return indexed_list


# 示例
my_list = ['apple', 'banana', 'cherry']
indexed = list_with_index(my_list)
for item in indexed:
    print(item)
