# Generated by Django 3.2.5 on 2021-07-16 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplierpayment', '0008_alter_suppayment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 7, 59, 46, 721447)),
        ),
    ]
