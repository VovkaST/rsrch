# Generated by Django 3.1.3 on 2020-11-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results_app', '0009_auto_20201122_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='user_email',
            field=models.EmailField(default='test@mail.ru', max_length=254, verbose_name='Адрес электронной почты для отправки результатов'),
            preserve_default=False,
        ),
    ]
