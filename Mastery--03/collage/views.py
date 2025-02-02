from django.shortcuts import render

# Create your views here.
def collage(req):
    return render(req,'collage/collage.html')