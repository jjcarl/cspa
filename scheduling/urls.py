from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^make_start_time/$', views.MakeStartTime.as_view(), name='make-start-time'),
    url(r'^schedule_appointment/$', views.ScheduleAppointment.as_view(), name='schedule-appointment'),
]
