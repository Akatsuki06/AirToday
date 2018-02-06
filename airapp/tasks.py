# airapp/tasks.py

from celery import task
from twilio.rest import Client
from django.core.mail import send_mail
from AirToday.celery import app
from AirToday import credentials as cred
from . import models, location
import json

@app.task
def sayhello():
    print('Celery tasks : hello world')


@app.task
def alertusers():
    print('getting all users')
    users = models.CustomUser.objects.all()
    loc = location()
    print('sending email')
    for user in users:
        data = json.load(loc.get_AQI(user.coordinates))
        # data = json.load(open('aqi.json'))
        msg_body = 'Alert: \n'+data['data']['alert']+'\n\n Source: \n'+data['data']['source']['name']
        send_mail('Air Quality Index Notification',
                    msg_body,
                    cred.ADMIN_EMAIL,
                    [user.email],
                    )
    # client = Client(cred.TWILIO_ACC, cred.TWILIO_TOKEN)
    # client.api.account.messages.create(
    #     to="",
    #     from_=cred.TWILIO_PHONE,
    #     body="Hello there!")
    # print('sms sent')
