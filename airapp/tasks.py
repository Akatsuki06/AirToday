# airapp/tasks.py

import logging

from AirToday.celery import app
from celery import task

@app.task
def sayhello():
    print('Celery tasks : hello world')
