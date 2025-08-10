# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 03_choose_random_item_from_list.py
@Project            : T006_Utils
@CreateTime         : 2025/8/10 11:16
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 11:16 
@Version            : 1.0
@Description        : None
"""

import random


def choose_random_item_from_list(data_list):
    """从列表中随机选择一个元素."""
    if not data_list:
        return "列表为空"
    return random.choice(data_list)


# 示例
my_list = ['apple', 'banana', 'cherry']
random_item = choose_random_item_from_list(my_list)
print(f"随机选择的元素: {random_item}")
