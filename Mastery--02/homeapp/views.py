from django.shortcuts import render

# Create your views here.

def homeapp(req):
    return render(req, 'homeapp/index.html')