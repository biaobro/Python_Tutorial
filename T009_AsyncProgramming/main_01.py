# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : main_01.py
@Project            : T009_AsyncProgramming
@CreateTime         : 2025/9/10 08:08
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/9/10 08:08 
@Version            : 1.0
@Description        : None
"""
import asyncio
import api
from loguru import logger


async def send_data(to: str):
    logger.info(f'Sending data to {to}')
    await asyncio.sleep(2)
    logger.info(f'Data has been sent to {to}!')


async def main():
    # 使用 await 表示在接收到数据之前不能继续执行
    data = await api.fetch_data()
    logger.info(f'Data: {data}')

    # await send_data('Mario')
    # await send_data('Luigi')
    await asyncio.gather(send_data('Mario'), send_data('Luigi'))


if __name__ == '__main__':
    asyncio.run(main())
