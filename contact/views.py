from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    
    else:
        form = NewForm()

    return render(request, 'contact/cont.html', {'form': form})