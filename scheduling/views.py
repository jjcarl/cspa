from django.shortcuts import render
from django.utils import timezone

from .forms import StartTimeForm, AppointmentForm
from .models import StartTime, Appointment


def make_start_time(request):
    context = dict()
    context['form'] = StartTimeForm()
    context['start_times'] = StartTime.objects.filter(
        scheduled=False, start_time__gt=timezone.now()).order_by('start_time')
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
    context = dict()
    context['form'] = AppointmentForm()
    if request.method == 'POST':
        new_app = Appointment(user=request.user)
        form = AppointmentForm(request.POST, instance=new_app)
        if form.is_valid():
            form.save()
        context['errors'] = form.errors
        return render(request, 'make_appointment.html', context)
    else:
        return render(request, 'make_appointment.html', context)


def view_appointments(request):
    appointments = Appointment.objects.filter(start_time__start_time__gt=timezone.now()).order_by(
        'start_time').select_related('treatment', 'start_time')
    return render(request, 'appointments.html', {'appointments': appointments})
