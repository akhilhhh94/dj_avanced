from django import forms
from django.db.models.base import Model
from django.forms import fields

from .models import PostModel

class PostForms(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'title',
            'content'
        ]