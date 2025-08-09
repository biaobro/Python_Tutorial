# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 05_get_webpage_with_timeout.py
@Project            : T004_Network_Request_Web
@CreateTime         : 2025/8/9 10:45
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:45 
@Version            : 1.0
@Description        : None
"""

import requests


def get_webpage_with_timeout(url, timeout_seconds):
    """发送 GET 请求，并设置超时时间."""
    try:
        response = requests.get(url, timeout=timeout_seconds)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        return "请求超时"
    except requests.exceptions.RequestException as e:
        return f"请求失败: {e}"


# 示例
content_with_timeout = get_webpage_with_timeout('https://www.example.com', 0.05)  # 超时时间为 5 秒
print(content_with_timeout[:200])
