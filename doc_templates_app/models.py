from django.db import models
from tinymce.models import HTMLField
from transliterate import slugify


class DocTemplates(models.Model):
    slug = models.SlugField('slug', max_length=255, unique=True, blank=True)
    title = models.CharField('Название', max_length=255)
    content = HTMLField('Содержание', max_length=2000)
    created_at = models.DateTimeField('Дата, время создания', auto_now_add=True)

    def clean(self):
        self.slug = slugify(self.title)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'rsrch_doc_templates'
        verbose_name = 'Шаблон документов'
        verbose_name_plural = 'Шаблоны документов'
