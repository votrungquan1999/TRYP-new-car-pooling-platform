from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.models import User
from .forms import *
from accounts.models import *
from accounts.views import *
from .models import *
from pssngr_interface.models import *

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
            destination_city = form.cleaned_data['destination_city']
            departure_state = form.cleaned_data['departure_state']
            departure_city = form.cleaned_data['departure_city']
            price = form.cleaned_data['price']
            bags = form.cleaned_data['bags']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            title = form.cleaned_data['title']
            user = User.objects.get(id=user_id)
            my_user = user.myuser
            car_pool_post = CarPoolPost(seats=seats, destination_state=destination_state, destination_city=destination_city,
                                        price=price, bags=bags, date=date, time=time, my_user=my_user, departure_city = departure_city,
                                        departure_state = departure_state, title = title)
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
            my_user = (User.objects.get(id = user_id)).myuser

            car = Car(seats = seats, year = year, model = model, manufacturer = manufacturer, my_user = my_user)
            car.save()
            return redirect('driver_interface:driver_view')
        return render(request, 'driver_interface/create_car.html', {'form': form})
    else:
        return Http404

def check_car_pool(request):
    user_id = request.session['user_id']
    if user_id is not None:
        user = User.objects.get(id= user_id)
        my_user = user.myuser
        car_pool_posts = my_user.carpoolpost_set.all()
        return render(request, 'driver_interface/check_car_pool.html', {'car_pool_posts':car_pool_posts})
    else:
        return Http404

def detail_car_pool(request, post_id):
    post = get_object_or_404(CarPoolPost, id = post_id)
    return render(request, 'driver_interface/detail_car_pool.html', {'post' : post})

def find_passenger(request):
    user_id = request.session['user_id']
    if user_id is not None:
        form = findPassengerForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id = user_id)
            my_user = user.myuser
            destination_state = form.cleaned_data['destination_state']
            destination_city = form.cleaned_data['destination_city']
            departure_state = form.cleaned_data['departure_state']
            departure_city = form.cleaned_data['departure_city']
            date = form.cleaned_data['date']
            '''need_ride_posts = NeedRidePost.objects.filter(destination_city = destination_city
                                                          ).filter(destination_state = destination_state
                                                          ).filter(departure_city = departure_city
                                                          ).filter(departure_state = departure_state)
                #.filter(date = date)'''
            need_ride_posts = NeedRidePost.objects.all()
            posts = []
            for post in need_ride_posts:
                if post.destination_state == destination_state and post.departure_state == departure_state:
                    if post.departure_city == departure_city and post.destination_city == destination_city:
                        if post.date == date:
                            posts.append(post)
            #form.save()
            return render(request, 'driver_interface/find_passenger.html', {'form' : form,
                                                                            'posts' : need_ride_posts})
            #return Http404
        else:
            return render(request, 'driver_interface/find_passenger.html', {'form' : form})
