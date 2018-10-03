from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def rolechoice_view(request):
    user_id = request.session['user_id']
    if user_id is not None:
        user = User.objects.get(pk=user_id)
        return HttpResponse("login successfully")
    else:
        raise Http404