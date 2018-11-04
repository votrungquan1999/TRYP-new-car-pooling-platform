from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import Http404
from .forms import *
from accounts.models import *
from accounts.views import *
from .models import *

# Create your views here.
def pssngr_view(request):
    user_id = request.session['user_id']
    if user_id is not None:
        user = User.objects.get(id=user_id)
        my_user = user.myuser
        first_name = my_user.first_name
        context = {'first_name': first_name}
        return render(request, 'pssngr_interface/passenger_options.html', context)
    else:
        return Http404

def post_need_ride(request):
    user_id = request.session['user_id']
    if user_id is not None:
        form = createNeedRideForm(request.POST)
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
            need_ride_post = NeedRidePost(seats=seats, destination_state=destination_state, destination_city=destination_city,
                                        price=price, bags=bags, date=date, time=time, my_user=my_user, departure_city = departure_city,
                                        departure_state = departure_state, title = title)
            need_ride_post.save()
            return redirect('pssngr_interface:pssngr_view')
        return render(request, 'pssngr_interface/create_need_ride.html', {'form':form})
    else:
        return Http404

def check_need_ride(request):
    user_id = request.session['user_id']
    if user_id is not None:
        user = User.objects.get(id= user_id)
        my_user = user.myuser
        need_ride_posts = my_user.need_ride_post_set.all()
        return render(request, 'pssngr_interface/check_need_ride.html', {'car_pool_posts':need_ride_posts})

def detail_need_ride(request, post_id):
    post = get_object_or_404(NeedRidePost, id = post_id)
    return render(request, 'pssngr_interface/detail_need_ride.html', {'post' : post})