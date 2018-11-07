from django.shortcuts import render, redirect
from django.http import Http404

# Create your views here.
def rolechoice_view(request):
    try:
        user_id = request.session['user_id']
        if user_id is not None:
            return render(request, 'rolechoice/rolechoice.html')
        else:
            raise Http404
    except:
        return redirect('Home:Home')