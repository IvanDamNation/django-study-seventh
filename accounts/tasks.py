from celery import shared_task
from accounts.utils import news_sender


@shared_task
def send_mail_for_sub_every_week():
    news_sender()
