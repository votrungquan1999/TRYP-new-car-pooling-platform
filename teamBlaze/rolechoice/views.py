from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def promt_user(request):
    return HttpResponse("THIS IS A SITE WHERE YOU ASK USER TO CHOOSE THE ROLE")