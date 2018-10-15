from django.shortcuts import render

# Create your views here.
def driver_view(request):
    user_id = request.session['user_id']
    
    return render(request, 'driver_interface/driver_options.html')
