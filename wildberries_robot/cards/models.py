from django.db import models


class UserArticle(models.Model):
    article = models.PositiveBigIntegerField(unique=True)

    def __str__(self):
        return str(self.article)

    class Meta:
        verbose_name = 'User Article'
        verbose_name_plural = 'User Articles'


class RecordCard(models.Model):
    id_article = models.ForeignKey(
        UserArticle, on_delete=models.CASCADE, related_name='user_article')
    name_of_product = models.CharField(max_length=255)
    price_without_discount = models.PositiveIntegerField()
    price_with_discount = models.PositiveIntegerField()
    brand = models.CharField(max_length=255)
    supplier = models.CharField(max_length=255)
    record_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.brand}, {self.name_of_product}'

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
