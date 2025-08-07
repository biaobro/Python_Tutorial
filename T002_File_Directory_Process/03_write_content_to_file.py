# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 03_write_content_to_file.py
@Project            : T002_File_Directory_Process
@CreateTime         : 2025/8/8 00:10
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/8 00:10 
@Version            : 1.0
@Description        : None
"""


def write_content_to_file(filepath, content):
    """将内容写入文件."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return "写入成功"
    except Exception as e:
        return f"写入失败: {e}"


# 示例
write_result = write_content_to_file('output.txt', '这是要写入的内容。\n第二行内容。')
print(write_result)
