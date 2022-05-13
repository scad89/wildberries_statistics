import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wildberries_robot.settings')

app = Celery('wildberries_robot')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
