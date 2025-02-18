from django.shortcuts import render
from home.forms import register, addressinfo, login
# Create your views here.

def registation(req):
    res = register()
    return render(req, 'home/index.html',{'registation':res})

def address(req):
    address = addressinfo()
    return render(req, 'home/address.html',{'address':address})

def loginuser(req):
    log = login()
    return render(req,"home/login.html", {'login':log})