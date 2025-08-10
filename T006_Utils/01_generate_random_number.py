# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 01_generate_random_number.py
@Project            : T006_Utils
@CreateTime         : 2025/8/10 11:15
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 11:15 
@Version            : 1.0
@Description        : None
"""

import random


def generate_random_integer(start, end):
    """生成指定范围内的随机整数."""
    return random.randint(start, end)


# 示例
random_number = generate_random_integer(1, 100)
print(f"随机整数 (1-100): {random_number}")


def generate_random_float(start, end):
    """生成指定范围内的随机浮点数."""
    return random.uniform(start, end)


# 示例
random_float = generate_random_float(0, 10)
print(f"随机浮点数 (0-10): {random_float}")
