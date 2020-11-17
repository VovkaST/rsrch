from django.urls import path, re_path
from questionnaire_app.views import (
    QuestionnairesListView, QuestionnaireCreateView,
)
from forms_app.views import FormDetailView, FormCreateView

urlpatterns = [
    path('', QuestionnairesListView.as_view(), name='questionnaires_list'),
    path('create', QuestionnaireCreateView.as_view(), name='questionnaire_create'),
    path('<slug>', FormDetailView.as_view(), name='questionnaire_view')
]
