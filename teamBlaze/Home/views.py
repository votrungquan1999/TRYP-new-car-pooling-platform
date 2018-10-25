from django.shortcuts import render, redirect

def Home(request):
    try:
        user_id = request.session['user_id']
        if user_id is not None:
            return redirect('roleChoice:roleChoice')
        else:
            return render(request, 'Home/homepage.html')
    except:
        return render(request, 'Home/homepage.html')

'''def Feedback_view(request):
    form = Feedback_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(request)
    context = {'form': form}
    return render(request, 'Home/feedback.html', context )'''
