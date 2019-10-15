"""
    Author: Pashazera
    Time  : 2019/10/14 17:00
    File  : log.py
    describe :
"""

from loguru import logger

logger.add("file.log")
logger.debug("这是一条debug日志")
logger.info('这是一条info日志')

import django
print(django.__version__)