from django.shortcuts import render
from django.views import generic

from results_app.models import Results


class QuestionnaireFillView(generic.CreateView):
    model = Results
    template_name = 'results_app/results_list.html'
