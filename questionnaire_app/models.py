from django.db import models

from transliterate import slugify

from doc_templates_app.models import DocTemplates
from ending_pages_app.models import EndingPages
from forms_app.models import Forms


class Questionnaires(models.Model):
    slug = models.SlugField('Ссылка', max_length=255, unique=True)
    title = models.CharField('Название анкеты', max_length=255)
    description = models.TextField('Описание', max_length=2000)
    form = models.ForeignKey(Forms, verbose_name='Базовая форма', on_delete=models.CASCADE,
                             related_name='questionnaire_form')
    document = models.ForeignKey(DocTemplates, verbose_name='Шаблон', on_delete=models.CASCADE,
                                 related_name='document_template')
    ending_page = models.ForeignKey(EndingPages, verbose_name='Страница завершения', on_delete=models.CASCADE,
                                    related_name='ending_page')
    meta = models.JSONField('Мета данные', blank=True)
    created_at = models.DateTimeField('Дата, время создания', auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        self.slug = slugify(self.title)

    class Meta:
        db_table = 'rsrch_questionnaires'
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'
