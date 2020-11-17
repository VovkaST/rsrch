from django.db import models

from forms_app.models import Forms


class Questionnaires(models.Model):
    # id = models.AutoField(primary_key=True)
    slug = models.SlugField('Ссылка', max_length=255, unique=True)
    title = models.CharField('Название анкеты', max_length=255)
    description = models.CharField('Описание', max_length=255)
    form = models.ForeignKey(Forms, verbose_name='Базовая форма', on_delete=models.CASCADE,
                             related_name='questionnaire_form')
    # document = models.ForeignKey()
    meta = models.JSONField('Мета данные')
    created_at = models.DateTimeField('Дата, время создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'rsrch_questionnaires'
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'
