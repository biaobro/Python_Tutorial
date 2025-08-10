# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : demo.py
@Project            : T007_ProgressBar_tqdm
@CreateTime         : 2025/8/10 17:04
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 17:04 
@Version            : 1.0
@Description        : None
"""

from time import sleep
from tqdm import tqdm
import pandas as pd
import seaborn as sns

'''code1: use range as object'''
# it/s = iteration/second
# desc 展示在进度百分比左侧的文字，可用于存在多个进度条时区分不同的进度条
# for _ in tqdm(range(1,10000), desc="Number"):
#     sleep(0.001)


'''code2: use list as object'''
# students = ['A','B','C','D','E','F','G','H']
# for _ in tqdm(students,desc='List'):
#     sleep(0.5)


'''code3: use generator as object'''
# def my_generator():
#     for i in range(50):
#         yield i
#
#
# # 默认情况下，因为 tqdm 不知道生成器需要迭代多少次，所以不会显示进度条，只会显示速度
# # 但还是可以通过 total 参数人工指定迭代次数
# for _ in tqdm(my_generator(), desc='Generator', total=50):
#     sleep(0.1)


'''code4: update progress bar manually'''
# 创建tqdm对象
# pbar = tqdm(total=100, desc='Manually')
# pbar.update(10) # 增加
# sleep(2)
# pbar.update(20)
# sleep(2)
# pbar.update(70)
# pbar.close()

'''code5: update progress bar manually'''
'''使用 context manager'''
# with tqdm(total=100, desc='Manually') as pbar:
#     pbar.update(10) # 增加
#     sleep(2)
#     pbar.update(20)
#     sleep(2)
#     pbar.update(70)


df = sns.load_dataset('iris')
# print(df.head())
tqdm.pandas(desc='Progressing')
df.petal_width.progress_apply(lambda x: x * 2)
