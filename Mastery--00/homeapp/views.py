from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request, **kawrgs):
    status = kawrgs.get('status','Not Allowed')
    return HttpResponse(f'<h1> Home app {status}<h1/>')