# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 09_url_encode_string.py
@Project            : T004_Network_Request_Web
@CreateTime         : 2025/8/9 10:54
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:54 
@Version            : 1.0
@Description        : None
"""

import urllib.parse


def url_encode_string(string_to_encode):
    """对字符串进行 URL 编码."""
    return urllib.parse.quote(string_to_encode)


# 示例
encoded_string = url_encode_string("search query with spaces")
print(f"URL 编码后的字符串: {encoded_string}")  # search%20query%20with%20spaces
