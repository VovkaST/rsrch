from django.db import models
from transliterate import slugify


class Forms(models.Model):
    title = models.CharField('Название формы', max_length=255)
    description = models.TextField('Описание', max_length=2000)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    form_fields = models.JSONField('Конструктор формы', blank=True)
    created_at = models.DateTimeField('Дата, время создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'rsrch_forms'
        indexes = [
            models.Index(fields=['title'], name='rsrch_forms_title_idx'),
        ]
        verbose_name = 'Форма анкеты'
        verbose_name_plural = 'Формы анкеты'

    def clean(self):
        self.slug = slugify(self.title)
