# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : readfromdb_traditional_way.py
@Project            : T008_DataBase_Operation
@CreateTime         : 2025/8/17 20:51
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/17 20:51 
@Version            : 1.0
@Description        : None
"""

import os  # 导入 os 模块，用于文件和目录操作
import pandas as pd  # 导入 pandas 库并使用 pd 别名，用于数据处理
import pymysql  # 导入 mysql.connector 模块，用于连接 MySQL 数据库

conn = pymysql.connect(
    host='localhost',  # 数据库主机地址
    user='root',       # 数据库用户名
    password='Wazg@2020', # 数据库密码
    database='runoob'   # 数据库名称
)

chunk_size = 50000  # 每个 Excel 文件的行数限制
output_folder = "output_data"  # 输出文件夹名称
if not os.path.exists(output_folder):  # 如果文件夹不存在，则创建
    os.makedirs(output_folder)

offset = 0  # 查询偏移量初始值为0
while True:  # 使用循环查询数据库，直到数据查询完毕
    query = f"SELECT * FROM fake_data LIMIT {offset}, {chunk_size}"  # 构造 SQL 查询语句
    df = pd.read_sql(query, conn)  # 使用 pandas 读取 SQL 查询结果为 DataFrame
    if df.empty:  # 如果查询结果为空，则退出循环
        break
    output_file = os.path.join(output_folder, f"output_{offset // chunk_size + 1}.xlsx")  # 构造输出文件路径
    df.to_excel(output_file, index=False)  # 将 DataFrame 写入 Excel 文件，不写入索引列
    offset += chunk_size  # 更新查询偏移量，准备下一次查询

conn.close()  # 关闭数据库连接
