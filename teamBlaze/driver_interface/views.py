from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import Http404
from .forms import *
from accounts.models import *
from .models import *

# Create your views here.

def driver_view(request):
    user_id = request.session['user_id']
    if user_id is not None:
        user = User.objects.get(id = user_id)
        my_user = user.myuser
        first_name = my_user.first_name
        context = {'first_name' : first_name}
        return render(request, 'driver_interface/driver_options.html', context)
    else:
        return Http404

def post_car_pool(request):
    user_id = request.session['user_id']
    if user_id is not None:
        form = createCarPoolForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['seats']
            destination_state = form.cleaned_data['destination_state']
            city = form.cleaned_data['city']
            price = form.cleaned_data['price']
            bags = form.cleaned_data['bags']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            user = User.objects.get(id=user_id)
            car_pool_post = CarPoolPost(seats=seats, destination_state=destination_state, city=city, price=price, bags=bags,
                                        date=date, time=time, user=user)
            car_pool_post.save()
            return redirect('driver_interface:driver_view')
        return render(request, 'driver_interface/create_car_pool.html', {'form':form})
    else:
        return Http404

def create_car(request):
    user_id = request.session['user_id']
    if user_id is not None:
        form = carForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['seats']
            year = form.cleaned_data['year']
            model = form.cleaned_data['model']
            manufacturer = form.cleaned_data['manufacturer']
            user = User.objects.get(id = user_id)
            car = Car(seats = seats, year = year, model = model, manufacturer = manufacturer, user = user)
            car.save()
            return redirect('driver_interface:driver_view')
        return render(request, 'driver_interface/create_car.html', {'form': form})
    else:
        return Http404
