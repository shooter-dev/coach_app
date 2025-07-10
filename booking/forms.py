from django import forms
from .models import Booking
from django.forms import DateTimeInput

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date']
        widgets = {
            'date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
