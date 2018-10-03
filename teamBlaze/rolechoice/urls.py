from django.urls import path
from . import views

app_name = 'roleChoice'
urlpatterns = [
    path('', views.rolechoice_view, name = "roleChoice")
]
