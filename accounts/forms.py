from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    is_coach = forms.BooleanField(required=False, label="Inscription en tant que coach")

    class Meta:
        model = CustomUser
        fields = ("username", "email", "is_coach", "password1", "password2")