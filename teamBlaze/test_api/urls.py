from django.urls import path
from . import views

app_name = 'test_api'

urlpatterns = [
    path('', views.test_uber_api, name = 'test_api')
]