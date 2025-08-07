# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 08_delete_directory.py
@Project            : T002_File_Directory_Process
@CreateTime         : 2025/8/8 00:15
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 00:15 
@Version            : 1.0
@Description        : None
"""
import os


def delete_directory(dirpath):
    """删除目录 (目录必须为空)."""
    try:
        os.rmdir(dirpath)
        return f"目录 '{dirpath}' 删除成功"
    except FileNotFoundError:
        return "目录未找到"
    except OSError:
        return "目录非空，无法删除"
    except Exception as e:
        return f"目录删除失败: {e}"


# 示例
delete_result = delete_directory('new_directory')
print(delete_result)  # 如果目录不为空，会打印 "目录非空，无法删除"
