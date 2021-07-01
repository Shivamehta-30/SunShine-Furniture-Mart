# Generated by Django 3.2.4 on 2021-07-01 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('description', models.TextField(blank=True, null=True)),
                ('maincategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='category.category')),
            ],
        ),
    ]
