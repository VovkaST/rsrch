from django.db import models

from forms_app.models import Forms
from questionnaire_app.models import Questionnaires


class Results(models.Model):
    link = models.CharField('Ссылка', max_length=32, unique=True)
    questionnaire = models.ForeignKey(Questionnaires, verbose_name='Анкета', on_delete=models.CASCADE,
                                      related_name='questionnaire')
    form = models.ForeignKey(Forms, verbose_name='Базовая форма', on_delete=models.CASCADE,
                             related_name='base_form')
    data = models.JSONField('Сохраненные данные')
    created_at = models.DateTimeField('Дата, время создания', auto_now_add=True)

    class Meta:
        db_table = 'rsrch_results'
        ordering = ['form', ]
        verbose_name = 'Заполненная анкета'
        verbose_name_plural = 'Заполненные анкеты'
