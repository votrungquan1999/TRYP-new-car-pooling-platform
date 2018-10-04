from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form })


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log user in
            user = form.get_user()
            login(request,user)
            request.session['user_id'] = user.id
            return redirect('roleChoice:roleChoice')


    else:
        form = AuthenticationForm()
    return render(request,"accounts/login.html",{'form':form})


def logout_view(request):
    if request.method =='POST':
        pass



def forgot_view(request):
    return render(request,"accounts/forgot.html")
