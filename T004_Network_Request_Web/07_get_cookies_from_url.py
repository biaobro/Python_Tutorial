# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 07_get_cookies_from_url.py
@Project            : T004_Network_Request_Web
@CreateTime         : 2025/8/9 10:52
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:52 
@Version            : 1.0
@Description        : None
"""

import requests


def get_cookies_from_url(url):
    """获取 URL 返回的 cookies."""
    try:
        response = requests.get(url)
        return response.cookies.get_dict()  # 将 Cookies 对象转换为字典
    except requests.exceptions.RequestException as e:
        return f"请求失败: {e}"


# 示例
cookies = get_cookies_from_url('https://www.example.com')
print(f"Cookies: {cookies}")
