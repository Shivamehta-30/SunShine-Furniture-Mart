# Generated by Django 3.2.5 on 2021-07-13 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerpayment', '0003_auto_20210711_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerpay',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 13, 15, 44, 7, 611270)),
        ),
    ]