from django.urls import path
from . import views

app_name = 'pssngr_interface'

urlpatterns = [
    path('', views.pssngr_view, name = "pssngr_view"),
]