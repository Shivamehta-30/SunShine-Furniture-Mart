# Generated by Django 3.2.4 on 2021-06-29 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('house_no', models.CharField(max_length=100)),
                ('streetname', models.CharField(max_length=100)),
                ('areaname', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('phoneno', models.CharField(max_length=10)),
                ('DOB', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('DOJ', models.CharField(max_length=100)),
            ],
        ),
    ]
