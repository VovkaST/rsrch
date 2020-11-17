from django.contrib import admin

from forms_app.models import Forms


@admin.register(Forms)
class QuestionnairesFormsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
