# Generated by Django 3.1.3 on 2020-11-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results_app', '0003_results_filled_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='meta',
            field=models.JSONField(blank=True, default={}, verbose_name='Мета данные'),
            preserve_default=False,
        ),
    ]
