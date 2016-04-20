from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^manage_treatments/$', views.manage_treatments, name='manage-treatments'),
    url(r'^manage_product/$', views.manage_products, name='manage-products'),
]