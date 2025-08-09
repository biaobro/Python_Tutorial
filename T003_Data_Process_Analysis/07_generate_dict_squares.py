# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 07_generate_dict_squares.py
@Project            : T003_Data_Process_Analysis
@CreateTime         : 2025/8/9 10:16
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:16 
@Version            : 1.0
@Description        : None
"""


def generate_dict_squares(n):
    """使用字典推导式生成 0 到 n-1 的平方字典，键为数字，值为平方."""
    return {x: x ** 2 for x in range(n)}


# 示例
dict_squares = generate_dict_squares(5)
print(f"平方字典: {dict_squares}")  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
