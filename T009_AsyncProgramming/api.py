# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : api.py
@Project            : T009_AsyncProgramming
@CreateTime         : 2025/9/10 08:00
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/9/10 08:00 
@Version            : 1.0
@Description        : None
"""

import asyncio
from loguru import logger


# async 函数可以被同时调用，并同时执行
async def fetch_data() -> str:
    logger.info('fetching data ...')

    # await 强制程序等待当前语句完成
    await asyncio.sleep(2.5)

    logger.info('data has been fetched !!!')

    return 'API Data'
