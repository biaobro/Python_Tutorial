# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : main_04.py
@Project            : T009_AsyncProgramming
@CreateTime         : 2025/9/16 21:49
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/9/16 21:49 
@Version            : 1.0
@Description        : None
"""
import asyncio
import api
from loguru import logger


async def main():
    task = asyncio.create_task(
        api.fetch_data()
    )

    try:
        # 等待2s后就直接放弃
        await asyncio.wait_for(task, timeout=2)

    except asyncio.CancelledError:
        logger.info('Cancelled : Request was cancelled...')
    except asyncio.TimeoutError:
        logger.info('Timeout : Request took too long...!')


if __name__ == '__main__':
    asyncio.run(main())
