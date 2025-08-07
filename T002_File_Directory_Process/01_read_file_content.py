# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 01_read_file_content.py
@Project            : T002_File_Directory_Process
@CreateTime         : 2025/8/4 07:17
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/4 07:17 
@Version            : 1.0
@Description        : None
"""


def read_file_content(filepath):
    """读取文件内容并返回字符串."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "文件未找到"


# 示例
file_content = read_file_content('example.txt')
print(file_content)


