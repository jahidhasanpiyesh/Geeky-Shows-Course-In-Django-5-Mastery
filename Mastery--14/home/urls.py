from django.urls import path
from .import views
urlpatterns = [
    path('', views.home_get, name='home'),
    path('post/', views.home_post, name='home_post'),
]
