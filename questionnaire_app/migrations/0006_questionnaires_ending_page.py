# Generated by Django 3.1.3 on 2020-11-22 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ending_pages_app', '0001_initial'),
        ('questionnaire_app', '0005_auto_20201121_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaires',
            name='ending_page',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ending_page', to='ending_pages_app.endingpage', verbose_name='Страница завершения'),
            preserve_default=False,
        ),
    ]