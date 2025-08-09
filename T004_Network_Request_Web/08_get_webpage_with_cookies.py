# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 08_get_webpage_with_cookies.py
@Project            : T004_Network_Request_Web
@CreateTime         : 2025/8/9 10:53
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:53 
@Version            : 1.0
@Description        : None
"""

import requests


def get_webpage_with_cookies(url, cookies_dict):
    """发送 GET 请求，并附带 cookies."""
    try:
        response = requests.get(url, cookies=cookies_dict)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"请求失败: {e}"


# 示例
cookies_to_send = {'session_id': '1234567890'}  # 假设的 cookies
content_with_cookies = get_webpage_with_cookies('https://www.example.com', cookies_to_send)
print(content_with_cookies[:200])
