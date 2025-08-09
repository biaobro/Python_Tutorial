# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 03_merge_dictionaries.py
@Project            : T003_Data_Process_Analysis
@CreateTime         : 2025/8/8 23:09
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 23:09 
@Version            : 1.0
@Description        : None
"""


def merge_dictionaries(dict1, dict2):
    """合并两个字典，如果键冲突，dict2 的值覆盖 dict1 的."""
    merged_dict = dict1.copy()  # 创建 dict1 的副本，避免修改原字典
    merged_dict.update(dict2)  # 将 dict2 的键值对添加到 merged_dict
    return merged_dict


# 示例
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = merge_dictionaries(dict1, dict2)
print(f"合并后的字典: {merged}")  # {'a': 1, 'b': 3, 'c': 4}
