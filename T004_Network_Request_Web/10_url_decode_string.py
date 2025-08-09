# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 10_url_decode_string.py
@Project            : T004_Network_Request_Web
@CreateTime         : 2025/8/9 10:55
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:55 
@Version            : 1.0
@Description        : None
"""

import urllib.parse

def url_decode_string(encoded_string):
    """对 URL 编码的字符串进行解码."""
    return urllib.parse.unquote(encoded_string)

# 示例
decoded_string = url_decode_string("search%20query%20with%20spaces")
print(f"URL 解码后的字符串: {decoded_string}") # search query with spaces
