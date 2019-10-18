import time
import asyncio
from threading import Thread


class AsyncTask:
    """异步任务
    """
    @staticmethod
    def task(loop, func):
        t = Thread(target=func, args=(loop,))
        t.start()


def test(loop):
    """异步测试
    """
    # cro = t()
    # loop.run_until_complete(cro)
    t()


def t():
    t1 = time.time()
    for i in range(4):
        # asyncio.sleep(2)
        print("-- 1 --")
    print("time:", time.time() - t1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    AsyncTask.task(loop, test)
