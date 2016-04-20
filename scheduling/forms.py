from django import forms

from core.models import Treatment, Product
from .models import Appointment, StartTime


class StartTimeForm(forms.ModelForm):
    class Meta:
        model = StartTime
        fields = ['start_time']
        widgets = {'start_time': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a date and a time - MM/DD/YY HH:MM'})}


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ['user']
        field_classes = {'start_time': forms.ModelChoiceField(
            queryset=StartTime.objects.filter(scheduled=False)),
            'treatment': forms.ModelChoiceField(queryset=Treatment.objects.all())
        }
