from xml.dom import ValidationErr
from django import forms

from .models import UserSample


class ClassAndUserTestForm(forms.ModelForm):
    class Meta:
        model = UserSample
        fields = [
            'name',
            'desc'
        ]
