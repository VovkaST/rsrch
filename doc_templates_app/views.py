from django.urls import reverse
from django.views import generic

from doc_templates_app.forms import DocTemplatesForm
from doc_templates_app.models import DocTemplates


class DocTemplatesUpdateView(generic.UpdateView):
    model = DocTemplates
    form_class = DocTemplatesForm
    template_name = 'doc_templates_app/doctemplates_edit.html'

    def get_success_url(self):
        return reverse('doc_templates_list')


class DocTemplatesListView(generic.ListView):
    model = DocTemplates


class DocTemplatesCreateView(generic.CreateView):
    template_name = 'doc_templates_app/doctemplates_create.html'
    form_class = DocTemplatesForm

    def get_success_url(self):
        return reverse('doc_templates_list')
