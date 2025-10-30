from django.shortcuts import render, HttpResponseRedirect
from .forms import userlogin
# Create your views here.
def home_view(request):
    if request.method == 'POST':
        form = userlogin(request.POST)
        if form.is_valid():
            form.cleaned_data
            return HttpResponseRedirect('/')
    else:
        form = userlogin()
    return render(request, 'HTML/index.html', {'form': form})