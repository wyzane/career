import time
from .celery import app
# from celery import app


@app.task
def task2_add(x, y):
    time.sleep(10)
    return x + y


@app.task
def task2_sum(x, y):
    time.sleep(10)
    return x + y
