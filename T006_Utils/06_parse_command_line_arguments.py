# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 06_parse_command_line_arguments.py
@Project            : T006_Utils
@CreateTime         : 2025/8/10 11:19
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 11:19 
@Version            : 1.0
@Description        : None
"""

import argparse


def parse_command_line_arguments():
    """使用 argparse 解析命令行参数."""
    parser = argparse.ArgumentParser(description="一个简单的命令行工具")
    parser.add_argument("filename", help="要处理的文件名")
    parser.add_argument("-n", "--number", type=int, help="一个数字参数", default=10)
    args = parser.parse_args()
    return args

# 示例 (在命令行中运行: python 06_parse_command_line_arguments.py input.txt -n 20)
args = parse_command_line_arguments()
print(f"文件名: {args.filename}, 数字参数: {args.number}")
