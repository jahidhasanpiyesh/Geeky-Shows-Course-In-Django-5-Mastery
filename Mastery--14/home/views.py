from django.shortcuts import render, HttpResponseRedirect
from .forms import homeget, homepost
# Create your views here.

# use or GET Request Method
def home_get(request):
    if request.method == 'GET':
        fm = homeget(request.GET)
        if fm.is_valid():
            fm.cleaned_data
            return HttpResponseRedirect('/')
    else:
        fm = homeget()
    return render(request, 'html/GET.html', {'fm': fm})

# Use of POST Request Method
def home_post(request):
    if request.method == 'POST':
        post = homepost(request.POST)
        if post.is_valid():
            post.cleaned_data
            return HttpResponseRedirect('/post/')
    else:
        post = homepost()
    return render(request, 'html/POST.html', {'post':post})