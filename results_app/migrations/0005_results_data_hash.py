# Generated by Django 3.1.3 on 2020-11-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results_app', '0004_results_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='data_hash',
            field=models.CharField(max_length=32, null=True, verbose_name='Хэш заполенных данных'),
        ),
    ]
