# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : main_02.py
@Project            : T009_AsyncProgramming
@CreateTime         : 2025/9/16 21:42
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/9/16 21:42 
@Version            : 1.0
@Description        : None
"""
import asyncio
import api
from loguru import logger


async def kill_time(num):
    logger.info(f'Running: {num}')
    await asyncio.sleep(1)
    logger.info(f'Finished: {num}')


async def main():
    logger.info(f'Started!')
    list_of_tasks = []
    for i in range(1, 1000+1):
        list_of_tasks.append(kill_time(i))
    await asyncio.sleep(2)
    await asyncio.gather(*list_of_tasks)
    logger.info(f'Done!')


if __name__ == '__main__':
    asyncio.run(main())
