# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 10_get_file_size.py
@Project            : T002_File_Directory_Process
@CreateTime         : 2025/8/8 00:20
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 00:20 
@Version            : 1.0
@Description        : None
"""
import os


def get_file_size(filepath):
    """获取文件大小，单位为字节."""
    try:
        size_in_bytes = os.path.getsize(filepath)
        return size_in_bytes
    except FileNotFoundError:
        return "文件未找到"


# 示例
file_size = get_file_size('example.txt')
print(f"文件大小: {file_size} 字节")
