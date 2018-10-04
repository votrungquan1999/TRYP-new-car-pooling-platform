from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def driver_view(request):
    return HttpResponse("you are a driver")
