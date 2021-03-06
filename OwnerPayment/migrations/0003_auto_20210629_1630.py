# Generated by Django 3.2.4 on 2021-06-29 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OwnerPayment', '0002_rename_payment_ownerpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerpayment',
            name='cheque_date',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ownerpayment',
            name='cheque_no',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='ownerpayment',
            name='type',
            field=models.CharField(choices=[('cash', 'cash'), ('netbank', 'netbank'), ('upi', 'upi'), ('check', 'check')], max_length=80),
        ),
    ]
