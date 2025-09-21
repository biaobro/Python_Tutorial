# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : main_03.py
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

    await asyncio.sleep(2)

    # task.cancel()
    # await asyncio.sleep(0.5)

    if task.cancelled():
        logger.info(task.cancelled())
    try:
        if task.done():
            logger.info(task.result())

        # result = await task
        # logger.info(result)
    except asyncio.CancelledError:
        logger.info('Cancelled : Request was cancelled...')
    except asyncio.TimeoutError:
        logger.info('Timeout : Request took too long...!')


if __name__ == '__main__':
    asyncio.run(main())
