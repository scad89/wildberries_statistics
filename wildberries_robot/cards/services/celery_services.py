import json
from django.utils import timezone
from ..models import RecordCard
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def complete_task(task):
    task.enabled = False
    return task.save()


def check_periodic_task(article):
    return PeriodicTask.objects.get(
        name=f'Create task periodic task for {article}')


def record_to_db(get_id, name_of_product,
                 price_without_discount,
                 price_with_discount,
                 brand,
                 supplier
                 ):
    return RecordCard.objects.create(
        id_article=get_id,
        name_of_product=name_of_product,
        price_without_discount=price_without_discount,
        price_with_discount=price_with_discount,
        brand=brand,
        supplier=supplier,
    )


def create_periodic_task(article):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.HOURS,
    )
    return PeriodicTask.objects.create(
        name=f'Create task periodic task for {article}',
        task='send_notification',
        interval=schedule,
        args=json.dumps([article]),
        start_time=timezone.now(),
    )
