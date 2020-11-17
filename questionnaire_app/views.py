from django.views import generic

from questionnaire_app.forms import QuestionnaireFormCreateForm
from questionnaire_app.models import Questionnaires


class QuestionnairesListView(generic.ListView):
    model = Questionnaires


class QuestionnaireDetailView(generic.DetailView):
    model = Questionnaires


class QuestionnaireCreateView(generic.CreateView):
    # model = Questionnaires
    form_class = QuestionnaireFormCreateForm
    template_name = 'questionnaire_app/questionnaire_create.html'
    # fields = ['title', 'slug', 'description', 'form']
