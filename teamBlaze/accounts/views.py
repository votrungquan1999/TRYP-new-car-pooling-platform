from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home:Home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form })


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect('roleChoice:roleChoice')
    else:
        form = AuthenticationForm()
    return render(request,"accounts/login.html",{'form':form})
