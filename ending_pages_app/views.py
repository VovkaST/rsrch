from django.urls import reverse
from django.views import generic

from ending_pages_app.forms import EndingPagesForm
from ending_pages_app.models import EndingPages


class EndingPagesListView(generic.ListView):
    model = EndingPages


class EndingPagesCreateView(generic.CreateView):
    form_class = EndingPagesForm
    template_name = 'ending_pages_app/endingpages_create.html'

    def get_success_url(self):
        return reverse('ending_pages_list')


class EndingPagesUpdateView(generic.UpdateView):
    model = EndingPages
    form_class = EndingPagesForm
    template_name = 'ending_pages_app/endingpages_edit.html'

    def get_success_url(self):
        return reverse('ending_pages_list')
