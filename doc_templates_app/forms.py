from django import forms

from doc_templates_app.models import DocTemplates


class DocTemplatesForm(forms.ModelForm):
    class Meta:
        model = DocTemplates
        exclude = ['slug', 'created_at', ]
