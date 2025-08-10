# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 04_shuffle_list.py
@Project            : T006_Utils
@CreateTime         : 2025/8/10 11:17
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 11:17 
@Version            : 1.0
@Description        : None
"""

import random


def shuffle_list(data_list):
    """打乱列表顺序 (原地修改)."""
    random.shuffle(data_list)
    return data_list


# 示例
my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list.copy())  # 避免修改原列表
print(f"打乱后的列表: {shuffled_list}")
