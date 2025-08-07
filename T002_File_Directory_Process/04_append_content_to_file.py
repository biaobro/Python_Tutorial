# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 04_append_content_to_file.py
@Project            : T002_File_Directory_Process
@CreateTime         : 2025/8/8 00:11
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 00:11 
@Version            : 1.0
@Description        : None
"""


def append_content_to_file(filepath, content):
    """将内容追加到文件末尾."""
    try:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(content)
        return "追加成功"
    except Exception as e:
        return f"追加失败: {e}"


# 示例
append_result = append_content_to_file('output.txt', '\n这是追加的内容。')
print(append_result)
