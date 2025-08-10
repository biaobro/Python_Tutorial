# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 07_generate_password.py
@Project            : T006_Utils
@CreateTime         : 2025/8/10 11:22
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 11:22 
@Version            : 1.0
@Description        : None
"""

import random
import string


def generate_password(length=12):
    """生成指定长度的随机密码，包含字母和数字."""
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password


# 示例
password = generate_password(16)
print(f"随机密码: {password}")
