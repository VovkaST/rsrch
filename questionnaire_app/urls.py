from django.urls import path
from questionnaire_app.views import (
    QuestionnairesListView, QuestionnaireCreateView, QuestionnaireUpdateView
)

urlpatterns = [
    path('', QuestionnairesListView.as_view(), name='questionnaires_list'),
    path('create', QuestionnaireCreateView.as_view(), name='questionnaire_create'),
    path('edit/<slug>', QuestionnaireUpdateView.as_view(), name='questionnaire_edit')
]
