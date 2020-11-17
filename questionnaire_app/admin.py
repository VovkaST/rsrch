from django.contrib import admin
from questionnaire_app.models import Questionnaires


@admin.register(Questionnaires)
class QuestionnairesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
