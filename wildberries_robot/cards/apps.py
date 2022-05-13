from django.apps import AppConfig
from django.db.models.signals import post_save, pre_delete


class CardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cards'

    def ready(self):
        from cards import signals
