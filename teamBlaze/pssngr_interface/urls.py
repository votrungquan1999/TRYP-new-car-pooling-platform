from django.urls import path
from . import views

app_name = 'pssngr_interface'

urlpatterns = [
    path('', views.pssngr_view, name = "passenger_view"),
    path('create_need_ride/', views.post_need_ride, name = 'create_need_ride'),
    path('check_need_ride/<int:post_id>/', views.detail_need_ride, name = 'detail_need_ride'),
    path('check_need_ride/', views.check_need_ride, name = 'check_need_ride'),
    path('find_driver/', views.find_driver, name = 'find_driver'),
    path('add_passenger/<int:post_id>/', views.add_passenger, name = 'add_passenger')
]