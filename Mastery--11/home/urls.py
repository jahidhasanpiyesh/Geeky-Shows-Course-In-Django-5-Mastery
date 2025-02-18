from django.urls import path
from home.views import registation,address, loginuser
urlpatterns = [
    path('reg/', registation),
    path('add/', address),
    path('login/', loginuser),
]