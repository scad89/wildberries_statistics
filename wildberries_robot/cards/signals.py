from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import UserArticle
from .tasks import parse_data, cancel_periodic_task


@receiver(post_save, sender=UserArticle, dispatch_uid="send_article")
def send_article_post_save(sender, instance, created, **kwargs):
    if kwargs:
        find_article = UserArticle.objects.filter(pk=instance.pk).first()
        article = find_article.article
        parse_data.apply_async(args=[article])


@receiver(pre_delete, sender=UserArticle, dispatch_uid="cancel_periodic_task")
def send_article_pre_delete(sender, instance, **kwargs):
    if kwargs:
        find_article = UserArticle.objects.filter(pk=instance.pk).first()
        article = find_article.article
        cancel_periodic_task.apply_async(args=[article])
