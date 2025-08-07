# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 09_list_directory_contents.py
@Project            : T002_File_Directory_Process
@CreateTime         : 2025/8/8 00:16
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 00:16 
@Version            : 1.0
@Description        : None
"""

import os


def list_directory_contents(dirpath):
    """列出目录中的文件和子目录."""
    try:
        contents = os.listdir(dirpath)
        return contents
    except FileNotFoundError:
        return ["目录未找到"]


# 示例
directory_contents = list_directory_contents('.')  # '.' 表示当前目录
print(f"目录内容: {directory_contents}")
