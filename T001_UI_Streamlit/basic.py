# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : basic.py
@Project            : T001_UI_Streamlit
@CreateTime         : 2025/7/26 11:01
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/7/26 11:01 
@Version            : 1.0
@Description        : None
"""
import streamlit as st
import pandas as pd
from loguru import logger

# st.text("test-xxx")

upload_file = st.file_uploader('excel file', type=['xlsx'])

# 如果没有选择文件，则不执行后续代码
if upload_file is None:
    st.stop()


# 添加缓存装饰器，当文件名称没有变化时，不执行加载
@st.cache_data
def load_data(file):
    logger.info("执行文件加载...")
    return pd.read_excel(file, None)


dfs = load_data(upload_file)

names = list(dfs.keys())
sheet_selects = st.multiselect('工作表', names, [])

# 如果没有选择sheet，则不执行后续代码
if len(sheet_selects) == 0:
    st.stop()
tabs = st.tabs(sheet_selects)
for tab, name in zip(tabs, names):
    with tab:
        df = dfs[name]
        st.dataframe(df)
# st.dataframe(df)
