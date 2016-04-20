from django.shortcuts import render, redirect
from django.utils import timezone
# from django.views.generic.edit import CreateView

from .forms import StartTimeForm, AppointmentForm
from .models import StartTime, Appointment


def make_start_time(request):
    context = {}
    context['form'] = StartTimeForm()
    context['start_times'] = StartTime.objects.filter(scheduled=False, start_time__gt=timezone.now())
    if request.method == 'POST':
        form = StartTimeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'make_start_times.html', context)
        context['errors'] = form.errors
        return render(request, 'make_start_times.html', context)
    else:
        return render(request, 'make_start_times.html', context)


def make_appointment(request):
    context = {}
    context['form'] = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
        context['errors'] = form.errors
        return render(request, 'make_appointment.html', context)
    else:
        return render(request, 'make_appointment.html', context)


# TODO Try out these Class based views later
# class MakeStartTime(CreateView):
#     form_class = StartTimeForm
#
#
# class ScheduleAppointment(CreateView):
#     form_class = AppointmentForm
