# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 07_delete_file.py
@Project            : T002_File_Directory_Process
@CreateTime         : 2025/8/8 00:14
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 00:14 
@Version            : 1.0
@Description        : None
"""
import os


def delete_file(filepath):
    """删除文件."""
    try:
        os.remove(filepath)
        return f"文件 '{filepath}' 删除成功"
    except FileNotFoundError:
        return "文件未找到"
    except Exception as e:
        return f"文件删除失败: {e}"


# 示例
delete_result = delete_file('output.txt')
print(delete_result)
