from django import forms

from ending_pages_app.models import EndingPages


class EndingPagesForm(forms.ModelForm):
    class Meta:
        model = EndingPages
        exclude = ['slug', 'created_at', ]
