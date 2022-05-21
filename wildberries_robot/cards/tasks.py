from wildberries_robot.celery import app
from celery.utils.log import get_task_logger
from .models import UserArticle
import requests
from cards.services.selenium_and_bs4_services import (
    getting_data_with_selenium,
    getting_brand_and_product_name,
    getting_supplier
)
from cards.services.celery_services import (
    record_to_db,
    create_periodic_task,
    get_periodic_task,
    complete_task
)
from dotenv import load_dotenv

load_dotenv()

logger = get_task_logger(__name__)


@app.task(bind=True)
def parse_data(self, article):
    get_id_article = UserArticle.objects.get(article=article)
    price_with_discount, price_without_discount = getting_data_with_selenium(
        article)
    if price_without_discount:
        brand, product_name = getting_brand_and_product_name(article)
        supplier = getting_supplier(article)
        record_to_db(get_id_article, product_name,
                     price_without_discount,
                     price_with_discount,
                     brand,
                     supplier,
                     )
        new_task = get_periodic_task(article)
        if new_task:
            return logger.info(
                f'Data for {article} received successfully')
        else:
            create_periodic_task(article)
            return logger.info(
                f'Data for {article} received successfully. A periodic task has been created.'
            )
    else:
        return logger.info(f'Data for {article} not received')


@app.task(bind=True)
def cancel_periodic_task(self, article):
    task_success = get_periodic_task(article)
    if task_success:
        complete_task(task_success)
        return logger.info(f'Periodic task for {article} removed')
