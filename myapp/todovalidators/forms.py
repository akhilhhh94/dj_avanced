from xml.dom import ValidationErr
from django import forms

from .models import todo

class TodoForms(forms.ModelForm):
    class Meta:
        model = todo
        fields = [
            'title'
        ]
    def clean_title(self):
        title = self.cleaned_data.get("title",  None)
        if title == "akhil":       
            raise ValidationErr("Akhil not allowd")
        
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title == "amela":       
            raise ValidationErr("amela not allowd")
        