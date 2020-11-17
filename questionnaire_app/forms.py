from django import forms
from forms_app.models import Forms


class QuestionnaireFormCreateForm(forms.ModelForm):
    class Meta:
        model = Forms
        exclude = ('slug', 'meta', 'created_at', )
        # widgets = {
        #     'slug': forms.TextInput()
        # }
