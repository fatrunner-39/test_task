from django import forms
from .models import Users


class ChoiceNameForm(forms.Form):
    choice = forms.ModelChoiceField(label='Пользователь', queryset=Users.objects.all())

