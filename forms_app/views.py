from django.urls import reverse
from django.views import generic

from forms_app.forms import FormsCreateForm, FieldFormSet
from forms_app.models import Forms


class DynamicFormMixin(object):
    def get_success_url(self):
        return reverse('forms_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        initial = self.object.form_fields if self.object else None
        if 'formset' not in context:
            formset = FieldFormSet(prefix='field', initial=initial)
            formset.extra = 0 if initial else 1
            context.update({
                'formset': formset
            })
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
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


class FormsListView(generic.ListView):
    model = Forms


class FormUpdateView(DynamicFormMixin, generic.UpdateView):
    form_class = FormsCreateForm
    model = Forms
    template_name = 'forms_app/forms_edit.html'


class FormCreateView(DynamicFormMixin, generic.CreateView):
    template_name = 'forms_app/form_create.html'
    form_class = FormsCreateForm
    model = Forms

    def get_object(self, queryset=None):
        return
