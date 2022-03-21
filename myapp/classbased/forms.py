from xml.dom import ValidationErr
from django import forms

from .models import UserSample, AnotherSample


class ClassAndUserTestForm(forms.ModelForm):
    class Meta:
        model = UserSample
        fields = [
            'name',
            'desc'
        ]


class FormTestForm(forms.ModelForm):
    # name = forms.
    class Meta:
        model = AnotherSample
        fields = [
            'name',
            'desc'
        ]

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        print(name)
        if name == "akhil":
            raise forms.ValidationError('Name Never Become Akhil')
        return name
    '''
    this is over ride the save method
    '''
    def save(self, commit=True, *args, **kwargs):
        obj = super(FormTestForm, self).save(commit=False)
        obj.name = obj.name + "haha"
        print(obj)
        if commit:
            obj.save()
        return obj

