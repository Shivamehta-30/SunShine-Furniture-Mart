# Generated by Django 3.2.4 on 2021-07-01 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='suppayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('cash', 'cash'), ('netbank', 'netbank'), ('upi', 'upi'), ('cheque', 'cheque')], max_length=80)),
                ('bank_name', models.CharField(blank=True, max_length=80, null=True)),
                ('bank_branch', models.CharField(blank=True, max_length=400, null=True)),
                ('account_no', models.CharField(blank=True, max_length=80, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=80, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('upi', models.CharField(blank=True, max_length=80, null=True)),
                ('cash', models.IntegerField(blank=True, default=0, null=True)),
                ('check_no', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('check_date', models.CharField(blank=True, default='', max_length=35, null=True)),
                ('sup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='supplier.supplier')),
            ],
        ),
    ]
