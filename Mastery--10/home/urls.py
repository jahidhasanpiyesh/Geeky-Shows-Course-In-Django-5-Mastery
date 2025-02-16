from django.urls import path
from home.views import registation,login
urlpatterns = [
    path('reg/', registation),
    path('login/', login),
]