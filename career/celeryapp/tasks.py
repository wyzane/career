import time
from .celery import app
# from celery import app


@app.task
def add(x, y):
    time.sleep(10)
    return x + y


@app.task
def sum(x, y):
    time.sleep(10)
    return x + y
