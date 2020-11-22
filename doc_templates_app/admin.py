from django.contrib import admin

from doc_templates_app.models import DocTemplates


@admin.register(DocTemplates)
class QuestionnairesAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
