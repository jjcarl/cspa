from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import StartTimeForm, AppointmentForm


class MakeStartTime(CreateView):
    form_class = StartTimeForm


class ScheduleAppointment(CreateView):
    form_class = AppointmentForm
