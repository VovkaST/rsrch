from django import forms
from django.forms import Form


class TemplatedForm(Form):
    def __init__(self, fields_list, *args, **kwargs):
        for field in fields_list:
            if field['type'] == 'textarea':
                field_instance = forms.CharField(label=field['name'], widget=forms.Textarea())
            elif field['type'] == 'input':
                field_instance = forms.CharField(label=field['name'])
            else:
                continue
            self.base_fields[field['var_name']] = field_instance
        self.base_fields['user_email'] = forms.EmailField(label='Адрес электронной почты для отправки результатов')
        super().__init__(*args, **kwargs)
