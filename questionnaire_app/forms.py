from django import forms
from questionnaire_app.models import Questionnaires


class QuestionnaireCreateForm(forms.ModelForm):
    class Meta:
        model = Questionnaires
        exclude = ('slug', 'created_at', )
        widgets = {
            'meta': forms.HiddenInput()
        }
