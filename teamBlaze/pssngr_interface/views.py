from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pssngr_view(request):
    return HttpResponse("you are a passenger")