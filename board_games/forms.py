from django import forms
from .models import BoardGame

class BoardgameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['name']
        labels = {'name': ''}
