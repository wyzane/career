"""项目启动时要做的工作
"""

from core.utils import CronUtil
from resume.hobby.crontab import task01


def run():
    print("--startup--")
    # 启动定时任务
    CronUtil.cron_task(task01)
