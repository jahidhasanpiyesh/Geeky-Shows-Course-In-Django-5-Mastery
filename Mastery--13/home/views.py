from django.shortcuts import render
from .forms import homeforms, demoforms
# Create your views here.
def home(request):
    form = homeforms()
    return render(request, 'html/index.html', {'form': form})

def demo_view(request):
    if request.method == 'POST':
        fm = demoforms(request.POST) 
        if fm.is_valid():
            fm = demoforms()
    else:
        fm = demoforms()

    return render(request, 'html/demo.html', {'fm': fm})