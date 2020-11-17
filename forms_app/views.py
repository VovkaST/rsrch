from django.urls import reverse
from django.views import generic

from forms_app.forms import FormsCreateForm, FieldFormSet
from forms_app.models import Forms


class FormsListView(generic.ListView):
    model = Forms


class FormDetailView(generic.DetailView):
    model = Forms


class FormCreateView(generic.CreateView):
    template_name = 'forms_app/form_create.html'
    form_class = FormsCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'formset' not in context:
            context.update({
                'formset': FieldFormSet(prefix='field')
            })
        return context

    def get_success_url(self):
        return reverse('forms_list')

    def post(self, request, *args, **kwargs):
        self.object = None
        formset = FieldFormSet(self.request.POST, prefix='field')
        form_kwargs = self.get_form_kwargs()
        data = form_kwargs['data'].copy()
        if formset.is_valid():
            data['form_fields'] = formset.cleaned_data
        else:
            data['form_fields'] = '{"1": "1231"}'
        form_kwargs['data'] = data
        form = self.form_class(**form_kwargs)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


