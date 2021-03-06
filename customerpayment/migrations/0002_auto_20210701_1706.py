# Generated by Django 3.2.4 on 2021-07-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerpayment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerpay',
            name='type',
            field=models.CharField(choices=[('cash', 'cash'), ('netbank', 'netbank'), ('upi', 'upi'), ('cheque', 'cheque')], default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='customerpay',
            name='account_no',
            field=models.CharField(blank=True, default='', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='customerpay',
            name='bank_branch',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='customerpay',
            name='bank_name',
            field=models.CharField(blank=True, default='', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='customerpay',
            name='ifsc_code',
            field=models.CharField(blank=True, default='', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='customerpay',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customerpay',
            name='upi',
            field=models.CharField(blank=True, default='', max_length=80, null=True),
        ),
    ]
