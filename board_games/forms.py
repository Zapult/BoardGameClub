from django import forms
from .models import BoardGame, Loan

class BoardgameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['name', 'description', 'year', 'image']
        labels = {'name': '', 'description': '', 'year': ''}

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['game']

    def clean(self):
        cleaned_data = super().clean()
        user = self.cleaned_data.get('user')
        if user is None:
            raise forms.ValidationError("User data is missing.")
        if Loan.objects.filter(user=user).count()>= 3:
            raise forms.ValidationError("You have already borrowed three games.")
        return cleaned_data
