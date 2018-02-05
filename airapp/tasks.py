# airapp/tasks.py

import logging

from AirToday.celery import app
from celery import task

@app.task
def sayhello():
    print('Celery tasks : hello world')

from django.core.mail import send_mail
from AirToday import credentials as cred

@app.task
def sendmail():
    print('sending email')
    send_mail('subject',
                'body of the message',
                 cred.ADMIN_EMAIL,
                ['xxx@gmail.com'],
                )


#
# @app.task
# def sendsms():
#     pass
