# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 09_replace_text_in_string.py
@Project            : T006_Utils
@CreateTime         : 2025/8/10 11:50
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 11:50 
@Version            : 1.0
@Description        : None
"""


def replace_text_in_string(text, old_substring, new_substring):
    """在字符串中替换子字符串."""
    return text.replace(old_substring, new_substring)


# 示例
original_text = "Hello World! World is great."
replaced_text = replace_text_in_string(original_text, "World", "Python")
print(f"替换后的文本: {replaced_text}")  # Hello Python! Python is great.
