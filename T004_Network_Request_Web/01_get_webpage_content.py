# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 01_get_webpage_content.py
@Project            : T004_Network_Request_Web
@CreateTime         : 2025/8/9 10:27
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:27 
@Version            : 1.0
@Description        : None
"""
import requests


def get_webpage_content(url):
    """发送 GET 请求到 URL 并返回网页内容."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功 (状态码 200)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"请求失败: {e}"


# 示例
webpage_content = get_webpage_content('https://www.example.com')
print(webpage_content[:200])  # 打印前 200 个字符
