# Generated by Django 3.1.3 on 2020-11-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results_app', '0005_results_data_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='created_at',
            field=models.DateTimeField(auto_created=True, verbose_name='Дата, время создания'),
        ),
    ]
