from django.shortcuts import render
from django.http import HttpResponse,Http404
<<<<<<< HEAD

# Create your views here.
def rolechoice_view(request):
    if 
        return HttpResponse("THIS IS A SITE WHERE YOU ASK USER TO CHOOSE THE ROLE")
    else :
        return Http404
=======
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def promt_user(request):
    user_id = request.session['user_id']
    if user_id is not None:
        user = User.objects.get(pk=user_id)
        return HttpResponse("login successfully")
    else:
        raise Http404
>>>>>>> 969339d390d1cb13a4cd2a438a679f96046530af
