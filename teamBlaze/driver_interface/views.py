from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def driver_view(request):
    user_id = request.session['user_id']
    user = User.objects.get(id = user_id)
    my_user = user.myuser
    first_name = my_user.first_name
    context = {'first_name' : first_name}
    return render(request, 'driver_interface/driver_options.html', context)
