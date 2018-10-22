from django.shortcuts import render
from .forms import Feedback_Form

def Home(request):
    request.session['user_id'] = None
    return render(request, 'Home/homepage.html')

def Feedback_view(request):
    form = Feedback_Form(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'Home/feedback.html', context )
