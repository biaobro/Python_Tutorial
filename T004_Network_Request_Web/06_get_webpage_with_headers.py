# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 06_get_webpage_with_headers.py
@Project            : T004_Network_Request_Web
@CreateTime         : 2025/8/9 10:46
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:46 
@Version            : 1.0
@Description        : None
"""

import requests

def get_webpage_with_headers(url, headers):
    """发送 GET 请求，并添加自定义请求头."""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"请求失败: {e}"

# 示例
custom_headers = {'User-Agent': 'My-Custom-User-Agent/1.0'}
content_with_headers = get_webpage_with_headers('https://www.example.com', custom_headers)
print(content_with_headers[:200])
