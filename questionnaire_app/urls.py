from django.urls import path
from questionnaire_app.views import (
    QuestionnairesListView, QuestionnaireCreateView, QuestionnaireDetailView
)

urlpatterns = [
    path('', QuestionnairesListView.as_view(), name='questionnaires_list'),
    path('create', QuestionnaireCreateView.as_view(), name='questionnaire_create'),
    path('<slug>', QuestionnaireDetailView.as_view(), name='questionnaire_view')
]
