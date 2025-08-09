# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 08_combine_lists.py
@Project            : T003_Data_Process_Analysis
@CreateTime         : 2025/8/9 10:17
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:17 
@Version            : 1.0
@Description        : None
"""


def combine_lists(names, ages, cities):
    """使用 zip 函数同时迭代三个列表，返回姓名、年龄和城市的组合列表."""
    combined_list = []
    for name, age, city in zip(names, ages, cities):
        combined_list.append(f"{name} is {age} years old and lives in {city}")
    return combined_list


# 示例
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 28]
cities = ['New York', 'London', 'Paris']
combined = combine_lists(names, ages, cities)
for item in combined:
    print(item)
