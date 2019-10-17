import time
from .celery import app
# from celery import app


@app.task
def task1_add(x, y):
    time.sleep(10)
    return x + y


@app.task
def task1_sum(x, y):
    time.sleep(10)
    return x + y
