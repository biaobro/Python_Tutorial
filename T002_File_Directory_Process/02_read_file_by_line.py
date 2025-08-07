# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 02_read_file_by_line.py
@Project            : T002_File_Directory_Process
@CreateTime         : 2025/8/8 00:10
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 00:10 
@Version            : 1.0
@Description        : None
"""


def read_file_line_by_line(filepath):
    """逐行读取文件内容并返回列表."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        return ["文件未找到"]


# 示例
lines = read_file_line_by_line('example.txt')
for line in lines:
    print(line.strip())  # strip()去除行尾的换行符
