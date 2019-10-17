import time
from celery import Task
from .celery import app


class BaseTask(Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))


@app.task(base=BaseTask)
def task3_add(x, y):
    time.sleep(10)
    if x < 0 or y < 0:
        raise KeyError()
    return x + y
