# Generated by Django 2.2.4 on 2019-11-03 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
