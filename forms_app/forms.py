from django import forms
from django.core.exceptions import ValidationError
from django.forms import HiddenInput

from forms_app.models import Forms


class FormsCreateForm(forms.ModelForm):
    class Meta:
        model = Forms
        exclude = ['slug', 'created_at', ]
        widgets = {
            'form_fields': HiddenInput()
        }


class FieldForm(forms.Form):
    FIELD_TYPES = (
        ('textarea', 'textarea'),
    )
    name = forms.CharField(label='Название поля', min_length=3, max_length=255, required=True)
    type = forms.Field(label='Тип поля', widget=forms.Select(choices=FIELD_TYPES))
    var_name = forms.SlugField(label='Название переменной', min_length=3, max_length=255)


class BaseFieldFormSet(forms.BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        vars = []
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue
            var = form.cleaned_data.get('var_name')
            if var in vars:
                raise ValidationError('Имена переменных должны быть уникальны!')
            vars.append(var)


FieldFormSet = forms.formset_factory(FieldForm, formset=BaseFieldFormSet)
