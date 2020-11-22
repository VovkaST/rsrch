from django.db import models

from doc_templates_app.models import DocTemplates
from ending_pages_app.models import EndingPages
from forms_app.models import Forms
from questionnaire_app.models import Questionnaires


class Results(models.Model):
    link_fill_out = models.CharField('Ссылка для заполнения', max_length=36, unique=True)
    link_view_ending = models.CharField('Ссылка для просмотра результатов (страница завершения)',
                                        max_length=36, unique=True, null=True)
    questionnaire = models.ForeignKey(Questionnaires, verbose_name='Анкета', on_delete=models.CASCADE,
                                      related_name='questionnaire')
    form = models.ForeignKey(Forms, verbose_name='Базовая форма', on_delete=models.CASCADE,
                             related_name='base_form')
    document = models.ForeignKey(DocTemplates, verbose_name='Шаблон', on_delete=models.CASCADE,
                                 related_name='result_document_template')
    ending_page = models.ForeignKey(EndingPages, verbose_name='Страница завершения', on_delete=models.CASCADE,
                                    related_name='result_ending_page')
    data = models.JSONField('Сохраненные данные')
    user_email = models.EmailField('Адрес электронной почты для отправки результатов')
    data_hash = models.CharField('Хэш заполенных данных', max_length=32, null=True)
    meta = models.JSONField('Мета данные', null=True)
    created_at = models.DateTimeField('Дата, время создания', auto_now_add=True)
    filled_at = models.DateTimeField('Дата, время заполнения', null=True, blank=True)

    class Meta:
        db_table = 'rsrch_results'
        ordering = ['form', ]
        verbose_name = 'Заполненная анкета'
        verbose_name_plural = 'Заполненные анкеты'
