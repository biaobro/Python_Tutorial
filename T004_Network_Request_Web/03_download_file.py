# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 03_download_file.py
@Project            : T004_Network_Request_Web
@CreateTime         : 2025/8/9 10:43
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/9 10:43 
@Version            : 1.0
@Description        : None
"""

import requests


def download_file(url, filepath):
    """从 URL 下载文件并保存到本地."""
    try:
        response = requests.get(url, stream=True)  # stream=True 用于大文件下载
        response.raise_for_status()
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):  # 分块写入，避免内存溢出
                f.write(chunk)
        return f"文件下载成功，保存到: {filepath}"
    except requests.exceptions.RequestException as e:
        return f"文件下载失败: {e}"


# 示例
file_url = 'https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif'  # 一个 GIF 图片示例
download_result = download_file(file_url, 'sample.gif')
print(download_result)
# [Image of sample gif image]
