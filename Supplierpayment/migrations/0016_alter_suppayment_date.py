# Generated by Django 3.2.5 on 2021-07-19 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplierpayment', '0015_alter_suppayment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 19, 6, 21, 0, 184362)),
        ),
    ]
