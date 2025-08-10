# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 10_safe_integer_division.py
@Project            : T006_Utils
@CreateTime         : 2025/8/10 11:50
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 11:50 
@Version            : 1.0
@Description        : None
"""


def safe_integer_division(numerator, denominator):
    """安全地进行整数除法，处理除零异常."""
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "除数不能为零"
    except TypeError:
        return "输入类型错误，请输入数字"


# 示例
division_result1 = safe_integer_division(10, 2)
division_result2 = safe_integer_division(10, 0)
division_result3 = safe_integer_division(10, 'a')
print(f"10 / 2 = {division_result1}")  # 5.0
print(f"10 / 0 = {division_result2}")  # 除数不能为零
print(f"10 / 'a' = {division_result3}")  # 输入类型错误，请输入数字
