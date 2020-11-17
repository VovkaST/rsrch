from django.contrib import admin

# Register your models here.
from results_app.models import Results


@admin.register(Results)
class QuestionnairesFilledAdmin(admin.ModelAdmin):
    list_display = ['questionnaire', 'created_at']