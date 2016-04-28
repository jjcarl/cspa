from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^make_start_time/$', views.make_start_time, name='make-start-time'),
    url(r'^make_appointment/$', views.make_appointment, name='schedule-appointment'),
    url(r'^view_appointment/$', views.view_appointments, name='view-appointments'),
]
