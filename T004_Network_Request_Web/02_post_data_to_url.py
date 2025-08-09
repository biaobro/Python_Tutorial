# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 02_post_data_to_url.py
@Project            : T004_Network_Request_Web
@CreateTime         : 2025/8/9 10:34
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:34 
@Version            : 1.0
@Description        : None
"""
import requests
import json


def post_data_to_url(url, data):
    """发送 POST 请求到 URL 并传递 JSON 数据."""
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        return response.json()  # 尝试解析 JSON 响应
    except requests.exceptions.RequestException as e:
        return f"请求失败: {e}"
    except json.JSONDecodeError:
        return "响应不是有效的 JSON 格式"


# 示例
post_url = 'https://httpbin.org/post'  # 一个用于测试 HTTP 请求的网站
post_data = {'name': 'John', 'age': 30}
post_response = post_data_to_url(post_url, post_data)
print(f"POST 响应: {post_response}")
