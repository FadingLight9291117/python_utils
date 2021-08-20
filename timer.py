import functools
import time
import logging

"""
一个计时器工具
可以作为装饰器，也可以作为上下文管理器使用
"""

logger = logging.getLogger(__name__)


class Timer:
    def __init__(self):
        self._total_time = []

    def __enter__(self):
        self._begin_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end_time = time.time()
        self._total_time.append(self._end_time - self._begin_time)

    def run_num(self):
        return len(self._total_time)

    def this_time(self):
        return self._end_time - self._begin_time

    def average_time(self):
        return sum(self._total_time) / len(self._total_time)

    def total_time(self):
        return sum(self._total_time)

    def all_time(self):
        return self._total_time

    def clear(self):
        self._total_time = []

    @classmethod
    def timer(cls, func):
        @functools.wraps(func)
        def wrapper(*args, **kargs):
            begin_time = time.time()
            res = func(*args, **kargs)
            end_time = time.time()
            during_time = end_time - begin_time

            logger.debug(f'run time: {during_time:.2f}s.')

            return res, during_time

        return wrapper
