from django.urls import reverse
from django.views import generic

from questionnaire_app.forms import QuestionnaireCreateForm
from questionnaire_app.models import Questionnaires


class QuestionnairesListView(generic.ListView):
    model = Questionnaires


class QuestionnaireDetailView(generic.DetailView):
    model = Questionnaires


class QuestionnaireCreateView(generic.CreateView):
    form_class = QuestionnaireCreateForm
    template_name = 'questionnaire_app/questionnaire_create.html'

    def get_success_url(self):
        return reverse('questionnaires_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == 'POST':
            data = kwargs['data'].copy()
            data.update({
                'meta': {
                    'REMOTE_ADDR': self.request.META.get('REMOTE_ADDR'),
                    'HTTP_USER_AGENT': self.request.META.get('HTTP_USER_AGENT'),
                }
            })
            kwargs['data'] = data
        return kwargs
