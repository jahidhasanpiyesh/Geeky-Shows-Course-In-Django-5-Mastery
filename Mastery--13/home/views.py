from django.shortcuts import render
from .forms import homeforms
# Create your views here.
def home(request):
    form = homeforms()
    return render(request, 'html/index.html', {'form': form})