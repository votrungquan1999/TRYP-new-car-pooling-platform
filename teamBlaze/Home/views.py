from django.shortcuts import render

def Home(request):
    request.session['user_id'] = None
    return render(request, 'Home/homepage.html')
