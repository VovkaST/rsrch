# Generated by Django 3.1.3 on 2020-11-17 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaires',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
    ]
