from django import forms
from django.contrib.auth.models import User, Group

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    group = forms.ChoiceField(choices=[('Client', 'Client'), ('Coach', 'Coach')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'group']