# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 06_create_directory.py
@Project            : T002_File_Directory_Process
@CreateTime         : 2025/8/8 00:13
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 00:13 
@Version            : 1.0
@Description        : None
"""

import os


def create_directory(dirpath):
    """创建目录."""
    try:
        os.makedirs(dirpath, exist_ok=True)  # exist_ok=True 表示目录已存在时不会报错
        return f"目录 '{dirpath}' 创建成功"
    except Exception as e:
        return f"目录创建失败: {e}"


# 示例
create_result = create_directory('new_directory')
print(create_result)
