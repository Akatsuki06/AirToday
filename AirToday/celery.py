# AirToday/celery.py

import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AirToday.settings')



app = Celery('AirToday')
app.config_from_object('django.conf:settings')
app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
#
app.conf.beat_schedule = {
    'sendmail': {
        'task': 'airapp.tasks.alertusers',
        'schedule': crontab(minute=0,hour='6')
        # 'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}
