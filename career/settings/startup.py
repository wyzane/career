"""项目启动时初始化
"""

from threading import Thread
from core.utils import CronUtil
from resume.hobby.crontab import task01
from server.rpc_server import SimpleServer
from server.functions import rpc_func1
from settings.local_wz import (SERVER_IP,
                               RPC_SERVER_PORT)


def run():
    print("--startup--")
    # 启动定时任务
    # CronUtil.cron_task(task01)

    thread_rpc = Thread(target=run_rpc)
    thread_rpc.start()


def run_rpc():
    """启动rpc服务
    """
    serv = SimpleServer((SERVER_IP, RPC_SERVER_PORT))
    # 注册新功能
    serv.add_function(rpc_func1)
    serv.serve_forever()
