from django.shortcuts import render

# Create your views here.
# First context base data pass dynamic way
# def home(req):
#     return render(req, 'home/home.html', context={
#         'name':'Django',
#         'roll':'47653',
#     })


# Second context base data pass dynamic way
def home(req):
    name = "Django"
    roll = "65478"
    dic = {'nm':name, 'rol':roll}
    return render(req, 'home/home.html', dic)