# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 04_get_http_status_code.py
@Project            : T004_Network_Request_Web
@CreateTime         : 2025/8/9 10:44
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:44 
@Version            : 1.0
@Description        : None
"""

import requests

def get_http_status_code(url):
    """获取 URL 的 HTTP 状态码."""
    try:
        response = requests.head(url) # 使用 HEAD 请求，只获取头部信息，更高效
        return response.status_code
    except requests.exceptions.RequestException:
        return "请求失败"

# 示例
status_code = get_http_status_code('https://www.example.com')
print(f"HTTP 状态码: {status_code}") # 通常为 200
