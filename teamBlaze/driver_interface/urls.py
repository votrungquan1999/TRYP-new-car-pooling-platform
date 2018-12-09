from django.urls import path
from . import views

app_name = 'driver_interface'
urlpatterns = [
    path('', views.driver_view, name = 'driver_view'),
    path('create_car/', views.create_car, name = 'create_car'),
    path('create_car_pool/', views.post_car_pool, name = 'create_car_pool'),
    path('check_car_pool/<int:post_id>/', views.detail_car_pool, name = 'detail_car_pool'),
    path('check_car_pool/', views.check_car_pool, name = 'check_car_pool'),
    path('find_passenger/', views.find_passenger, name = 'find_passenger'),
    path('add_driver/<int:post_id>/', views.add_driver, name = 'add_driver'),
    path('compare_price/', views.compare_price, name = 'compare_price'),
]