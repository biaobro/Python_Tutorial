# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 05_check_file_exists.py
@Project            : T002_File_Directory_Process
@CreateTime         : 2025/8/8 00:12
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 00:12 
@Version            : 1.0
@Description        : None
"""
import os


def check_file_exists(filepath):
    """检查文件是否存在."""
    return os.path.exists(filepath)


# 示例
exists = check_file_exists('example.txt')
print(f"文件是否存在: {exists}")
