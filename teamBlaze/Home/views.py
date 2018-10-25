from django.shortcuts import render

def Home(request):
    request.session['user_id'] = None
    return render(request, 'Home/homepage.html')
<<<<<<< HEAD

def Feedback_view(request):
    form = Feedback_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(request)
    context = {'form': form}
    return render(request, 'Home/feedback.html', context )
=======
>>>>>>> 8aaa1d03f4735adefbd23aa9452515af70881a6f
