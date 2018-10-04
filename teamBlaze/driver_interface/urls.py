from django.urls import path
from . import views

app_name = 'driver_interface'
urlpatterns = [
    path('', views.driver_view, name = 'driver_view'),
]