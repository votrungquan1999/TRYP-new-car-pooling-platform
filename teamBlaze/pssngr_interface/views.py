from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.models import User
from .forms import createNeedRideForm, findDriverForm, addPassengerForm
from .models import NeedRidePost
from driver_interface.models import CarPoolPost
from accounts.models import MyUser

# Create your views here.
def pssngr_view(request):
    try:
        user_id = request.session['user_id']
        if user_id is not None:
            user = User.objects.get(id=user_id)
            my_user = user.myuser
            first_name = my_user.first_name
            context = {'first_name': first_name}
            return render(request, 'pssngr_interface/passenger_options.html', context)
        else:
            return Http404
    except:
        return redirect('Home:Home')

def post_need_ride(request):
    try:
        user_id = request.session['user_id']
    except:
        return redirect('Home:Home')

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
            driver = User.objects.get(username = 'test123')
            need_ride_post = NeedRidePost(seats=seats, destination_state=destination_state, destination_city=destination_city,
                                        price=price, bags=bags, date=date, time=time, my_user=my_user, departure_city = departure_city,
                                        departure_state = departure_state, title = title, driver = driver)
            need_ride_post.save()
            return redirect('pssngr_interface:passenger_view')
        return render(request, 'pssngr_interface/create_need_ride.html', {'form':form})
    else:
        return Http404


def check_need_ride(request):
    try:
        user_id = request.session['user_id']
    except:
        return redirect('Home:Home')
    if user_id is not None:
        user = User.objects.get(id= user_id)
        my_user = user.myuser
        #need_ride_posts = my_user.need_ride_post_set.all()
        need_ride_posts = NeedRidePost.objects.all()
        posts = []
        for post in need_ride_posts:
            if post.my_user is my_user:
                posts.append(post)
        return render(request, 'pssngr_interface/check_need_ride.html', {'posts':posts})
    else:
        return redirect('Home:Home')

def detail_need_ride(request, post_id):
    post = get_object_or_404(NeedRidePost, id = post_id)
    return render(request, 'pssngr_interface/detail_need_ride.html', {'post' : post})

def find_driver(request):
    try:
        user_id = request.session['user_id']
        if user_id is not None:
            form = findDriverForm(request.POST)
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
                car_pool_posts = CarPoolPost.objects.all()
                posts = []
                for post in car_pool_posts:
                    if post.destination_state == destination_state and post.departure_state == departure_state:
                        if post.departure_city == departure_city and post.destination_city == destination_city:
                            if post.date == date and post.seats > 0:
                                posts.append(post)
                #form.save()
                return render(request, 'pssngr_interface/find_driver.html', {'form' : form,
                                                                             'posts' : posts})
                #return Http404
            else:
                return render(request, 'pssngr_interface/find_driver.html', {'form' : form})
    except:
        return redirect('Home:Home')



def add_passenger(request, post_id):
    try:
        post = CarPoolPost.objects.get(id = post_id)
        user_id = request.session['user_id']
    except:
        return Http404

    if user_id is not None:
        form = addPassengerForm(request.POST)
        user = User.objects.get(id = user_id)
        if form.is_valid():
            confirm = form.cleaned_data['confirm']
            if confirm == 'CONFIRM':
                post.passengers.add(user)
                post.seats -= 1
                post.save()
                return redirect('pssngr_interface:passenger_view')
            else:
                return render(request, 'pssngr_interface/add_passenger.html', {'form' : form,
                                                                               'post' : post})
        else:
            return render(request, 'pssngr_interface/add_passenger.html', {'form': form,
                                                                           'post': post})
    else:
        return Http404
