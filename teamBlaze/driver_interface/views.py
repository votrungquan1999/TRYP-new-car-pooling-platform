from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import Http404
from .forms import *
from accounts.models import *

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
    pass

def create_car(request):
    user_id = request.session['user_id']
    if user_id is not None:
        form = carForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['seats']
            year = form.cleaned_data['year']
            model = form.cleaned_data['model']
            manufacturer = form.cleaned_data['manufacturer']
            my_user = (User.objects.get(id = user_id)).myuser
            car = Car(seats = seats, year = year, model = model, manufacturer = manufacturer, my_user = my_user)
            car.save()
<<<<<<< HEAD
            redirect("driver_interface:driver_view")
=======
            return redirect('driver_interface:driver_view')
>>>>>>> 8cf950ed50d699cb90dac7c871b259f0d2951805
        return render(request, 'driver_interface/create_car.html', {'form': form})
    else:
        return Http404
