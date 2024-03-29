import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send_mail_every_monday_8am': {
        'task': 'accounts.tasks.send_mail_for_sub_every_week',
        'schedule': crontab(minute="*/1"),
    },
}

app.autodiscover_tasks()
