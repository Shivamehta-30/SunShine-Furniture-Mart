# Generated by Django 3.2.5 on 2021-07-11 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplierpayment', '0002_auto_20210711_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 11, 11, 15, 56, 123113)),
        ),
    ]
