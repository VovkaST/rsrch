from django.contrib import admin

from ending_pages_app.models import EndingPages


@admin.register(EndingPages)
class QuestionnairesAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
