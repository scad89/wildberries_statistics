# Generated by Django 3.2.13 on 2022-05-18 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordcard',
            name='id_user_for_card',
        ),
        migrations.RemoveField(
            model_name='userarticle',
            name='id_user_for_article',
        ),
    ]