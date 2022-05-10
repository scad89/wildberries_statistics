from django.db import models


class UserArticul(models.Model):
    articul = models.PositiveBigIntegerField()
    unvisible = models.BooleanField(default=False)


class RecordCard(models.Model):
    id_articul = models.ForeignKey(
        UserArticul, on_delete=models.CASCADE, related_name='user_articul')
    name_of_product = models.CharField(max_length=255)
    price_without_discount = models.PositiveIntegerField()
    price_with_discount = models.PositiveIntegerField()
    brand = models.CharField(max_length=255)
    supplier = models.CharField(max_length=255)
    record_time = models.DateTimeField(auto_now_add=True)
