from django import forms

from .models import Appointment, StartTime


class StartTimeForm(forms.ModelForm):
    class Meta:
        model = StartTime
        fields = ['start_time']
        widgets = {'start_time': forms.DateTimeField}


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {'start_time': forms.ModelChoiceField(
            queryset=StartTime.objects.filter(scheduled=False), to_field_name='start_time')}
