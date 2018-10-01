from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home:Home')
    else:
        form = UserCreationForm()
    return render(request, 'login/login.html', {'form' : form })
