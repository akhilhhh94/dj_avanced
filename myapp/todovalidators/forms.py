from django import forms

from .models import todo

class TodoForms(forms.ModelForm):
    class Meta:
        model = todo
        fields = [
            'title'
        ]