from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def promt_user(request):
    try:
        user_id = request.session['user_id']
    except:
        raise Http404
    user = User.objects.get(pk=user_id)
    return HttpResponse("login successfully")