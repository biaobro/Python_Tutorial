# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 06_generate_squares.py
@Project            : T003_Data_Process_Analysis
@CreateTime         : 2025/8/9 10:16
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:16 
@Version            : 1.0
@Description        : None
"""


def generate_squares(n):
    """使用列表推导式生成 0 到 n-1 的平方列表."""
    return [x ** 2 for x in range(n)]


# 示例
squares = generate_squares(5)
print(f"平方列表: {squares}")  # [0, 1, 4, 9, 16]
